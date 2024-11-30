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

class TodoItem(Base):
    __tablename__='todoitems'
    id = Column(Integer, primary_key=True)
    email=Column(String(255),index=True,nullable=False)
    titre=Column(String(50),nullable=False)
    description=Column(String(100),nullable=True)
    date_creation=Column(DateTime,nullable=False,default=func.now())
    date_modification=Column(DateTime,nullable=True,onupdate=func.now())
