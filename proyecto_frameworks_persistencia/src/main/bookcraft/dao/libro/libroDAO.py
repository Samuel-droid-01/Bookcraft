from ...bd.mappers.libro.libro_map import LibroMapper
from ...bd.domain.libro import Libro
from ...dao.copia.copiaDAO import CopiaDAO

class LibroDAO:
    def __init__(self, titulo = None, isbn = None, autor = None, editorial = None, fecha_publicacion = None, id_categoria = None, 
                edicion = None, numero_paginas = None, numero_copias = None, copias_disponibles = None, id = None):
        if id != None:
            if id != 0:
                mapper = LibroMapper()
                self.__libro = mapper.get_by_id(id)
            else:
                self.__libro = None
        else:
            self.__libro = Libro(id, titulo, isbn, autor, editorial, fecha_publicacion, id_categoria, edicion, numero_paginas,
            numero_copias, copias_disponibles)
    
    def set_libro(self):
        mapper = LibroMapper()
        mapper.insert(self.__libro)
    
    def get_libro(self):
        return self.__libro
        
    def get_libro_by_id(self, id):
        mapper = LibroMapper()
        self.__libro = mapper.get_by_id(id)
        return self.__libro

    def delete_libro(self):
        try:
            mapper = LibroMapper()
            mapper.delete(self.__libro.get_id())
            self.__libro = None
        except:
            print("El id no existe.")

    def update_libro(self):
        try:
            mapper = LibroMapper()
            mapper.update(self.__libro)
        except:
            print("El id no existe.")

    def get_libros(self):
        mapper = LibroMapper()
        lista_ids = mapper.get_all()
        return lista_ids
    
    def get_copias(self):
        copia_libro = CopiaDAO(self.get_libro().get_id(), self.get_libro().get_copias_disponibles())
        return copia_libro
    
    def filtrar_autor(self, autor):
        mapper = LibroMapper()
        lista_ids = mapper.get_by_author(autor)
        return lista_ids
    
    def filtrar_categoria(self, categoria):
        mapper = LibroMapper()
        lista_ids = mapper.get_by_category(categoria)
        return lista_ids
    
    def listar_libros(self):
        mapper = LibroMapper()
        return mapper.get_all_libros()

    def ver_libro(self,id: int):
        mapper = LibroMapper()
        return mapper.get_by_id(id)