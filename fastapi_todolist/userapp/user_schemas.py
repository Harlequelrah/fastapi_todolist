from elrahapi.user import model
from fastapi_todolist.settings import authentication
class UserBaseModel(model.UserBaseModel):
    pass

class UserCreateModel(model.UserCreateModel):
    pass

class UserUpdateModel(model.UserUpdateModel):
    pass


class UserPydanticModel(UserBaseModel):
    class Config :
        from_attributes=True

authentication.UserPydanticModel = UserPydanticModel
authentication.UserCreateModel = UserCreateModel
authentication.UserUpdateModel = UserUpdateModel


