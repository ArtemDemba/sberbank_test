import json

from fastapi import Body
from fastapi import FastAPI

from src.routers.routers import process_router
from src.services.json_services import JsonService

with open('examples/example.json') as file:
    example = file.read()
    parsed_tree = JsonService.parse_json(example)
    with open('examples/output.json', 'w') as output_file:
        json.dump(parsed_tree, output_file, indent=4, ensure_ascii=False)

# app = FastAPI()
#
#
# @app.get("/")
# async def root():
#     return {"message": "Hello World"}
#
#
# @process_router.post(path='process_json/',
#                      status_code=200)
# async def process_json():
#     pass
#
#
# @process_router.post(path='process_xml/',
#                      status_code=200)
# async def process_xml():
#     pass
