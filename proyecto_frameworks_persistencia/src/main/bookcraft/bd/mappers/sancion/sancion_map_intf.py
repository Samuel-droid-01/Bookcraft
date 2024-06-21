from ...domain.sancion import Sancion
from abc import ABCMeta, abstractmethod
from typing import List
class SancionMapperInterface(metaclass=ABCMeta):
    @abstractmethod
    def insert(self, sancion: Sancion):
        pass
    
    @abstractmethod
    def update(self, sancion: Sancion):
        pass
    
    @abstractmethod
    def delete(self, id: int):
        pass
    
    @abstractmethod
    def get_by_id(self, id: int)-> Sancion:
        pass
    
    @abstractmethod
    def get_all(self)-> List[Sancion]:
        pass