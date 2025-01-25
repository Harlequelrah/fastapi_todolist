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
from fastapi_todolist.settings.database import Base

from sqlalchemy.sql import func
from sqlalchemy.orm import relationship


class TodoItem(Base):
    __tablename__ = "todoitems"
    id = Column(Integer, primary_key=True)
    titre = Column(String(50), nullable=False)
    description = Column(String(100), nullable=True)
    date_creation = Column(DateTime, nullable=False, default=func.now())
    date_modification = Column(DateTime, nullable=True, onupdate=func.now())
    est_fini=Column(Boolean,default=False)
