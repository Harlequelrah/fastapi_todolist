from pydantic import BaseModel, Field
from typing import List, Optional
from datetime import datetime
from decimal import Decimal
from fastapi import Form

class TodoItemCreate(BaseModel):
    titre:str
    email:str
    description=Optional[str]=None
class TodoItemUpdate(TodoItemCreate):
    titre: Optional[str] = Field(
        default=None, title="Le titre de la tâche", max_length=100
    )
    email: Optional[str] = Field(
        default=None, title="Adresse email utilisateur ", max_length=100
    )
    description: Optional[str]=Field(None, title="La description de la tâche", max_length=100)

class TodoItem(TodoItemCreate):
    id:int
    date_creation:datetime
    date_modification:datetime
