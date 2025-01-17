from fastapi_todolist.settings.database import Base, authentication
from sqlalchemy import Boolean, Column, ForeignKey, Integer, Table
from harlequelrah_fastapi.exception.auth_exception import INSUFICIENT_PERMISSIONS_CUSTOM_HTTP_EXCEPTION
from harlequelrah_fastapi.user import models
from sqlalchemy.orm import relationship
from harlequelrah_fastapi.authorization.role_model import RoleModel
from harlequelrah_fastapi.authorization.privilege_model import PrivilegeModel
from sqlalchemy.orm import relationship


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


class UserPrivilege(Base):
    __tablename__ = "user_privileges"
    user_id = Column(Integer, ForeignKey("users.id"), primary_key=True)
    privilege_id = Column(Integer, ForeignKey("privileges.id"), primary_key=True)
    user = relationship("User", back_populates="privileges")
    privilege = relationship("Privilege", back_populates="users")
    is_active=Column(Boolean,default=True)


class User(Base, models.User):
    __tablename__ = "users"
    role_id=Column(Integer, ForeignKey("roles.id"))
    role = relationship("Role", back_populates="users")
    privileges = relationship("UserPrivilege",back_populates="user")

    def has_role(self,role_name:str):
        if role_name.upper() == self.role.normalizedName : return True
        else :raise INSUFICIENT_PERMISSIONS_CUSTOM_HTTP_EXCEPTION

    def has_privilege(self,privilege_name:str):
        for privilege in self.privileges :
            if privilege.normalizedName == privilege_name.upper() :
                return True
        else : raise INSUFICIENT_PERMISSIONS_CUSTOM_HTTP_EXCEPTION


authentication.User = User
metadata= Base.metadata
