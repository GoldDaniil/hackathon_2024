from sqlalchemy.orm import Session
import models
from datetime import datetime

def get_user_by_username(db: Session, username: str):#получение пользователя по имени
    return db.query(models.User).filter(models.User.username == username).first()

def create_user(db: Session, username: str, password_hash: str, email: str):#создание нового пользователя
    db_user = models.User(username=username, password_hash=password_hash, email=email)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_server_by_id(db: Session, server_id: int):#получение сервера по ID
    return db.query(models.Server).filter(models.Server.id == server_id).first()

def get_all_servers(db: Session):#получение всех серверов
    return db.query(models.Server).all()

def create_server(db: Session, name: str, ip_address: str):#создание нового сервера
    db_server = models.Server(name=name, ip_address=ip_address)
    db.add(db_server)
    db.commit()
    db.refresh(db_server)
    return db_server

def create_reservation(db: Session, user_id: int, server_id: int, start_time: datetime, end_time: datetime):#создание нового бронирования
    db_reservation = models.Reservation(user_id=user_id, server_id=server_id, start_time=start_time, end_time=end_time)
    db.add(db_reservation)
    db.commit()
    db.refresh(db_reservation)
    return db_reservation

def get_reservations_for_user(db: Session, user_id: int):#получение всех бронирований для пользователя
    return db.query(models.Reservation).filter(models.Reservation.user_id == user_id).all()
