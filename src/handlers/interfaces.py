from abc import ABC, abstractmethod


class Handler(ABC):
    @classmethod
    @abstractmethod
    def merge_trees(cls, trees: list):
        pass
