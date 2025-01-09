from pydantic import BaseModel
from harlequelrah_fastapi.middleware.models import LoggerMiddlewarePydanticModel
class LogBaseModel(LoggerMiddlewarePydanticModel):
    class Config:
        from_orm=True



