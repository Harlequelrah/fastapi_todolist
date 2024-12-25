from fastapi_todolist.todolistapp import model
from sqlalchemy import MetaData
from fastapi_todolist.userapp import user_model
from fastapi_todolist.settings import logger_model


target_metadata = MetaData()
target_metadata = model.Base.metadata
target_metadata = logger_model.Base.metadata
target_metadata = user_model.Base.metadata
