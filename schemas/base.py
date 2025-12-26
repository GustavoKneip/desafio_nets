from abc import ABC, abstractmethod

class EventSchema(ABC):
    topic: str

    @abstractmethod
    def build(self, event: dict):
        """Return a list of (key, payload)"""
        pass
