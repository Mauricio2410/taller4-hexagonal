from abc import ABC, abstractmethod

class UserRepository(ABC):
    @abstractmethod
    def save(self, user): pass
    @abstractmethod
    def get_all(self): pass
    @abstractmethod
    def get_by_id(self, user_id): pass
    @abstractmethod
    def update(self, user_id, user_data): pass
    @abstractmethod
    def delete(self, user_id): pass