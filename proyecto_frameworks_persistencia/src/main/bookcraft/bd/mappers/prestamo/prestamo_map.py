from ...domain.prestamo import Prestamo
from ...config.db_connector import DBConnector
from .prestamo_map_intf import PrestamoMapperInterface

class PrestamoMapper(PrestamoMapperInterface):
    def __init__(self):
        self.__connection = DBConnector().get_connection()

    def insert(self, Prestamo):
        cursor = self.__connection.cursor()
        query = """INSERT INTO prestamos (id_usuario, id_libro, fecha_prestamo, fecha_devolucion,id_sancion,activo) VALUES (%s, %s, %s, %s,%s,%s)
            """
        try:
            cursor.execute(query, (
                Prestamo.get_id_usuario(),
                Prestamo.get_id_libro(),
                Prestamo.get_fecha_prestamo(),
                Prestamo.get_fecha_devolucion(),
                Prestamo.get_id_sancion(),
                Prestamo.get_activo()
            ))
            self.__connection.commit()
            print("Prestamo insertado correctamente.")
        except Exception as e:
            self.__connection.rollback()
            print(f"Error al insertar el prestamo: {e}")
        finally:
            cursor.close()
            self.__connection.close()
        
    def update(self, Prestamo):
        cursor = self.__connection.cursor()
        query = """UPDATE prestamos SET id_usuario = %s, id_libro = %s, fecha_prestamo = %s, fecha_devolucion = %s, id_sancion = %s, activo = %s WHERE id = %s
            """
        try:
            cursor.execute(query, (
                Prestamo.get_id_usuario(),
                Prestamo.get_id_libro(),
                Prestamo.get_fecha_prestamo(),
                Prestamo.get_fecha_devolucion(),
                Prestamo.get_id_sancion(),
                Prestamo.get_activo(),
                Prestamo.get_id()
            ))
            self.__connection.commit()
            print("Prestamo actualizado correctamente.")
        except Exception as e:
            self.__connection.rollback()
            print(f"Error al actualizar el prestamo: {e}")
        finally:
            cursor.close()
            self.__connection.close()

    def delete(self, Prestamo):
        cursor = self.__connection.cursor()
        query = """DELETE FROM prestamos WHERE id = %s
            """
        try:
            cursor.execute(query, (Prestamo.get_id(),))
            self.__connection.commit()
            print("Prestamo eliminado correctamente.")
        except Exception as e:
            self.__connection.rollback()
            print(f"Error al eliminar el prestamo: {e}")
        finally:
            cursor.close()
            self.__connection.close()

    def find_all(self):
        cursor = self.__connection.cursor()
        query = """SELECT * FROM prestamos
            """
        try:
            cursor.execute(query)
            prestamos = cursor.fetchall()
            return [
                Prestamo(
                    prestamo[0],prestamo[1], prestamo[2], prestamo[3], prestamo[4], prestamo[5], prestamo[6]
                ) for prestamo in prestamos
            ]
        except Exception as e:
            print(f"Error al buscar los prestamos: {e}")
        finally:
            cursor.close()
            self.__connection.close()
    
    def find_by_id(self, id):#no recibe un objeto, sino un id,pero retorna un objeto de la clase Prestamo
        cursor = self.__connection.cursor()
        query = """SELECT * FROM prestamos WHERE id_reservacion = %s
            """
        try:
            cursor.execute(query, (id,))
            prestamo = cursor.fetchone()
            return Prestamo(
                prestamo[0],prestamo[1], prestamo[2], prestamo[3], prestamo[4], prestamo[5], prestamo[6]
            )
        except Exception as e:
            print(f"Error al buscar el prestamo: {e}")
        finally:
            cursor.close()
            self.__connection.close()
