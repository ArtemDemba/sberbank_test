from fastapi import APIRouter, HTTPException

from src.services.json_services import JsonService


process_router = APIRouter(prefix='/v1')


@process_router.post('/v1/process_json/')
async def process_json(tree: dict):
    try:
        return await JsonService.parse_json(tree)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
