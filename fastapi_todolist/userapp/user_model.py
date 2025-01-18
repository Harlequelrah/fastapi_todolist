from fastapi_todolist.settings.database import Base, authentication
from sqlalchemy import Boolean, Column, ForeignKey, Integer, Table
from harlequelrah_fastapi.exception.auth_exception import INSUFICIENT_PERMISSIONS_CUSTOM_HTTP_EXCEPTION
from harlequelrah_fastapi.user import models
from sqlalchemy.orm import relationship
from harlequelrah_fastapi.authorization.role_model import RoleModel
from harlequelrah_fastapi.authorization.privilege_model import PrivilegeModel


class Privilege(PrivilegeModel,Base):
    __tablename__ = "privileges"
    roles = relationship(
        "Role", secondary="role_privileges", back_populates="privileges"
    )
    users = relationship("UserPrivilege", back_populates="privilege")


class Role(RoleModel,Base):
    __tablename__ = "roles"
    users = relationship("User", back_populates="role")
    privileges = relationship(
        "Privilege", secondary="role_privileges", back_populates="roles"
    )


role_privileges = Table(
    "role_privileges",
    Base.metadata,
    Column("role_id", Integer, ForeignKey("roles.id")),
    Column("privilege_id", Integer, ForeignKey("privileges.id")),
)


class UserPrivilege(models.UserPrivilege):
    __tablename__ = "user_privileges"
    user = relationship("User", back_populates="privileges")
    privilege = relationship("Privilege", back_populates="users")


class User(Base, models.User):
    __tablename__ = "users"
    role = relationship("Role", back_populates="users")
    privileges = relationship("UserPrivilege", back_populates="user")


authentication.User = User
metadata= Base.metadata
