from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder

from server.database import (
    retrieve_logs,
    add_logs_data,
    retrieve_log,
    update_logs,
    delete_log,
)
from server.models.logs import (
    ErrorResponseModelLogs,
    ResponseModelLogs,
    LogsSchema,
    UpdateLogsModel
)

routerLogs = APIRouter()

@routerLogs.post("/", response_description="logs data added into the database")
async def add_logs(logs: LogsSchema = Body(...)):
    print('ok')
    logs = jsonable_encoder(logs)
    #ia = postIA(logs)
    new_log = await add_logs_data(logs)
    return ResponseModelLogs(new_log, "Logs added successfully.")

@routerLogs.get("/", response_description="Logs retrieved")
async def get_logs():
    logs = await retrieve_logs()
    if logs:
        return ResponseModelLogs(logs, "Logs data retrieved successfully")
    return ResponseModelLogs(logs, "Empty list returned")

@routerLogs.get("/{id}", response_description="Logs data retrieved")
async def get_logs_data(id):
    logs = await retrieve_log(id)
    if logs:
        return ResponseModelLogs(logs, "Logs data retrieved successfully")
    return ErrorResponseModelLogs("An error occurred.", 404, "Logs doesn't exist.")

@routerLogs.put("/{id}")
async def update_logs_data(id: str, req: UpdateLogsModel = Body(...)):
    req = {k: v for k, v in req.dict().items() if v is not None}
    updated_logs = await update_logs(id, req)
    if updated_logs:
        return ResponseModelLogs(
            "Logs with ID: {} name update is successful".format(id),
            "Log name updated successfully",
        )
    return ErrorResponseModelLogs(
        "An error occurred",
        404,
        "There was an error updating the log data.",
    )

@routerLogs.delete("/{id}", response_description="Log data deleted from the database")
async def delete_logs_data(id: str):
    deleted_log = await delete_log(id)
    if deleted_log:
        return ResponseModelLogs(
            "Log with ID: {} removed".format(id), "Log deleted successfully"
        )
    return ErrorResponseModelLogs(
        "An error occurred", 404, "Log with id {0} doesn't exist".format(id)
    )