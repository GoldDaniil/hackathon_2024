from sqlalchemy.orm import Session
from . import models, crud, database

db = database.SessionLocal()#создание новой сессии

def test_create_user():#тест создания нового пользователя
    new_user = crud.create_user(db=db, username='test_user', password_hash='hashed_password', email='test_user@example.com')
    print(new_user)

def test_get_user_by_username():#тест получения пользователя по имени
    user_from_db = crud.get_user_by_username(db=db, username='test_user')
    print(user_from_db)

def test_create_booking():#тест создания нового бронирования (используем Reservation - а не Booking)
    new_booking = models.Reservation(user_id=1, server_id=1, start_time="2024-11-24 10:00:00", end_time="2024-11-24 12:00:00")
    db.add(new_booking)
    db.commit()
    db.refresh(new_booking)
    print(new_booking)

if __name__ == "__main__":
    test_create_user()
    test_get_user_by_username()
    test_create_booking()

db.close()#закрываем сессию
