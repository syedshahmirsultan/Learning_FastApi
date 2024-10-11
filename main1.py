from fastapi import FastAPI,Body,Header

app:FastAPI = FastAPI()


@app.get("/notifications/")
def greet(name:str)->dict:
    return {"message":f"Hi! {name}"}

# Expect 'who' parameter to be sent as a key-value pair in a JSON object
@app.post("/hello/")
def hello_Func(who:str = Body(embed=True)):
    return (f"Hello ! {who}")

# Extract the 'who' value from the request headers
@app.post("/hey/")
def greetings(who:str = Header()):
    return (f"Hey {who}")

