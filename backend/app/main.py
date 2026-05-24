from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from .database import init_db
from .routes import products

app = FastAPI()

@app.on_event("startup")
def startup():
    init_db()

app.include_router(products.router, prefix="/api")
app.mount("/static", StaticFiles(directory="../frontend/static"), name="static")
@app.get("/")
async def home(request: Request):
    return FileResponce("../../frontend/index.html")
