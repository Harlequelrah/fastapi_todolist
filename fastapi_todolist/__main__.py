from sqlalchemy.orm import Session
from fastapi import FastAPI, Depends, HTTPException, status
import uvicorn
from settings.database import engine, authentication, sessionLocal
from settings import logger_model
from settings.models_metadata import target_metadata
from userapp.app_user import app_user
from loggerapp.log_router import app_logger
from harlequelrah_fastapi.middleware.error_middleware import ErrorHandlingMiddleware
from harlequelrah_fastapi.middleware.log_middleware import LoggerMiddleware
from todolistapp.route import app_todolist

app = FastAPI()

target_metadata.create_all(bind=engine)


app.include_router(app_user)
app.include_router(app_todolist)
app.include_router(app_logger)
app.add_middleware(
    ErrorHandlingMiddleware,
    LoggerMiddlewareModel=logger_model.Logger,
    session_factory=authentication.session_factory,
)
app.add_middleware(
    LoggerMiddleware,
    LoggerMiddlewareModel=logger_model.Logger,
    session_factory=authentication.session_factory,
)

if __name__ == "__main__":
    uvicorn.run("__main__:app", host="0.0.0.0", port=8000, reload=True)
