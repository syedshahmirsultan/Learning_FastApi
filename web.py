from fastapi import FastAPI
from model import Creature
app:FastAPI = FastAPI()

@app.get("/creatures/")
def get_all()->list[Creature]:
    from data import get_creatures
    return get_creatures()