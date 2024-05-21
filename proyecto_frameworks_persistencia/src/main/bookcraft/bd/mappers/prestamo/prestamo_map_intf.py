from ...domain.sancion import Sancion
from abc import ABCMeta, abstractmethod

class PrestamoMapper(metaclass=ABCMeta):
    @abstractmethod
    def insert(self, Prestamo):
        pass