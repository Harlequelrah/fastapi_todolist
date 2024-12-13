from sqlalchemy.orm import Session
from fastapi import FastAPI, Depends, HTTPException, status
import uvicorn
from settings.database import engine, authentication, sessionLocal
from settings import logger_model
from todolistapp import model
from sqlalchemy import MetaData
from userapp import user_model
from userapp.app_user import app_user
from harlequelrah_fastapi.middleware.error_middleware import ErrorHandlingMiddleware
from harlequelrah_fastapi.middleware.log_middleware import LoggerMiddleware
from todolistapp.route import app_todolist

app = FastAPI()
target_metadata = MetaData()
target_metadata = model.Base.metadata
target_metadata = logger_model.Base.metadata
target_metadata = user_model.Base.metadata
target_metadata.create_all(bind=engine)


app.include_router(app_user)
app.include_router(app_todolist)
app.add_middleware(ErrorHandlingMiddleware)
app.add_middleware(
    LoggerMiddleware,
    LoggerMiddlewareModel=logger_model.Logger,
    db_session=authentication.get_session,
)


if __name__ == "__main__":
    uvicorn.run("__main__:app", host="127.0.0.1", port=8000, reload=True)
