from sqlalchemy.orm import Session
from fastapi_todolist.todolistapp.schema import *
from fastapi_todolist.settings.database import get_db
from fastapi_todolist.settings.secret import authentication
import fastapi_todolist.todolistapp.crud as crud
import fastapi_todolist.todolistapp.model as model
from fastapi import Depends, APIRouter
from typing import List

app_todolist = APIRouter(prefix="/todoitem", tags=["todo"])
dependencies = [
    Depends(authentication.get_session),
    Depends(authentication.get_current_user),
]


@app_todolist.get("/get-todoitem/{todoitem_id}", response_model=TodoItem)
async def get_todoitem(todoitem_id: int, db: Session = dependencies[0]):
    return await crud.get_todoitem(db=db,todoitem_id=todoitem_id)


@app_todolist.get("/get-todoitems", response_model=List[TodoItem])
async def get_todos(db:Session= dependencies[0],skip: int = 0, limit: int =None):
    return await crud.get_all_todoitems(db,skip, limit)


@app_todolist.post("/create-todoitem", response_model=TodoItemCreate)
async def create_todo(todoitem: TodoItemCreate, db: Session = dependencies[0]):
    return await crud.create_todoitem(db,todoitem)


@app_todolist.put("/update-todoitem/{todoitem_id}", response_model=TodoItem)
async def update_todoitem(
    todoitem_id: int, todoitem: TodoItemUpdate, db: Session = dependencies[0],access_token:str=dependencies[1]
):
    return await crud.update_todoitem(db,todoitem_id, todoitem)


@app_todolist.delete("/delete-todoitem/{todoitem_id}")
async def delete_todoitem(todoitem_id: int, db: Session = dependencies[0],access_token:str=dependencies[1]):
    return await crud.delete_todoitem(db=db,todoitem_id=todoitem_id)
