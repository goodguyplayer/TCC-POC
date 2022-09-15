from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder

from server.database import (
    retrieve_logins,
    retrieve_login,
    add_login_data,
    update_logins,
    delete_login
)

from server.models.login import (
    ErrorResponseModelLogin,
    ResponseModelLogin,
    LoginSchema,
    UpdateLoginModel
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

@routerLogin.put("/{id}")
async def update_login_data(id: str, req: UpdateLoginModel = Body(...)):
    req = {k: v for k, v in req.dict().items() if v is not None}
    updated_logs = await update_logins(id, req)
    if updated_logs:
        return ResponseModelLogin(
            "Logs with ID: {} name update is successful".format(id),
            "Log name updated successfully",
        )
    return ErrorResponseModelLogin(
        "An error occurred",
        404,
        "There was an error updating the log data.",
    )

@routerLogin.delete("/{id}", response_description="Log data deleted from the database")
async def delete_login_data(id: str):
    deleted_log = await delete_login(id)
    if deleted_log:
        return ResponseModelLogin(
            "Log with ID: {} removed".format(id), "Log deleted successfully"
        )
    return ErrorResponseModelLogin(
        "An error occurred", 404, "Log with id {0} doesn't exist".format(id)
    )