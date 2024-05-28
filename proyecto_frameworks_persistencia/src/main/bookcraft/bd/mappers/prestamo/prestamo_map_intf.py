from ...domain.prestamo import Prestamo
from abc import ABCMeta, abstractmethod
from typing import List
class PrestamoMapperInterface(metaclass=ABCMeta):
    @abstractmethod
    def insert(self, Prestamo):
        pass
    def delete(self, Prestamo):
        pass
    def update(self, Prestamo):
        pass
    def get_by_id(self, id)-> Prestamo:
        pass
    def get_all(self)-> List[Prestamo]:
        pass