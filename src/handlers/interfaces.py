from abc import ABC, abstractmethod


class IHandler(ABC):
    @classmethod
    @abstractmethod
    def merge_trees(cls, trees: list[dict]) -> dict:
        pass

    @staticmethod
    @abstractmethod
    async def split_tree(tree: dict) -> list[dict]:
        pass
