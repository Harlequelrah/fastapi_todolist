from sqlalchemy.sql import func
from fastapi import HTTPException, status, Depends, Response
from todolistapp.model import TodoItem
from todolistapp.schema import TodoItemCreate,TodoItemUpdate
from sqlalchemy.orm import Session
from harlequelrah_fastapi.utility.utils import update_entity
from settings.database import authentication


dependencies=[Depends(authentication.get_session),Depends(authentication.get_current_user)]
async def create_todoitem(
    todoitem_create: TodoItemCreate,
    db: Session = dependencies[0],
):
    todoitem=TodoItem(**todoitem_create.dict())
    db.add(todoitem)
    db.commit()
    db.refresh(todoitem)
    return todoitem


async def get_todoitem(todoitem_id: int, db: Session=dependencies[0]):
    return db.query(TodoItem).filter(TodoItem.id == todoitem_id).first()


async def get_all_todoitems(
    skip: int = 0,
    limit: int = None,
    db: Session = dependencies[0],
):
    return db.query(TodoItem).offset(skip).limit(limit).all()


async def delete_todoitem(todoitem_id:int,db:Session=dependencies[0],access_token:str=dependencies[1]):
    todoitem=get_todoitem(todoitem_id,db)
    if todoitem is not None:
        db.delete(todoitem)
        db.commit()
        return Response(status_code=200,content="The entity has been deleted with success")

async def update_todoitem(todoitem_id:int,todoitem_update:TodoItemUpdate,db:Session=dependencies[0],access_token=dependencies[1]):
    todoitem= await get_todoitem(todoitem_id,db)
    if todoitem is not None:
        update_entity(todoitem, todoitem_update)
        db.commit()
        db.refresh(todoitem)
        return todoitem
