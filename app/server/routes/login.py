from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder

from server.database import (
    retrieve_logins,
    retrieve_login,
    add_login_data,
)

from server.models.login import (
    ErrorResponseModelLogin,
    ResponseModelLogin,
    LoginSchema
)

routerLogin = APIRouter()

@routerLogin.get("/", response_description="Login retrieved")
async def get_login():
    login = await retrieve_logins()
    if login:
        return ResponseModelLogin(login, "Login data retrieved successfully")
    return ResponseModelLogin(login, "Empty list returned")


@routerLogin.get("/{id}", response_description="Login data retrieved")
async def get_login_data(id):
    login = await retrieve_login(id)
    if login:
        return ResponseModelLogin(login, "Login data retrieved successfully")
    return ErrorResponseModelLogin("An error occurred.", 404, "Login doesn't exist.")

@routerLogin.post("/", response_description="login data added into the database")
async def add_login(login: LoginSchema = Body(...)):
    print('ok')
    login = jsonable_encoder(login)
    new_login = await add_login_data(login)
    return ResponseModelLogin(new_login, "Login added successfully.")