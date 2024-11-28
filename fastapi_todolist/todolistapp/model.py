from sqlalchemy import (
    Boolean,
    Column,
    DECIMAL,
    Integer,
    String,
    DateTime,
    ForeignKey,
    Table,
)
from  settings.database import Base
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from harlequelrah_fastapi.middleware.model import LoggerMiddleware
class Logger(Base,LoggerMiddleware):
    __tablename__='loggers'

class TodoItem(Base):
    __tablename___='todoitems'
    email=Column(String(255),index=True,nullable=False)
    id=Column(Integer,primary_key=True)
    titre=Column(String(50),nullable=False)
    description=Column(String(100),nullable=True,blank=True)
    date_creation=Column(DateTime,nullable=False,default=func.now())
    date_modification=Column(DateTime,nullable=True,onupdate=func.now())



