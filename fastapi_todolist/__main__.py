from sqlalchemy.orm import Session
from fastapi import FastAPI, Depends, HTTPException, status
import uvicorn
from settings.secret import authentication
from settings.database import engine
from sqlalchemy import metadata
from alembic.env import target_metadata
from harlequelrah_fastapi.appuser import app_user
from harlequelrah_fastapi.middleware import log_middleware
from todolistapp.route import app_todolist
app = FastAPI()
target_metadata.create_all(bind=engine)
app.include_router(app_user)
app.include_router(app_todolist)
app.add_middleware(log_middleware)


if __name__ == "__main__":
    uvicorn.run("__main__:app", host="127.0.0.1", port=8000, reload=True)
