from elrahapi.user import models
from fastapi_todolist.settings import authentication
class UserBaseModel(models.UserBaseModel):
    pass

class UserCreateModel(models.UserCreateModel):
    pass

class UserUpdateModel(models.UserUpdateModel):
    pass


class UserPydanticModel(UserBaseModel):
    class Config :
        from_orm=True

authentication.UserPydanticModel = UserPydanticModel
authentication.UserCreateModel = UserCreateModel
authentication.UserUpdateModel = UserUpdateModel


