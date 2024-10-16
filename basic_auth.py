from fastapi import FastAPI,Depends,HTTPException,status
from fastapi.security import OAuth2PasswordBearer,OAuth2PasswordRequestForm
from typing import Annotated
from pydantic import BaseModel

fake_db:dict = {
"alice":{
    "username" : "alice",
    "email" : "alice@gmail.com",
    "hashed_password" : "fakedhashedsecret2",
    "disabled": True
    },
"johndoe" : {
"username":"johndoe",
"email" :"johndoe@gmail.com",
"hashed_password":"fakedhashedsecret",
"disabled" : False
}
}

class Token(BaseModel):
    access_token:str
    token_type:str |None = "bearer"

class User(BaseModel):
    username:str
    email:str|None = None
    disabled: bool|None = None

class UserInDB(User):
    hashed_password:str
    

app : FastAPI = FastAPI(title="Learning Authentication")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

def fake_password_hashed(password:str):
    return "fakedhashed"+ password

def get_user(db,username:str):
    if username in db:
        user_dict = fake_db.get(username)
        return UserInDB(**user_dict)
    

def get_current_user(token: Annotated[str,Depends(oauth2_scheme)]):
    user = get_user(fake_db,token)
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Unauthorized Username")
    if user.disabled:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail="Inactive User")
    return user


@app.post("/token",response_model=Token)
def login(form_data: Annotated[OAuth2PasswordRequestForm,Depends()]):  
 user_dict = fake_db.get(form_data.username)
 user = UserInDB(**user_dict)
 if not user:
     raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="Username or password not exists in the DateBase")
     
 hashed_password = fake_password_hashed(form_data.password)
 if not hashed_password == user.hashed_password:
         raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Incorrect Password")
 
 return {"access_token" :form_data.username,"token_type":"bearer"}


@app.get("/users/me")
def read_data(current_user: Annotated[str,Depends(get_current_user)]):
    return current_user
    
     
     
    
    
     

    