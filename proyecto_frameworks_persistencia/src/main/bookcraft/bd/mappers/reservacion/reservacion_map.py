from ...domain.reservacion import Reservacion
from .reservacion_map_intf import ReservacionMapper
from ...config.db_connector import DBConnector
from typing import List

class ReservacionMapper(ReservacionMapper):
    def __init__(self):
        self.__connection = DBConnector().get_connection()

    def insert(self, reservacion: Reservacion):
        cursor = self.__connection.cursor()
        query = """
            INSERT INTO reservaciones (
                id_libro, id_usuario, fecha_reservacion, fecha_devolucion
            ) VALUES (%s, %s, %s, %s)
        """
        
        try:
            cursor.execute(query, (
                reservacion.get_id_libro(), 
                reservacion.get_id_usuario(), 
                reservacion.get_fecha_reservacion(), 
                reservacion.get_fecha_devolucion()
            ))
            self.__connection.commit()
            print("Reservacion insertada correctamente.")
        except Exception as e:
            self.__connection.rollback()
            print(f"Error al insertar la reservacion: {e}")
        finally:
            cursor.close()

    def update(self, reservacion: Reservacion):
        cursor = self.__connection.cursor()
        query = """
            UPDATE reservaciones SET 
                id_libro = %s,
                id_usuario = %s,
                fecha_reservacion = %s,
                fecha_devolucion = %s
            WHERE id = %s
        """

        try:
            cursor.execute(query, (
                reservacion.get_id_libro(), 
                reservacion.get_id_usuario(), 
                reservacion.get_fecha_reservacion(), 
                reservacion.get_fecha_devolucion(), 
                reservacion.get_id()
            ))
            self.__connection.commit()
            print("Reservacion actualizada correctamente.")
        except Exception as e:
            self.__connection.rollback()
            print(f"Error al actualizar la reservacion: {e}")
        finally:
            cursor.close()

    def delete(self, id):
        cursor = self.__connection.cursor()
        query = "DELETE FROM reservaciones WHERE id = %s"

        try:
            cursor.execute(query, (id,))
            self.__connection.commit()
            print("Reservacion eliminada correctamente.")
        except Exception as e:
            self.__connection.rollback()
            print(f"Error al eliminar la reservacion: {e}")
        finally:
            cursor.close()

    def find_by_id(self, id) -> Reservacion:
        cursor = self.__connection.cursor()
        query = "SELECT * FROM reservaciones WHERE id = %s"

        try:
            cursor.execute(query, (id,))
            data = cursor.fetchone()
            return Reservacion(*data)
        except Exception as e:
            print(f"Error al obtener la reservacion: {e}")
        finally:
            cursor.close()
    
    def find_all(self) -> List[Reservacion]:
        cursor = self.__connection.cursor()
        query = "SELECT * FROM reservaciones"

        try:
            cursor.execute(query)
            reservaciones = cursor.fetchall()
            reservaciones = [Reservacion(*data) for data in reservaciones]
            return reservaciones
        except Exception as e:
            print(f"Error al obtener las reservaciones: {e}")
        finally:
            cursor.close()