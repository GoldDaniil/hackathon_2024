from backend.database import init_db
from backend.models import Base
from backend.database import engine

init_db()#инициализация базы данных
print("Database initialized successfully.")

Base.metadata.create_all(bind=engine)#создание всех таблиц
