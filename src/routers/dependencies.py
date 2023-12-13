from fastapi import Request

from src.services.json_service import JsonService
from src.services.xml_service import XMLService
from src.exceptions import InvalidContentType


class ContentTypeChecker:
    def __call__(self, request: Request):
        content_type = request.headers.get("Content-Type", "").lower()
        if content_type == 'application/json':
            return JsonService()
        elif content_type == 'application/xml':
            return XMLService()
        else:
            raise InvalidContentType('Недопустимый тип контента')
