from fastapi_todolist.userapp.user_crud import userCrud
from sqlalchemy.orm import Session
from typing import List
from harlequelrah_fastapi.router.route_config import RouteConfig
from harlequelrah_fastapi.router.router_crud import exclude_route, get_single_route
from harlequelrah_fastapi.router.router_namespace import (
    ROUTES_PROTECTED_CONFIG,
    DefaultRoutesName,
    USER_AUTH_CONFIG_ROUTES,
)
from harlequelrah_fastapi.router.user_router_provider import UserRouterProvider


user_router_provider = UserRouterProvider(
    prefix="/users",
    tags=["users"],
    crud=userCrud,
)
custom_init_data = USER_AUTH_CONFIG_ROUTES + exclude_route(ROUTES_PROTECTED_CONFIG,[DefaultRoutesName.CREATE,DefaultRoutesName])
app_user = user_router_provider.get_mixed_router(
    init_data= custom_init_data ,
    public_routes_name=[DefaultRoutesName.CREATE],
)

