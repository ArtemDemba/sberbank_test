from abc import ABC, abstractmethod


class Normalizer(ABC):
    @classmethod
    @abstractmethod
    def normalize(cls, tree: dict) -> None:
        pass
