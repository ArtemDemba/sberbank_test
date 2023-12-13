import xml.etree.ElementTree as ET

from .interfaces import Service
from src.normalizers.date_normalizer import DateNormalizer


class XMLService(Service):
    """
    Сервис для конвертации xml в словарь с последующей нормализацией словаря
    """

    @classmethod
    async def parse(cls, tree: str) -> dict:
        dicted_data = await cls.__convert_xml_to_dict(tree)
        await DateNormalizer.normalize(dicted_data)
        return dicted_data

    @classmethod
    async def __convert_xml_to_dict(cls, xml_data: str) -> dict:
        """
        Метод, который конвертирует XML в словарь
        """
        root = ET.fromstring(xml_data)
        result_dict = {}
        for element in root:
            if len(element) == 0:
                result_dict[element.tag] = element.text
            else:
                result_dict[element.tag] = {}
                for sub_element in element:
                    result_dict[element.tag][sub_element.tag] = sub_element.text
        return result_dict
