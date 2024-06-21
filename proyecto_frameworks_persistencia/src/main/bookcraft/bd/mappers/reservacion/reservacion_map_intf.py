from ...domain.reservacion import Reservacion 
from abc import ABCMeta, abstractmethod
from typing import List

class ReservacionMapperInterface(metaclass=ABCMeta):
    @abstractmethod
    def insert(self, reservacion : Reservacion):
        pass

    @abstractmethod
    def delete(self, reservacion : Reservacion):
        pass

    @abstractmethod
    def update(self, reservacion : Reservacion):
        pass

    @abstractmethod
    def get_by_id(self, id : int) -> Reservacion:
        pass

    @abstractmethod
    def get_all(self) -> List[Reservacion]:
        pass

    @abstractmethod
    def get_nombre_usuario(self, id_reservacion : int):
        pass

    @abstractmethod
    def get_nombre_libro(self, id_reservacion : int):
        pass