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
    est_fini:Optional[bool]=Field(example=True,default=False)


class TodoItemUpdate(TodoItemBase):
    titre: str = Field(example="Le titre de la tâche", max_length=100
    )
    est_fini:Optional[bool]=Field(example=True,default=False)



class TodoItem(TodoItemCreate):
    id: int
    date_creation: datetime
    date_modification: Optional[datetime]=None

    class Config:
        from_attributes=True
