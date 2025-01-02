from sqlalchemy.orm import Session
from fastapi import Depends, HTTPException, status
from harlequelrah_fastapi.authentication.token import Token, AccessToken, RefreshToken
from fastapi.security import OAuth2PasswordRequestForm
from fastapi import APIRouter, Depends
import fastapi_todolist.userapp.user_crud as crud
from sqlalchemy.orm import Session
from typing import List
from fastapi_todolist.settings.database import authentication
from harlequelrah_fastapi.authentication.authenticate import AUTHENTICATION_EXCEPTION
from harlequelrah_fastapi.user.userCrud import UserCrud, UserCrudForgery
from harlequelrah_fastapi.user.userRouter import UserRouterProvider

userCrud= UserCrudForgery(authentication)
user_router_provider=UserRouterProvider(
        prefix="/users",
        tags=["users"],
        crud=userCrud,
)
app_user =  user_router_provider.get_protected_router()
