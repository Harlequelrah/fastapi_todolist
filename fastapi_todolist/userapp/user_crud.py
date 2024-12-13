from sqlalchemy.sql import func
from sqlalchemy.orm import Session
from fastapi.responses import JSONResponse
from fastapi import HTTPException as HE, Response, status, Depends
from settings.database import authentication
from sqlalchemy import or_
from harlequelrah_fastapi.utility.utils import update_entity

User = authentication.User
UserLoginModel = authentication.User
UserCreate = authentication.UserCreateModel
UserUpdate = authentication.UserUpdateModel



async def get_count_users(db: Session):
    return db.query(func.count(User.id)).scalar()


async def is_unique(sub: str, db: Session):
    user = db.query(User).filter(or_(User.email == sub, User.username == sub)).first()
    return user is None


async def create_user(
    user: UserCreate,
    db: Session,
):
    new_user = User(**user.dict())
    if not await is_unique(new_user.email, db) or not await is_unique(
        new_user.username, db
    ):
        raise HE(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Le nom d'utilisateur ou l'email existe déjà",
        )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


async def get_user(
    db: Session ,
    id: int = None,
    sub: str = None,
):
    user = (
        db.query(User)
        .filter(or_(User.username == sub, User.email == sub, User.id == id))
        .first()
    )
    return user


async def get_users(
    db: Session,
    skip: int = 0,
    limit: int = None,
):
    limit = await get_count_users(db)
    users = db.query(User).offset(skip).limit(limit).all()
    return users

async def delete_user(user_id:int,db:Session):
    user = await get_user(db,id=user_id)
    db.delete(user)
    db.commit()
    return JSONResponse(status_code=200,content={'message': 'User deleted successfully'})

async def update_user(
    db: Session,
    user_id: int,
    user: UserUpdate,

):
    existing_user = await get_user(db, user_id)
    update_entity(existing_user, user)
    db.commit()
    db.refresh(existing_user)
    return existing_user
