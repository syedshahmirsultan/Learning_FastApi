from fastapi import FastAPI,Depends
from typing import Annotated
from fastapi.security import OAuth2PasswordBearer,OAuth2PasswordRequestForm


app:FastAPI = FastAPI()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


@app.get("/item")
def read_item(token: Annotated[str,Depends(oauth2_scheme)])->dict:
    return {"token":token}

@app.post("/aaaaa")
def login(form_data: Annotated[OAuth2PasswordRequestForm, Depends()]):
    return {
    "access_token":form_data.username, "token_type":"bearer"
    }