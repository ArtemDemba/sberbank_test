from src.handlers.handler import Handler
from src.normalizers.date_normalizer import DateNormalizer
from .interfaces import Service


class JsonService(Service):
    @classmethod
    async def parse(cls, tree: dict) -> dict:
        trees = Handler.split_tree(tree)
        parsed_tree = Handler.merge_trees(trees=trees)
        DateNormalizer.normalize(parsed_tree)
        return parsed_tree
