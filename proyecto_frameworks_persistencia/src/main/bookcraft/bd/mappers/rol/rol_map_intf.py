from abc import ABCMeta, abstractmethod
from ...domain.rol import Rol

class RolMapperInterface(metaclass=ABCMeta):
    @abstractmethod
    def insert(self, rol: Rol):
        pass

    @abstractmethod
    def get_by_id(self, id: int) -> Rol:
        pass

    @abstractmethod
    def update(self, rol: Rol):
        pass

    @abstractmethod
    def delete(self, id: int):
        pass
