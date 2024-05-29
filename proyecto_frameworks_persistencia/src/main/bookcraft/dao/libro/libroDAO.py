from ...bd.mappers.libro.libro_map import LibroMapper
from ...bd.domain.libro import Libro

class LibroDAO:
    def __init__(self, titulo = None, isbn = None, autor = None, editorial = None, fecha_publicacion = None, id_categoria = None, 
                edicion = None, numero_paginas = None, numero_copias = None, copias_disponibles = None, id = None):
        if id != None:
            mapper = LibroMapper()
            self.__libro = mapper.get_by_id(id)
        else:
            self.__libro = Libro(id, titulo, isbn, autor, editorial, fecha_publicacion, id_categoria, edicion, numero_paginas,
            numero_copias, copias_disponibles)
    
    def set_libro(self):
        mapper = LibroMapper()
        mapper.insert(self.__libro)

    def get_libro(self):
        return self.__libro.get_titulo()