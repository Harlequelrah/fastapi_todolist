from sqlalchemy.orm import Session
from todolistapp.schema import *
from settings.database import get_db
from settings.secret import authentication
import todolistapp.crud as crud
import todolistapp.model as model
from fastapi import Depends, APIRouter
from typing import List
get_curent_user=authentication.get_current_user
app_todolist = APIRouter(prefix="/todoitem", tags=["todo"])

@app_todolist.get("/get-todoitem/{todoitem_id}",response_model=TodoItem)
async def get_todoitem(todoitem_id:int,db:Session=Depends(get_db)):
    return await crud.get_todoitem(todoitem_id,db)

@app_todolist.get("/get-todoitems",response_model=List[TodoItem])
async def get_todos(skip:int = 0, limit: int = 10, db: Session=Depends(get_db)):
    return await crud.get_all_todoitems(skip, limit, db)

@app_todolist.post("/create-todoitem",response_model=TodoItem)
async def create_todo(todoitem:TodoItemCreate,db:Session=Depends(get_db)):
    return await crud.create_todoitem(db, todoitem)

@app_todolist.put("/update-todoitem/{todoitem_id}",response_model=TodoItem)
async def update_todoitem(todoitem_id:int, todoitem: TodoItemUpdate, db: Session=Depends(get_db)):
    return await crud.update_todoitem(todoitem_id, todoitem, db)

@app_todolist.delete("/delete-todoitem/{todoitem_id}")
async def delete_todoitem(todoitem_id:int, db: Session=Depends(get_db)):
    return await crud.delete_todoitem(todoitem_id, db)
