from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from datetime import datetime
import crud, models
from database import SessionLocal
from fastapi.middleware.cors import CORSMiddleware
from pathlib import Path

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Разрешите фронтенду доступ
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def get_db():#получение сессии базы данных
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/users/")#регистрация нового пользователя
def create_user(username: str, password_hash: str, email: str, db: Session = Depends(get_db)):
    db_user = crud.create_user(db=db, username=username, password_hash=password_hash, email=email)
    return db_user

@app.get("/users/{username}")#получение пользователя по имени
def get_user(username: str, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_username(db=db, username=username)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

@app.post("/servers/")#создание нового сервера
def create_server(name: str, ip_address: str, db: Session = Depends(get_db)):
    db_server = crud.create_server(db=db, name=name, ip_address=ip_address)
    return db_server

@app.get("/servers/")#получение всех серверов
def get_all_servers(db: Session = Depends(get_db)):
    servers = crud.get_all_servers(db=db)#получение серверов через функцию CRUD
    return servers

@app.get("/servers/{server_id}")#получение сервера по ID
def get_server(server_id: int, db: Session = Depends(get_db)):
    db_server = crud.get_server_by_id(db=db, server_id=server_id)
    if db_server is None:
        raise HTTPException(status_code=404, detail="Server not found")
    return db_server

@app.post("/reservations/")#создание нового бронирования
def create_reservation(user_id: int, server_id: int, start_time: datetime, end_time: datetime, db: Session = Depends(get_db)):
    db_reservation = crud.create_reservation(db=db, user_id=user_id, server_id=server_id, start_time=start_time, end_time=end_time)
    return db_reservation

@app.get("/reservations/{user_id}")#получение всех бронирований пользователя
def get_user_reservations(user_id: int, db: Session = Depends(get_db)):
    reservations = crud.get_reservations_for_user(db=db, user_id=user_id)
    if not reservations:
        raise HTTPException(status_code=404, detail="No reservations found")
    return reservations

@app.post("/servers/{server_id}/reinstall")#переустановки сервера
def reinstall_server(server_id: int, db: Session = Depends(get_db)):
    #проверяем, существует ли сервер
    db_server = crud.get_server_by_id(db=db, server_id=server_id)
    if db_server is None:
        raise HTTPException(status_code=404, detail="Server not found")

    # тоже можно получать из квери параметром, предоставив выбор админу
    os_name = "ubuntu-24.04.1-live-server-arm64"
    # mac_address = db_server.mac_address  #MAC-адрес сервера. Его нет в бд, поэтому пока мок
    mac_address = "00:1A:2B:3C:4D:5E"
    if not mac_address:
        raise HTTPException(status_code=400, detail="MAC address not found for the server")

    #создаем конфигурацию PXE
    pxe_config = f"""
DEFAULT install
LABEL install
    KERNEL vmlinuz
    APPEND initrd=initrd.img root=/dev/ram0 ip=dhcp url=http://192.168.1.12:8080/{os_name}.iso
    """

    #используем функцию write_pxe_config для сохранения конфигурации
    try:
        result = write_pxe_config(mac_address, pxe_config)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to write PXE config: {str(e)}")

    return {"status": "success", "message": f"PXE configuration saved for server {server_id}", "path": result["path"]}



def write_pxe_config(mac_address: str, config_data: str):
    #общий volume
    shared_dir = Path("/app/shared/pxelinux.cfg")
    shared_dir.mkdir(parents=True, exist_ok=True)

    #PXE конфигурация для заданного MAC-адреса
    config_file = shared_dir / f"01-{mac_address.replace(':', '-')}"

    with open(config_file, "w") as f:
        f.write(config_data)

    return {"status": "success", "path": str(config_file)}