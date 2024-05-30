from ...bd.domain.copia import Copia
from ...dao.libro.libroDAO import LibroDAO

class CopiaDAO:
    def __init__(self, id_libro, estado):
        self.__id_libro = id_libro
        self.__estado = estado
        self.__copiaLibro = LibroDAO(id_libro)
        self.__copia = Copia(id_libro, estado)
        
    def get_estado(self):
        return self.__estado
    
    def set_estado(self, estado):
        self.__estado = estado
    