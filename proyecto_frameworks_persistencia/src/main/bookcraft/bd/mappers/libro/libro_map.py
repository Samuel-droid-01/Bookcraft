from typing import List
from ...domain.libro import Libro
from ...config.db_connector import DBConnector
from .libro_map_intf import LibroMapperInterface

class LibroMapper(LibroMapperInterface):
    def __init__(self):
        self.__connection = DBConnector().get_connection()

    def insert(self, libro: Libro):
        cursor = self.__connection.cursor()
        query = """
            INSERT INTO libros (
                titulo, isbn, autor, editorial, fecha_publicacion, 
                id_categoria, edicion, numero_paginas, numero_copias, copias_disponibles
            ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
        
        try:
            cursor.execute(query, (
                libro.get_titulo(), 
                libro.get_isbn(), 
                libro.get_autor(), 
                libro.get_editorial(), 
                libro.get_fecha_publicacion(), 
                libro.get_id_categoria(), 
                libro.get_edicion(), 
                libro.get_numero_paginas(), 
                libro.get_numero_copias(), 
                libro.get_copias_disponibles()
            ))
            self.__connection.commit()
            print("Libro insertado correctamente.")
        except Exception as e:
            self.__connection.rollback()
            print(f"Error al insertar el libro: {e}")
        finally:
            cursor.close()

    def update(self, libro: Libro):
        cursor = self.__connection.cursor()
        query = """
            UPDATE libros SET 
                titulo = %s,
                isbn = %s,
                autor = %s,
                editorial = %s,
                fecha_publicacion = %s,
                id_categoria = %s,
                edicion = %s,
                numero_paginas = %s,
                numero_copias = %s,
                copias_disponibles = %s
            WHERE id = %s
        """

        try:
            cursor.execute(query, (
                libro.get_titulo(), 
                libro.get_isbn(), 
                libro.get_autor(), 
                libro.get_editorial(), 
                libro.get_fecha_publicacion(), 
                libro.get_id_categoria(), 
                libro.get_edicion(), 
                libro.get_numero_paginas(), 
                libro.get_numero_copias(), 
                libro.get_copias_disponibles(),
                libro.get_id()
            ))
            self.__connection.commit()
            print("Libro actualizado correctamente.")
        except Exception as e:
            self.__connection.rollback()
            print(f"Error al actualizar el libro: {e}")
        finally:
            cursor.close()

    def delete(self, id):
        cursor = self.__connection.cursor()
        query = """
            DELETE FROM libros WHERE id = %s
        """

        try:
            cursor.execute(query, (id, ))
            self.__connection.commit()
            print("Libro eliminado correctamente")
        except Exception as e:
            self.__connection.rollback()
            print(f"Error al eliminar el libro: {e}")
        finally:
            cursor.close()

    def get_by_id(self, id):
        cursor = self.__connection.cursor()
        query = """
            SELECT * FROM libros WHERE id = %s
        """

        try:
            cursor.execute(query, (id, ))
            libro = cursor.fetchone()
            libro = Libro(*libro)
            return libro
        except Exception as e:
            print(f"Error al obtener el libro: {e}")
        finally:
            cursor.close()

    def get_all(self):
        cursor = self.__connection.cursor()
        query = """
            SELECT * FROM libros
        """

        try:
            cursor.execute(query)
            libros = cursor.fetchall()
            libros = [Libro(*data) for data in libros]
            return libros
        except Exception as e:
            print(f"Error al obtener los libros: {e}")
        finally:
            cursor.close()

    def get_by_title(self, title) -> List[Libro]:
        cursor = self.__connection.cursor()
        query = """
            SELECT * FROM libros WHERE titulo LIKE %s
        """

        try:
            cursor.execute(query, ('%' + title + '%', ))
            libros = cursor.fetchall()
            if libros:
                libros = [Libro(*data) for data in libros]
                return libros
            else:
                print("No se encontraron libros con ese título.")
        except Exception as e:
            print(f"Error al obtener los libros: {e}")
        finally:
            cursor.close()

    def get_by_author(self, author) -> List[Libro]:
        cursor = self.__connection.cursor()
        query = """
            SELECT * FROM libros WHERE autor LIKE %s
        """

        try:
            cursor.execute(query, ('%' + author + '%', ))
            libros = cursor.fetchall()
            if libros:
                libros = [Libro(*data) for data in libros]
                return libros
            else:
                print("No se encontraron libros con ese autor.")
        except Exception as e:
            print(f"Error al obtener los libros: {e}")
        finally:
            cursor.close()

    def get_by_category(self, category) -> List[Libro]:
        cursor = self.__connection.cursor()
        query = """
            SELECT libros.id, libros.titulo, libros.isbn, libros.autor, libros.editorial, 
            libros.fecha_publicacion, libros.id_categoria, libros.edicion, libros.numero_paginas, 
            libros.numero_copias, libros.copias_disponibles
            FROM libros 
            JOIN categorias ON libros.id_categoria = categorias.id
            WHERE categoria = %s
        """

        try:
            cursor.execute(query, (category, ))
            libros = cursor.fetchall()
            if libros:
                libros = [Libro(*data) for data in libros]
                return libros
            else:
                print("No se encontraron libros en esa categoría.")
        except Exception as e:
            print(f"Error al obtener los libros: {e}")
        finally:
            cursor.close()