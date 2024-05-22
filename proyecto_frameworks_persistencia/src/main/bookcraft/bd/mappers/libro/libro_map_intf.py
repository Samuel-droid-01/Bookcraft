from abc import ABCMeta, abstractmethod
from ...domain.libro import Libro

class LibroMapperInterface(metaclass=ABCMeta):
    @abstractmethod
    def insert(self, Libro):
        pass

    @abstractmethod
    def update(self, Libro):
        pass