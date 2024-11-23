from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from .models_base import Base#импорт Base из models_base.py
from sqlalchemy.ext.declarative import declarative_base

#URL для подключения к базе данных
DATABASE_URL = "postgresql://gold:1234@localhost:5432/resource_booking"

engine = create_engine(DATABASE_URL)#создание подключения к базе данных

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)#настроим сессию для работы с базой данных

Base = declarative_base()#определение базового класса для моделей

def init_db():#инициализации базы данных
    Base.metadata.create_all(bind=engine)#создаем все таблицы - определенные в моделях
