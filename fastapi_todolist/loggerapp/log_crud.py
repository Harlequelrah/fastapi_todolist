from harlequelrah_fastapi.middleware.logCrud import LoggerCrud
from fastapi_todolist.settings.secret import authentication

# from loggerapp.log_model import Logger
from fastapi_todolist.settings.logger_model import Logger

logCrud= LoggerCrud(session_factory=authentication.session_factory,LoggerModel=Logger)
