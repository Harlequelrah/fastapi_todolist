from fastapi import (
    FastAPI,
    WebSocketDisconnect,
    WebSocket,
)

from fastapi_todolist.settings.database import engine, authentication
from fastapi_todolist.settings import logger_model
from fastapi_todolist.settings.models_metadata import target_metadata
from fastapi_todolist.loggerapp.log_router import app_logger
from fastapi_todolist.userapp.user_routers import app_role,app_privilege,app_user_privilege,app_role_privilege,app_user
from harlequelrah_fastapi.middleware.error_middleware import ErrorHandlingMiddleware
from harlequelrah_fastapi.middleware.log_middleware import LoggerMiddleware
from fastapi_todolist.todolistapp.route import app_todolist
from harlequelrah_fastapi.websocket.connectionManager import ConnectionManager


app = FastAPI()
manager = ConnectionManager()
target_metadata.create_all(bind=engine)


app.include_router(app_user)
app.include_router(app_todolist)
app.include_router(app_logger)
app.include_router(app_role)
app.include_router(app_privilege)
app.include_router(app_user_privilege)
app.include_router(app_role_privilege)
from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Permet les requêtes depuis toutes les origines.
    allow_credentials=True,
    allow_methods=["*"],  # Autorise toutes les méthodes HTTP.
    allow_headers=["*"],  # Autorise tous les en-têtes nécessaires.
)


app.add_middleware(
    ErrorHandlingMiddleware,
    LoggerMiddlewareModel=logger_model.Logger,
    session_factory=authentication.session_factory,
    manager=manager,
)
app.add_middleware(
    LoggerMiddleware,
    LoggerMiddlewareModel=logger_model.Logger,
    session_factory=authentication.session_factory,
    manager=manager,
)


@app.websocket("/ws/notifications")
async def websocket_notification(websocket: WebSocket):
    await manager.connect(websocket)
    try:
        while True:
            data = await websocket.receive_text()
            await manager.send_message(data)
    except WebSocketDisconnect:
        await manager.disconnect(websocket)
