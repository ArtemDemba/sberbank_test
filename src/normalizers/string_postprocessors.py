from num2words import num2words


class StringProcessor:
    @staticmethod
    def convert_to_bool(stringed_bool: str) -> bool:
        """
        Эта функция принимает значение какого-то ключа (да/нет) и конвертирует его в True/False
        """
        return stringed_bool.lower() == 'да'
