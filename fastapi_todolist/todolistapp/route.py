from sqlalchemy.orm import Session
from fastapi_todolist.todolistapp.schema import *
from fastapi_todolist.settings.database import get_db
from fastapi_todolist.settings.secret import authentication
from fastapi_todolist.todolistapp.crud import todo_crud
import fastapi_todolist.todolistapp.model as model
from fastapi import Depends, APIRouter
from typing import List
from harlequelrah_fastapi.router.route_config import RouteConfig
from harlequelrah_fastapi.router.router_provider import CustomRouterProvider

router_provider= CustomRouterProvider(
    prefix="/todoitem",
    tags=["todo"],
    PydanticModel=TodoItem,
    crud=todo_crud,
    get_access_token=authentication.get_access_token
)
# app_todolist = router_provider.get_default_router()
# app_todolist = router_provider.get_protected_router()

init_data:List[RouteConfig]=[
    RouteConfig(route_name='create',is_activated=True),
    RouteConfig(route_name='read-one', is_activated=True,is_protected=True),
    RouteConfig(route_name='update', is_activated=True,is_protected=True),
    RouteConfig(route_name='delete', is_activated=True,is_protected=True),
]
app_todolist= router_provider.initialize_router(init_data=init_data)
