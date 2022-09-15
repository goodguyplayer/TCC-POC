from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder

from server.database import (
    retrieve_logs,
    add_logs_data,
    retrieve_log,
    update_logs,
    delete_log,
    retrieve_logins,
    retrieve_login,
    add_login_data,
)
from server.models.logs import (
    ErrorResponseModel,
    ResponseModel,
    LogsSchema,
    UpdateLogsModel
)

from server.models.login import (
    LoginSchema
)

router = APIRouter()

@router.post("/", response_description="logs data added into the database")
async def add_logs(logs: LogsSchema = Body(...)):
    print('ok')
    logs = jsonable_encoder(logs)
    #ia = postIA(logs)
    new_log = await add_logs_data(logs)
    return ResponseModel(new_log, "Logs added successfully.")

@router.get("/", response_description="Logs retrieved")
async def get_logs():
    logs = await retrieve_logs()
    if logs:
        return ResponseModel(logs, "Logs data retrieved successfully")
    return ResponseModel(logs, "Empty list returned")

@router.get("/{id}", response_description="Logs data retrieved")
async def get_logs_data(id):
    logs = await retrieve_log(id)
    if logs:
        return ResponseModel(logs, "Logs data retrieved successfully")
    return ErrorResponseModel("An error occurred.", 404, "Logs doesn't exist.")

@router.put("/{id}")
async def update_logs_data(id: str, req: UpdateLogsModel = Body(...)):
    req = {k: v for k, v in req.dict().items() if v is not None}
    updated_logs = await update_logs(id, req)
    if updated_logs:
        return ResponseModel(
            "Logs with ID: {} name update is successful".format(id),
            "Log name updated successfully",
        )
    return ErrorResponseModel(
        "An error occurred",
        404,
        "There was an error updating the log data.",
    )

@router.delete("/{id}", response_description="Log data deleted from the database")
async def delete_logs_data(id: str):
    deleted_log = await delete_log(id)
    if deleted_log:
        return ResponseModel(
            "Log with ID: {} removed".format(id), "Log deleted successfully"
        )
    return ErrorResponseModel(
        "An error occurred", 404, "Log with id {0} doesn't exist".format(id)
    )

@router.get("/login", response_description="Login retrieved")
async def get_logs():
    login = await retrieve_logins()
    if login:
        return ResponseModel(login, "Login data retrieved successfully")
    return ResponseModel(login, "Empty list returned")


@router.get("/login/{id}", response_description="Login data retrieved")
async def get_logs_data(id):
    login = await retrieve_login(id)
    if login:
        return ResponseModel(login, "Login data retrieved successfully")
    return ErrorResponseModel("An error occurred.", 404, "Login doesn't exist.")

@router.post("/login", response_description="login data added into the database")
async def add_login(login: LoginSchema = Body(...)):
    print('ok')
    login = jsonable_encoder(login)
    new_login = await add_login_data(login)
    return ResponseModel(new_login, "Login added successfully.")