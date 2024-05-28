from abc import ABCMeta, abstractmethod
from ...domain.sancion import Sancion
from typing import List
class SancionMapperInterface(metaclass=ABCMeta):
    @abstractmethod
    def insert(self, sancion):
        pass

    def update(self, sancion):
        pass

    def delete(self, sancion):
        pass

    def get_by_id(self, id)-> Sancion:
        pass
    
    def get_all(self)-> List[Sancion]:
        pass