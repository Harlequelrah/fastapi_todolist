from harlequelrah_fastapi.crud.crud_forgery import CrudForgery, LinkClass
from fastapi_todolist.settings.database import authentication
from harlequelrah_fastapi.authorization.privilege_model import (
    PrivilegeCreateModel,
    PrivilegeUpdateModel,
)
from harlequelrah_fastapi.authorization.role_model import (
    RoleCreateModel,
    RoleUpdateModel,
)
from .user_model import Privilege, Role , UserPrivilege
from harlequelrah_fastapi.user.models import UserPrivilegeCreateModel,UserPrivilegeUpdateModel

roleCrud = CrudForgery(
    entity_name="role",
    SQLAlchemyModel=Role,
    CreatePydanticModel=RoleCreateModel,
    UpdatePydanticModel=RoleUpdateModel,
    authentication=authentication,
    Linked_Classes=[LinkClass(key='privileges',Model=Privilege)]
)

privilegeCrud = CrudForgery(
    entity_name="privilege",
    SQLAlchemyModel=Privilege,
    CreatePydanticModel=PrivilegeCreateModel,
    UpdatePydanticModel=PrivilegeUpdateModel,
    authentication=authentication,
)


userPrivilegeCrud=CrudForgery(
    entity_name='user_privilege',
    authentication=authentication,
    SQLAlchemyModel=UserPrivilege,
    CreatePydanticModel=UserPrivilegeCreateModel,
    UpdatePydanticModel= UserPrivilegeUpdateModel
)


