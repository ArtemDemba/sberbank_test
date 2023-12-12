from fastapi.exceptions import HTTPException


class InvalidDateException(Exception):
    """
    Тип ошибки, который будет выкидываться, если формат даты не получится спарсить
    """