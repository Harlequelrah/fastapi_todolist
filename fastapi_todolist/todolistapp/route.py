from sqlalchemy.orm import Session
from fastapi_todolist.todolistapp.schema import *
from fastapi_todolist.settings.database import get_db
from fastapi_todolist.settings.secret import authentication
from fastapi_todolist.todolistapp.crud import todo_crud
import fastapi_todolist.todolistapp.model as model
from fastapi import Depends, APIRouter
from typing import List
from elrahapi.router.route_config import RouteConfig
from elrahapi.router.router_provider import CustomRouterProvider

router_provider= CustomRouterProvider(
    prefix="/todos",
    tags=["todo"],
    PydanticModel=TodoItem,
    crud=todo_crud,
    # roles=["Manager"]
)
app_todolist = router_provider.get_public_router()

