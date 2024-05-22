from abc import ABCMeta, abstractmethod
from ...domain.sancion import Sancion

class SancionMapperInterface(metaclass=ABCMeta):
    @abstractmethod
    def insert(self, sancion):
        pass
    def update(self, sancion):
        pass
    def delete(self, sancion):
        pass
    def find_by_id(self, id):
        pass
    def find_all(self):
        pass