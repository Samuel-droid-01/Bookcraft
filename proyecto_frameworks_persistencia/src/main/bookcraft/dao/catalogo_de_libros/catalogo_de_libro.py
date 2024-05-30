from ...dao.libro.libroDAO import LibroDAO

class Catalogo_de_libroDAO:
    def __init__(self):
        self.__aux = LibroDAO(id=0)
        self.__lista_Libros = self.__aux.get_libros()
        
   