from ...domain.prestamo import Prestamo
from abc import ABCMeta, abstractmethod
from typing import List

class PrestamoMapperInterface(metaclass=ABCMeta):
    @abstractmethod
    def insert(self, prestamo: Prestamo):
        pass

    @abstractmethod
    def delete(self, id: int):
        pass

    @abstractmethod
    def update(self,prestamo: Prestamo):
        pass

    @abstractmethod
    def get_by_id(self, id: int)-> Prestamo:
        pass

    @abstractmethod
    def get_all(self)-> List[Prestamo]:
        pass