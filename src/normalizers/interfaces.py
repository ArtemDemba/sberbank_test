from abc import ABC, abstractmethod


class Normalizer(ABC):
    """
    Interface for tree normalization
    """
    @classmethod
    @abstractmethod
    def normalize(cls, tree: dict) -> None:
        pass
