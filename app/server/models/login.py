from typing import Optional
from pydantic import BaseModel, Field
class LoginSchema(BaseModel):
    email: str = Field(...)
    senha: str = Field(...)
    class Config:
        schema_extra = {
            "example": {
                "email": "email@email.com",
                "senha": "minhasenha123",
            }
        }

class UpdateLoginModel(BaseModel):
    email: Optional[str]
    senha: Optional[str]
    class Config:
        schema_extra = {
            "example": {
                "email": "teste@email.com",
                "senha": "123456",
            }
        }

def ResponseModelLogin(data, message):
    return {
        "data": [data],
        "code": 200,
        "message": message,
    }

def ErrorResponseModelLogin(error, code, message):
    return {"error": error, "code": code, "message": message}