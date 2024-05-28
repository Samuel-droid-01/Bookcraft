from abc import ABCMeta, abstractmethod
from ...domain.solicitud import Solicitud
from typing import List
class SolicitudMapperInterface(metaclass=ABCMeta):
    @abstractmethod
    def insert(self, solicitud: Solicitud):
        pass

    @abstractmethod
    def update(self, solicitud: Solicitud):
        pass

    @abstractmethod
    def delete(self, id: int):
        pass

    @abstractmethod
    def get_by_id(self, id: int)->Solicitud:
        pass

    @abstractmethod
    def get_all(self)->List[Solicitud]:
        pass