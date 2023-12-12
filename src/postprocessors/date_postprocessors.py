import datetime


class DateProcessor:
    @staticmethod
    def convert_string_to_date(stringed_date: str) -> datetime.date:
        """
        Тут будет приниматься строка типа '10 ноября 2022' и конвертироваться в '10.11.2022'
        """

    @staticmethod
    def calculate_remained_term(deadline: datetime.date) -> str:
        """
        Тут будет приниматься объект даты и возвращаться оставшийся срок до дедлайна в виде строки в формате
        'год_месяц_неделя_день'
        """