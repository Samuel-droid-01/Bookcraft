from abc import ABCMeta, abstractmethod
from ...domain.libro import Libro

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