from abc import ABC, abstractmethod


class Service(ABC):
    @classmethod
    @abstractmethod
    async def parse(cls, data: str | dict) -> dict:
        pass
