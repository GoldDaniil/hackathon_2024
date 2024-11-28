from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Boolean
from sqlalchemy.orm import relationship
from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    password_hash = Column(String)
    email = Column(String, index=True)
    is_admin = Column(Boolean, default=False)
    reservations = relationship("Reservation", back_populates="user")


class Server(Base):
    __tablename__ = "servers"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True)
    ip_address = Column(String)
    status = Column(String, default="inactive")
    created_at = Column(DateTime, default=datetime.utcnow)
    reservations = relationship("Reservation", back_populates="server")


class Reservation(Base):
    __tablename__ = "reservations"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    server_id = Column(Integer, ForeignKey('servers.id'))
    start_time = Column(DateTime)
    end_time = Column(DateTime)
    created_at = Column(DateTime, default=datetime.utcnow)
    user = relationship("User", back_populates="reservations")
    server = relationship("Server", back_populates="reservations")
