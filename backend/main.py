from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from datetime import datetime
from . import crud, models
from .database import SessionLocal

app = FastAPI()

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
