from sqlalchemy.sql import func
from fastapi import HTTPException, status, Depends, Response
from todolistapp.model import TodoItem
from todolistapp.schema import TodoItemCreate,TodoItemUpdate
from sqlalchemy.orm import Session
from harlequelrah_fastapi.utility.utils import update_entity

async def create_todoitem(db:Session,todoitem_create:TodoItemCreate):
    todoitem=TodoItem(**todoitem_create.dict())
    db.add(todoitem)
    db.commit()
    db.refresh(todoitem)
    return todoitem

async def get_todoitem(todoitem_id: int, db: Session):
    return db.query(TodoItem).filter(TodoItem.id == todoitem_id).first()

async def get_all_todoitems(db: Session,skip:int=0,limit:int=None):
    return db.query(TodoItem).offset(skip).limit(limit).all()

async def delete_todoitem(todoitem_id:int,db:Session):
    todoitem=get_todoitem(todoitem_id,db)
    if todoitem is not None:
        db.delete(todoitem)
        db.commit()
        return Response(status_code=200,content="The entity has been deleted with success")

async def update_todoitem(todoitem_id:int,todoitem_update:TodoItemUpdate,db:Session):
    todoitem=get_todoitem(todoitem_id,db)
    if todoitem is not None:
        update_entity(todoitem, todoitem_update)
        db.commit()
        db.refresh(todoitem)
        return todoitem
