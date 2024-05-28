from abc import ABCMeta, abstractmethod
from ...domain.sancion import Sancion
from typing import List
class SancionMapperInterface(metaclass=ABCMeta):
    @abstractmethod
    def insert(self, sancion:Sancion):
        pass

    def update(self, sancion:Sancion):
        pass

    def delete(self, id:int):
        pass

    def get_by_id(self, id)-> Sancion:
        pass
    
    def get_all(self)-> List[Sancion]:
        pass