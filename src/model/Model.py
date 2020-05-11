from abc import ABC, abstractmethod


class Model(ABC):
    @classmethod
    @abstractmethod
    def from_json(cls, json):
        pass
