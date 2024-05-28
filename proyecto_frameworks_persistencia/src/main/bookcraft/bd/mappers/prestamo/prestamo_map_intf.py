from ...domain.prestamo import Prestamo
from abc import ABCMeta, abstractmethod
from typing import List

class PrestamoMapperInterface(metaclass=ABCMeta):
    @abstractmethod
    def insert(self, Prestamo):
        pass

    @abstractmethod
    def delete(self, Prestamo):
        pass

    @abstractmethod
    def update(self, Prestamo):
        pass

    @abstractmethod
    def get_by_id(self, id)-> Prestamo:
        pass

    @abstractmethod
    def get_all(self)-> List[Prestamo]:
        pass