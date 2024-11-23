from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from passlib.context import CryptContext
from sqlalchemy.orm import Session
from . import models, database
import jwt
from datetime import datetime, timedelta

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")#создаем объект безопасности
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

SECRET_KEY = "mysecretkey"#секретный ключ для JWT
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30


def get_password_hash(password):#хэширования пароля
    return pwd_context.hash(password)

def verify_password(plain_password, hashed_password):#проверка пароля
    return pwd_context.verify(plain_password, hashed_password)

def get_user(db: Session, username: str):#получения пользователя по имени
    return db.query(models.User).filter(models.User.username == username).first()

def create_access_token(data: dict, expires_delta: timedelta = timedelta(minutes=15)):#создание токена
    to_encode = data.copy()
    expire = datetime.utcnow() + expires_delta
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

from fastapi import APIRouter#эндпоинт для получения токена

router = APIRouter()

@router.post("/token")
def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(database.get_db)):
    user = get_user(db, form_data.username)
    if not user or not verify_password(form_data.password, user.password_hash):
        raise HTTPException(
            status_code=400,
            detail="Incorrect username or password",
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}

@router.post("/register")#эндпоинт для регистрации пользователя
def register_user(username: str, password: str, db: Session = Depends(database.get_db)):
    user = get_user(db, username)
    if user:
        raise HTTPException(status_code=400, detail="Username already registered")
    
    hashed_password = get_password_hash(password)
    new_user = models.User(username=username, password_hash=hashed_password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user
