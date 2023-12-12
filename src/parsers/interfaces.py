from abc import ABC, abstractmethod


class Parser(ABC):
    @staticmethod
    @abstractmethod
    def merge_trees(trees: list):
        pass
