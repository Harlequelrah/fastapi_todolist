
from fastapi_todolist.userapp.user_crud  import userCrud
from sqlalchemy.orm import Session
from typing import List
from harlequelrah_fastapi.router.route_config import RouteConfig
from harlequelrah_fastapi.router.router_crud import get_single_route
from harlequelrah_fastapi.router.router_namespace import DEFAULTROUTESNAME, USER_AUTH_CONFIG
from harlequelrah_fastapi.user.userRouter import UserRouterProvider


user_router_provider=UserRouterProvider(
        prefix="/users",
        tags=["users"],
        crud=userCrud,
)
app_user=user_router_provider.get_mixed_router(init_data=USER_AUTH_CONFIG,public_routes_name=[DEFAULTROUTESNAME.CREATE],protected_routes_name=[DEFAULTROUTESNAME.READ_ALL_BY_FILTER])
# create_route= get_single_route(DEFAULTROUTESNAME.CREATE)
# read_by_filter_route = get_single_route(DEFAULTROUTESNAME.READ_ALL_BY_FILTER,'protected')
# custom_init_data : List[RouteConfig] = USER_AUTH_CONFIG + [create_route,read_by_filter_route]
# app_user = user_router_provider.initialize_router(init_data=custom_init_data)
