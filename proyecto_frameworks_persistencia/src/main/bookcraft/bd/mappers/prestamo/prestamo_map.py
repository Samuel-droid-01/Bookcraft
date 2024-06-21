from ...domain.prestamo import Prestamo
from ...config.db_connector import DBConnector
from .prestamo_map_intf import PrestamoMapperInterface

class PrestamoMapper(PrestamoMapperInterface):
    def __init__(self):
        self.__connection = DBConnector().get_connection()

    def insert(self, prestamo:  Prestamo):
        cursor = self.__connection.cursor()
        query = """INSERT INTO prestamos (id_usuario, id_libro, fecha_prestamo, fecha_devolucion,id_sancion,activo) VALUES (%s, %s, %s, %s,%s,%s)
            """
        try:
            cursor.execute(query, (
                prestamo.get_id_usuario(),
                prestamo.get_id_libro(),
                prestamo.get_fecha_prestamo(),
                prestamo.get_fecha_devolucion(),
                prestamo.get_id_sancion(),
                prestamo.get_activo()
            ))
            self.__connection.commit()
            # Actualizar copias disponibles
            libroQuery = """UPDATE libros SET copias_disponibles = copias_disponibles - 1 WHERE id = %s
                """
            cursor.execute(libroQuery, (prestamo.get_id_libro(),))
            self.__connection.commit()

            print("Prestamo insertado correctamente.")
            return True,"Prestamo insertado correctamente."
        except Exception as e:
            self.__connection.rollback()
            print(f"Error al insertar el prestamo: {e}")
            return False,f"Error al insertar el prestamo: {e}"
        finally:
            cursor.close()
        
    def update(self, prestamo: Prestamo):
        cursor = self.__connection.cursor()
        query = """UPDATE prestamos SET id_usuario = %s, id_libro = %s, fecha_prestamo = %s, fecha_devolucion = %s, id_sancion = %s, activo = %s WHERE id = %s
            """
        try:
            cursor.execute(query, (
                prestamo.get_id_usuario(),
                prestamo.get_id_libro(),
                prestamo.get_fecha_prestamo(),
                prestamo.get_fecha_devolucion(),
                prestamo.get_id_sancion(),
                prestamo.get_activo(),
                prestamo.get_id()
            ))
            self.__connection.commit()
            print("Prestamo actualizado correctamente.")
        except Exception as e:
            self.__connection.rollback()
            print(f"Error al actualizar el prestamo: {e}")
        finally:
            cursor.close()


    def delete(self, id:int):
        cursor = self.__connection.cursor()
        query = """DELETE FROM prestamos WHERE id = %s
            """
        try:
            cursor.execute(query, (id,))
            self.__connection.commit()
            print("Prestamo eliminado correctamente.")
        except Exception as e:
            self.__connection.rollback()
            print(f"Error al eliminar el prestamo: {e}")
        finally:
            cursor.close()

    def get_all(self):
        cursor = self.__connection.cursor()
        query = """SELECT * FROM prestamos
            """
        try:
            cursor.execute(query)
            prestamos = cursor.fetchall()
            prestamos=[Prestamo(*data) for data in prestamos]
            return prestamos
        except Exception as e:
            print(f"Error al buscar los prestamos: {e}")
        finally:
            cursor.close()
    
    def get_by_id(self, id: int):
        cursor = self.__connection.cursor()
        query = """SELECT * FROM prestamos WHERE id = %s
            """
        try:
            cursor.execute(query, (id,))
            prestamo = cursor.fetchone()
            prestamo = Prestamo(*prestamo)
            return prestamo
        except Exception as e:
            print(f"Error al buscar el prestamo: {e}")
        finally:
            cursor.close()
    def get_by_user_and_book(self, id_usuario: int, id_libro: int):
        cursor = self.__connection.cursor()
        query = """SELECT prestamos.*
        FROM prestamos
        JOIN usuarios ON prestamos.id_usuario = usuarios.id
        JOIN libros ON prestamos.id_libro = libros.id
        WHERE prestamos.id_usuario = %s AND prestamos.id_libro = %s ;"""
        try:
            cursor.execute(query, (id_libro, id_usuario))
            prestamo = cursor.fetchone()
            prestamo = Prestamo(*prestamo)
            return prestamo
        except Exception as e:
            print(f"Error al buscar el prestamo: {e}")
        finally:
            cursor.close()
    def get_by_user(self, id_usuario: int):
        cursor = self.__connection.cursor()
        query = """SELECT prestamos.id,prestamos.id_libro,prestamos.fecha_devolucion
        FROM prestamos
        JOIN usuarios ON prestamos.id_usuario = usuarios.id
        JOIN libros ON prestamos.id_libro = libros.id
        WHERE prestamos.id_usuario = %s;"""
        try:
            cursor.execute(query, (id_usuario,))
            prestamos = cursor.fetchall()
            return prestamos
        except Exception as e:
            print(f"Error al buscar el prestamos: {e}")
        finally:
            cursor.close()
    