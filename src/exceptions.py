from fastapi import HTTPException
from fastapi import status


class InvalidDateException(Exception):
    pass


class UnsupportedContentType(HTTPException):
    DEFAULT_MESSAGE = 'Unsupported content type'
    STATUS_CODE = status.HTTP_422_UNPROCESSABLE_ENTITY

    def __init__(self, message: str | None = None, status_code: int | None = None):
        self.status_code = status_code or self.STATUS_CODE
        self.detail = message or self.DEFAULT_MESSAGE
