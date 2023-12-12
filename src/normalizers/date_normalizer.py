import datetime

from dateparser import parse

from .interfaces import Normalizer
from src.exceptions import InvalidDateException


class DateNormalizer(Normalizer):
    @classmethod
    def normalize(cls, tree: dict) -> None:
        """
        Все шаги для нормализации дат в дереве
        """
        for key, value in tree.items():
            if 'дата' in key.lower():
                tree[key] = cls.__convert_string_to_date(stringed_date=value)

    @classmethod
    def __convert_string_to_date(cls, stringed_date: str) -> str:
        """
        Тут будет приниматься строка типа '10 ноября 2022 года' и конвертироваться в '10.11.2022'
        """
        date = parse(stringed_date, languages=['ru'])
        if date is None:
            raise InvalidDateException('Неверный формат даты')
        formatted_date = date.strftime('%d.%m.%Y')
        return formatted_date

    @staticmethod
    def __calculate_remained_term(deadline: datetime.date) -> str:
        """
        Тут будет приниматься объект даты и возвращаться оставшийся срок до дедлайна в виде строки в формате
        'год_месяц_неделя_день'
        """