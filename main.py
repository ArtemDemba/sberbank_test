from fastapi import Body
from fastapi import FastAPI

from src.routers.routers import process_router


app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@process_router.post(path='process_json/',
                     status_code=200)
async def process_json():
    pass


@process_router.post(path='process_xml/',
                     status_code=200)
async def process_xml():
    pass
