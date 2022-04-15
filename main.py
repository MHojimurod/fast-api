from typing import Optional
import uvicorn
from fastapi import FastAPI
from models import Database
db = Database("user.db")
app = FastAPI()

@app.get("/")
def read_root():
    return {"users":db.get_users()}


@app.post("/create_user")
def read_item(name:str,surname:str):
    print("aaaaaa")
    db.create_user(name,surname)
    return {"users":db.get_users()}


