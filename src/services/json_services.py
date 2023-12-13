from src.handlers.json_handler import JsonHandler
from src.normalizers.date_normalizer import DateNormalizer


class JsonService:
    @classmethod
    async def parse_json(cls, tree: dict) -> dict:
        trees = await cls.__split_trees(tree)
        parsed_tree = await JsonHandler.merge_trees(trees=trees)
        await DateNormalizer.normalize(parsed_tree)
        return parsed_tree

    @classmethod
    async def __split_trees(cls, trees: dict) -> list[dict]:
        """
        Метод принимает несколько деревьев внутри словаря, разделяет их и
        возвращает список деревьев
        """
        return [tree for tree in trees.values()]
