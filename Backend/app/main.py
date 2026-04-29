from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from .database import init_db

app = FastAPI()

@app.on_event("startup")
def startup():
    print("The server is starting...")
    init_db()
    print("The server is started")

@app.get("/")
def home(request: Request):
    return {"status": "ok", "message": "Database initialized"}
