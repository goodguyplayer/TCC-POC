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