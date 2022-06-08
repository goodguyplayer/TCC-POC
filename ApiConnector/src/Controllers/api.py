from turtle import st
from typing import Union

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

list_de_envios = list()

class SendApi(BaseModel):
    name: str
    price: float
    is_offer: Union[bool, None] = None

class ReceiveApi(BaseModel):
    name: str
    price: float
    is_offer: Union[bool, None] = None

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


@app.put("/items/{item_id}")
def update_item(item_id: int, item: SendApi):
    return {"item_price": item.price, "item_id": item_id}

@app.post("/postData/")
def post_data(user_id: float):
    print(user_id)
    list_de_envios.append(user_id)
    return {
        "Id":user_id,
    }