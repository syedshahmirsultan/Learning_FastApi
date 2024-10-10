from fastapi import FastAPI

# Making connection with Fast API
app: FastAPI = FastAPI()

@app.get("/")
def index()->dict:
    return {"message": "Welcome to FastAPI !"}