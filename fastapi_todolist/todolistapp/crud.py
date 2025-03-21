from fastapi.responses import JSONResponse
from sqlalchemy.sql import func
from fastapi import HTTPException, status, Depends, Response
from fastapi_todolist.todolistapp.model import TodoItem
from fastapi_todolist.todolistapp.schema import TodoItemCreate, TodoItemUpdate
from sqlalchemy.orm import Session
from elrahapi.utility.utils import update_entity
from elrahapi.crud.crud_forgery import CrudForgery
from fastapi_todolist.settings.database import authentication

todo_crud = CrudForgery(
    entity_name="todo",
    authentication=authentication,
    SQLAlchemyModel=TodoItem,
    CreatePydanticModel=TodoItemCreate,
    UpdatePydanticModel=TodoItemUpdate,
)
