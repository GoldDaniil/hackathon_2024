import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, User, Server, Reservation#модели из models.py

#строка подключения к базе данных (можно использовать переменную окружения или строку подключения напрямую)
DATABASE_URL = os.environ.get("DATABASE_URL")

#создание подключения к базе данных
engine = create_engine(DATABASE_URL, echo=True)#echo=True для логирования SQL запросов

#создание сессии для работы с базой данных
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

#функция для создания всех таблиц
def create_tables():
    #создание таблиц - если их нет
    Base.metadata.create_all(bind=engine)
    print("Tables created successfully.")

create_tables()
