from sqlalchemy.orm import Session
from fastapi_todolist.todolistapp.schema import *
from fastapi_todolist.settings.database import get_db
from fastapi_todolist.settings.secret import authentication
from fastapi_todolist.todolistapp.crud import todo_crud
import fastapi_todolist.todolistapp.model as model
from fastapi import Depends, APIRouter
from typing import List
from harlequelrah_fastapi.router.router_provider import provide_router
app_todolist=  provide_router(
    prefix='/todoitem',
    tags=["todo"],
    PydanticModel=TodoItem,
    crud=todo_crud,
    authentication=authentication
)

