from fastapi.exceptions import HTTPException


class InvalidDateException(HTTPException):
    """
    Тип ошибки, который будет выкидываться, если формат даты не получится спарсить
    """