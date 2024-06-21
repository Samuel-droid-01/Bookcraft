from ...domain.solicitud import Solicitud
from ...config.db_connector import DBConnector
from .solicitud_map_intf import SolicitudMapperInterface

class SolicitudMapper(SolicitudMapperInterface):
    def __init__(self):
        self.__connection = DBConnector().get_connection()

    def insert(self, solicitud: Solicitud):
        cursor = self.__connection.cursor()
        query = """
            INSERT INTO solicitudes (
                id_usuario, id_libro, tipo, fecha
            ) VALUES (%s, %s, %s, %s)
        """

        try:
            cursor.execute(query, (
                solicitud.get_id_usuario(),
                solicitud.get_id_libro(),
                solicitud.get_tipo(),
                solicitud.get_fecha()
            ))
            self.__connection.commit()
            print("Solicitud insertada correctamente.")
        except Exception as e:
            self.__connection.rollback()
            print(f"Error al insertar la solicitud: {e}")
        finally:
            cursor.close()
    
    def update(self, solicitud: Solicitud):
        cursor = self.__connection.cursor()
        query = """
            UPDATE solicitudes
            SET id_usuario = %s, id_libro = %s, tipo = %s, fecha = %s
            WHERE id = %s
        """

        try:
            cursor.execute(query, (
                solicitud.get_id_usuario(),
                solicitud.get_id_libro(),
                solicitud.get_tipo(),
                solicitud.get_fecha(),
                solicitud.get_id()
            ))
            self.__connection.commit()
            print("Solicitud actualizada correctamente.")
        except Exception as e:
            self.__connection.rollback()
            print(f"Error al actualizar la solicitud: {e}")
        finally:
            cursor.close()

    def delete(self, id: int):
        cursor = self.__connection.cursor()
        query = """
            DELETE FROM solicitudes WHERE id = %s
        """

        try:
            cursor.execute(query, (id,))
            self.__connection.commit()
            print("Solicitud eliminada correctamente.")
        except Exception as e:
            self.__connection.rollback()
            print(f"Error al eliminar la solicitud: {e}")
        finally:
            cursor.close()

    def get_by_id(self, id: int):
        cursor = self.__connection.cursor()
        query = """
            SELECT * FROM solicitudes WHERE id = %s
        """
        try:
            cursor.execute(query, (id,))
            result = cursor.fetchone()
            if result:
                return Solicitud(*result)
            else:
                return None
        except Exception as e:
            print(f"Error al obtener la solicitud por ID: {e}")
        finally:
            cursor.close()
    
    def get_all(self):
        cursor = self.__connection.cursor()
        query = """
            SELECT * FROM solicitudes
        """
        try:
            cursor.execute(query)
            result = cursor.fetchall()
            return [Solicitud(*row) for row in result]
        except Exception as e:
            print(f"Error al obtener todas las solicitudes: {e}")
        finally:
            cursor.close()

    def select_by_tipo(self, category):
        cursor = self.__connection.cursor()
        query = """
            SELECT * FROM solicitudes WHERE tipo = %s
        """
        try:
            cursor.execute(query, (category,))
            result = cursor.fetchall()
            return [Solicitud(*row) for row in result]
        except Exception as e:
            print(f"Error al obtener todas las solicitudes por categoría: {e}")
        finally:
            cursor.close()
