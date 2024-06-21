from abc import ABCMeta, abstractmethod
from ...domain.categoria import Categoria

class CategoriaMapperInterface(metaclass=ABCMeta):
    @abstractmethod
    def insert(self, categoria: Categoria):
        pass

    @abstractmethod
    def get_by_id(self, id: int):
        pass

    @abstractmethod
    def update(self, categoria: Categoria):
        pass

    @abstractmethod
    def delete(self, id: int):
        pass
