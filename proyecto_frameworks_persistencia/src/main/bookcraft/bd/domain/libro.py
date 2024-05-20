class Libro:
    def __init__(
            self, id, titulo, isbn, autor, editorial, fecha_publicacion, 
            id_categoria, edicion, numero_paginas, numero_copias, copias_disponibles
        ):
        self.__id = id
        self.__titulo = titulo
        self.__isbn = isbn
        self.__autor = autor
        self.__editorial = editorial
        self.__fecha_publicacion = fecha_publicacion
        self.__id_categoria = id_categoria
        self.__edicion = edicion
        self.__numero_paginas = numero_paginas
        self.__numero_copias = numero_copias
        self.__copias_disponibles = copias_disponibles

    def get_id(self):
        return self.__id
    
    def get_titulo(self):
        return self.__titulo
    
    def get_isbn(self):
        return self.__isbn
    
    def get_autor(self):
        return self.__autor
    
    def get_editorial(self):
        return self.__editorial
    
    def get_fecha_publicacion(self):
        return self.__fecha_publicacion
    
    def get_id_categoria(self):
        return self.__id_categoria
    
    def get_edicion(self):
        return self.__edicion
    
    def get_numero_paginas(self):
        return self.__numero_paginas
    
    def get_numero_copias(self):
        return self.__numero_copias
    
    def get_copias_disponibles(self):
        return self.__copias_disponibles
    
    def set_titulo(self, titulo):
        self.__titulo = titulo

    def set_isbn(self, isbn):
        self.__isbn = isbn
    
    def set_autor(self, autor):
        self.__autor = autor

    def set_editorial(self, editorial):
        self.__editorial = editorial

    def set_fecha_publicacion(self, fecha_publicacion):
        self.__fecha_publicacion = fecha_publicacion

    def set_id_categoria(self, id_categoria):
        self.__id_categoria = id_categoria
    
    def set_edicion(self, edicion):
        self.__edicion = edicion
    
    def set_numero_paginas(self, numero_paginas):
        self.__numero_paginas = numero_paginas
    
    def set_numero_copias(self, numero_copias):
        self.__numero_copias = numero_copias
    
    def set_copias_disponibles(self, copias_disponibles):
        self.__copias_disponibles = copias_disponibles