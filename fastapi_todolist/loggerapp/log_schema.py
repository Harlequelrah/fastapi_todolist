from pydantic import BaseModel
from elrahapi.middleware.models import LoggerMiddlewarePydanticModel
class LogBaseModel(LoggerMiddlewarePydanticModel):
    class Config:
        from_orm=True



