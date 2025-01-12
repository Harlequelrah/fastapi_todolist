from fastapi.responses import JSONResponse
from sqlalchemy.sql import func
from fastapi import HTTPException, status, Depends, Response
from fastapi_todolist.todolistapp.model import TodoItem
from fastapi_todolist.todolistapp.schema import TodoItemCreate, TodoItemUpdate
from sqlalchemy.orm import Session
from harlequelrah_fastapi.utility.utils import update_entity
from harlequelrah_fastapi.crud.crud_forgery import CrudForgery
from fastapi_todolist.settings.database import authentication

todo_crud = CrudForgery(
    entity_name="todo",
    session_factory=authentication.session_factory,
    SQLAlchemyModel=TodoItem,
    CreatePydanticModel=TodoItemCreate,
    UpdatePydanticModel=TodoItemUpdate,
)
