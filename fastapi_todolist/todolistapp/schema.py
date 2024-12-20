from pydantic import BaseModel, Field
from typing import List, Optional
from datetime import datetime
from decimal import Decimal
from fastapi import Form


class TodoItemBase(BaseModel):
    description : Optional[str] = Field(
        default=None, title="La description de la tâche", max_length=100
    )


class TodoItemCreate(TodoItemBase):
    titre: str = Field(title="Le titre de la tâche", max_length=100)
    email: str = Field(title="Adresse email utilisateur ", max_length=100)


class TodoItemUpdate(TodoItemBase):
    titre: Optional[str] = Field(
        default=None, title="Le titre de la tâche", max_length=100
    )
    email: Optional[str] = Field(
        default=None, title="Adresse email utilisateur ", max_length=100
    )


class TodoItem(TodoItemCreate):
    id: int
    date_creation: datetime
    date_modification: Optional[datetime]=None

    class setting:
        from_orm=True
