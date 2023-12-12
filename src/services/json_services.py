import json

from src.parsers.json_parser import JsonHandler
from src.normalizers.date_normalizer import DateNormalizer


class JsonService:
    @classmethod
    def parse_json(cls, tree: str) -> dict:
        trees = cls.__split_trees(tree)
        parsed_tree = JsonHandler.merge_trees(trees=trees)
        DateNormalizer.normalize(parsed_tree)
        return parsed_tree

    @classmethod
    def __split_trees(cls, tree: str) -> list[dict]:
        """
        Метод принимает несколько деревьев в строковом формате и конвертирует их в список словарей
        """
        dicted_tree: dict = json.loads(tree)
        return [tree for tree in dicted_tree.values()]
