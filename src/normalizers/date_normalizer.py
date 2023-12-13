from dateparser import parse
from ru_word2number.w2n import word_to_num

from .interfaces import Normalizer
from src.exceptions import InvalidDateException


class DateNormalizer(Normalizer):
    @classmethod
    async def normalize(cls, tree: dict) -> None:
        """
        Нормализация дат и сроков в дереве
        """
        for key, value in tree.items():
            if isinstance(value, dict):
                await cls.normalize(value)
            if 'дата' in key.lower():
                tree[key] = cls.__convert_string_to_date(stringed_date=value)
            if 'срок' in key.lower():
                tree[key] = cls.__calculate_remained_term(deadline=value)

    @classmethod
    async def __convert_string_to_date(cls, stringed_date: str) -> str:
        """
        Метод, конвертирующий даты из разных форматов в формат 'dd.mm.yyyy'
        """
        date = parse(stringed_date, languages=['ru'])
        if date is None:
            raise InvalidDateException('Неверный формат даты')
        formatted_date = date.strftime('%d.%m.%Y')
        return formatted_date

    @classmethod
    async def __calculate_remained_term(cls, deadline: str) -> str:
        """
        Метод считает, сколько лет, месяцев, недель и дней остаётся до истечения срока
        оплаты и представляет эту информацию в виде строки в формате
        'год_месяц_неделя_день'
        """
        left = 0
        term_dict = {
            'years': 0,
            'months': 0,
            'weeks': 0,
            'days': 0
        }
        splitted_deadline = deadline.split()
        if 'полгода' in splitted_deadline:
            term_dict['months'] += 6
        if 'полтора года' in deadline:
            term_dict['years'] += 1
            term_dict['months'] += 6
        if 'полтора месяца' in deadline:
            term_dict['months'] += 1
            term_dict['weeks'] += 2

        for indx, word in enumerate(splitted_deadline):
            possible_number = splitted_deadline[indx - 1]
            if (
                    'лет' in word.lower() or
                    'год' in word.lower()
            ):
                if possible_number == 'полтора':
                    continue
                number = await cls.__get_number(possible_number=possible_number,
                                                word_range=splitted_deadline[left:indx + 1])
                term_dict['years'] += number
                left = indx
            elif 'месяц' in word.lower():
                if possible_number == 'полтора':
                    continue
                number = await cls.__get_number(possible_number=possible_number,
                                                word_range=splitted_deadline[left:indx + 1])
                term_dict['months'] += number
                left = indx
            elif (
                    'недели' in word.lower() or
                    'недель' in word.lower() or
                    'неделя' in word.lower()
            ):
                number = await cls.__get_number(possible_number=possible_number,
                                                word_range=splitted_deadline[left:indx + 1])
                term_dict['weeks'] += number
                left = indx
            elif (
                    'день' in word.lower() or
                    'дней' in word.lower() or
                    'дня' in word.lower()
            ):
                number = await cls.__get_number(possible_number=possible_number,
                                                word_range=splitted_deadline[left:indx + 1])
                term_dict['days'] += number
                left = indx

        print(term_dict)
        return '_'.join(map(str, term_dict.values()))

    @classmethod
    async def __convert_word_to_number(cls, splitted_deadline: list[str]) -> int | None:
        start = 0
        was_the_number = False
        for indx, word in enumerate(splitted_deadline):
            try:
                word_to_num(word)
            except ValueError:
                if not was_the_number:
                    continue
                return word_to_num(' '.join(splitted_deadline[start:indx + 1]))
            else:
                if not was_the_number:
                    start = indx
                    was_the_number = True

    @classmethod
    async def __get_number(cls,
                           possible_number: str,
                           word_range: list[str]) -> int:
        """
        Метод получает часть строки и конвертирует её в целое число
        """
        try:
            number = int(possible_number)
        except ValueError:
            if possible_number == 'одна':
                # Так как фукция word_to_num() не конвертирует 'одна' в 1
                return 1
            number = await cls.__convert_word_to_number(splitted_deadline=word_range)
        return number
