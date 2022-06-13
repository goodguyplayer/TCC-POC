from typing import Optional

from pydantic import BaseModel, Field

class LogsSchema(BaseModel):
    FlowID: str = Field(...)

    class Config:
        schema_extra = {
            "example": {
                "FlowID": "192.168.4.118-203.73.24.75-4504-80-6",
            }
        }

class UpdateLogsModel(BaseModel):
    FlowID: Optional[str]
    SrcIP: Optional[str]
    SrcPort: Optional[str]

    class Config:
        schema_extra = {
            "example": {
                "FlowID": "John Doe",
                "SrcIP": "jdoe@x.edu.ng",
                "SrcPort": "Water resources and environmental engineering",
            }
        }

def ResponseModel(data, message):
    return {
        "data": [data],
        "code": 200,
        "message": message,
    }

def ErrorResponseModel(error, code, message):
    return {"error": error, "code": code, "message": message}