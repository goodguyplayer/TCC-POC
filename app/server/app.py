from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from server.routes.logs import routerLogs as LogsRouter
from server.routes.login import routerLogin as LoginRouter

app = FastAPI()

origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:8080",
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(LogsRouter, tags=["Logs"], prefix="/logs")

app.include_router(LoginRouter, tags=["Login"], prefix="/login")

@app.get("/", tags=["Root"])
async def read_root():
    return {"message": "Welcome to this fantastic app!"}
