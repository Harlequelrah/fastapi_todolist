from harlequelrah_fastapi.crud.crud_forgery import CrudForgery
from fastapi_todolist.settings.secret import authentication
from fastapi_todolist.settings.logger_model import Logger

logCrud = CrudForgery(
    entity_name="log",
    session_factory=authentication.session_factory,
    SQLAlchemyModel=Logger,
)
