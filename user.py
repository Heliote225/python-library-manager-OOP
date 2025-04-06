from abc import ABC, abstractmethod

class User(ABC):
    def __init__(self, name: str, user_id: int):
        self.name = name
        self.user_id = user_id

    @abstractmethod
    def get_user_type(self) -> str:
        pass

    def __str__(self):
        return f"{self.get_user_type()} - {self.name} (ID: {self.user_id})"