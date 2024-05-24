from abc import ABCMeta, abstractmethod
from ...domain.libro import Libro
from typing import List

class LibroMapperInterface(metaclass=ABCMeta):
    @abstractmethod
    def insert(self, libro: Libro):
        pass

    @abstractmethod
    def update(self, libro: Libro):
        pass

    @abstractmethod
    def delete(self, id):
        pass

    @abstractmethod
    def get_by_id(self, id) -> Libro:
        pass

    @abstractmethod
    def get_all(self) -> List[Libro]:
        pass