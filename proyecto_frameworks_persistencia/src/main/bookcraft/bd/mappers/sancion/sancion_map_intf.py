from abc import ABCMeta, abstractmethod
from ...domain.sancion import Sancion

class SancionMapperInterface(metaclass=ABCMeta):
    @abstractmethod
    def insert(self, Sancion):
        pass