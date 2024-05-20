from abc import ABCMeta, abstractmethod
from ..domain.libro import Libro
from ..config.db_connector import DBConnector

class LibroMapperInterface(metaclass=ABCMeta):
    @abstractmethod
    def insert(self, Libro):
        pass

class LibroMapper(LibroMapperInterface):
    def __init__(self):
        self.__connection = DBConnector().get_connection()

    def insert(self, Libro):
        cursor = self.__connection.cursor()
        query = """
            INSERT INTO libros (
                titulo, isbn, autor, editorial, fecha_publicacion, 
                id_categoria, edicion, numero_paginas, numero_copias, copias_disponibles
            ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
        
        try:
            cursor.execute(query, (
                Libro.get_titulo(), 
                Libro.get_isbn(), 
                Libro.get_autor(), 
                Libro.get_editorial(), 
                Libro.get_fecha_publicacion(), 
                Libro.get_id_categoria(), 
                Libro.get_edicion(), 
                Libro.get_numero_paginas(), 
                Libro.get_numero_copias(), 
                Libro.get_copias_disponibles()
            ))
            self.__connection.commit()
            print("Libro insertado correctamente.")
        except Exception as e:
            self.__connection.rollback()
            print(f"Error al insertar el libro: {e}")
        finally:
            cursor.close()
            self.__connection.close()
