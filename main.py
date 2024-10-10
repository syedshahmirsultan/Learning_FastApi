from fastapi import FastAPI
from typing import Any

app1: FastAPI = FastAPI()


@app1.get("/hi")
def hi()->str:
    return ("Hi!")


@app1.get("/hi/{name}")
def main(name:str)->str:
    return (f"Hi! {name}")


@app1.get("/{id}")
def get_id(id:int)->Any:
    return (f"Your id is {id}")
    
# You can do this as well in Fast API    
@app1.get("/{id}/{name}")
def get_info(id:int,name:str)->Any:
    return (f"Your Id is {id} and your name is {name}")
    