from fastapi import FastAPI,Depends
from fastapi.security import OAuth2PasswordBearer
from typing import Annotated
from pydantic import BaseModel


app:FastAPI = FastAPI()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


class User(BaseModel):
    username:str
    email: str | None = None
    fullname : str | None = None
    disabled: bool | None = None


def fake_decode_token(token):
    return User(username= token + "fakedecoded", email="fakedecoded@gmai.com", fullnme="John Doe")

def get_current_user(token:Annotated[dict,Depends(oauth2_scheme)]):
    user = fake_decode_token(token)
    return user


@app.get("/users/me")
def get_user(current_user:Annotated[dict,Depends(get_current_user)]):
    return current_user