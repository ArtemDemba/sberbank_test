from fastapi import HTTPException
from fastapi import Request
from fastapi.openapi.models import HTTPBase
from starlette.middleware.base import BaseHTTPMiddleware, RequestResponseEndpoint

from src.services.json_service import JsonService
from src.services.xml_service import XMLService


class ContentTypeMiddleware(BaseHTTPMiddleware):
    async def dispatch(self,
                       request: Request,
                       call_next: RequestResponseEndpoint) -> HTTPBase:
        content_type = request.headers.get('Content-Type')
        if not content_type:
            raise HTTPException(status_code=400, detail='Missing Content-Type header')

        if 'json' in content_type:
            request.state.service = JsonService()
        elif 'xml' in content_type:
            request.state.service = XMLService()
        else:
            raise HTTPException(status_code=400, detail='Unsupported Content-Type')

        response = await call_next(request)
        return response
