from typing import Union

from fastapi import FastAPI
from app.core.model import run_model

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/llm_chat")
def read_item(query:str):
    result = run_model(query)
    return {"result": result}