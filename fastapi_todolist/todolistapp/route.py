from sqlalchemy.orm import Session
from todolistapp.schema import *
from settings.database import get_db
from settings.secret import authentication
import todolistapp.crud as crud
import todolistapp.model as model
from fastapi import Depends, APIRouter
from typing import List
app_todolist = APIRouter(prefix="/todoitem", tags=["todo"])

@app_todolist.get("/get-todoitem/{todoitem_id}",response_model=TodoItem)
async def get_todoitem(todoitem_id:int):
    return await crud.get_todoitem(todoitem_id)

@app_todolist.get("/get-todoitems",response_model=List[TodoItem])
async def get_todos(skip:int = 0, limit: int = 10):
    return await crud.get_all_todoitems(skip, limit)

@app_todolist.post("/create-todoitem",response_model=TodoItem)
async def create_todo(todoitem:TodoItemCreate):
    return await crud.create_todoitem( todoitem)

@app_todolist.put("/update-todoitem/{todoitem_id}",response_model=TodoItem)
async def update_todoitem(todoitem_id:int, todoitem: TodoItemUpdate):
    return await crud.update_todoitem(todoitem_id, todoitem)

@app_todolist.delete("/delete-todoitem/{todoitem_id}")
async def delete_todoitem(todoitem_id:int):
    return await crud.delete_todoitem(todoitem_id)
