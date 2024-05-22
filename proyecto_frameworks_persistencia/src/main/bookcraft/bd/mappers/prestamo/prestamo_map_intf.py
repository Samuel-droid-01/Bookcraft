from ...domain.sancion import Sancion
from abc import ABCMeta, abstractmethod

class PrestamoMapper(metaclass=ABCMeta):
    @abstractmethod
    def insert(self, Prestamo):
        pass
    def delete(self, Prestamo):
        pass
    def update(self, Prestamo):
        pass
    def find_by_id(self, id):
        pass
    def find_all(self):
        pass