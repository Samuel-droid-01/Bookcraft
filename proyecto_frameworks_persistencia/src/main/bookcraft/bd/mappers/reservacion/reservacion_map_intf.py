from ...domain.reservacion import Reservacion 
from abc import ABCMeta, abstractmethod
from typing import List

class ReservacionMapperInterface(metaclass=ABCMeta):
    @abstractmethod
    def insert(self, Prestamo):
        pass
    def delete(self, Prestamo):
        pass
    def update(self, Prestamo):
        pass
    def find_by_id(self, id) -> Reservacion:
        pass
    def find_all(self) -> List[Reservacion]:
        pass