from ...domain.reservacion import Reservacion
from .reservacion_map_intf import ReservacionMapperInterface
from ...config.db_connector import DBConnector
from typing import List

class ReservacionMapper(ReservacionMapperInterface):
    def __init__(self):
        self.__connection = DBConnector().get_connection()

    def insert(self, reservacion: Reservacion):
        cursor = self.__connection.cursor()
        query = """
            INSERT INTO reservaciones (
                id_usuario,id_libro,fecha_reservacion
            ) VALUES (%s, %s, %s)
        """
        
        try:
            cursor.execute(query, (
                reservacion.get_id_libro(), 
                reservacion.get_id_usuario(), 
                reservacion.get_fecha_reservacion(), 
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
                id_usuario = %s, 
                id_libro = %s, 
                fecha_reservacion = %s 
            WHERE id_reservacion = %s
        """
        try:
            cursor.execute(query, (
                reservacion.get_id_usuario(), 
                reservacion.get_id_libro(),
                reservacion.get_fecha_reservacion(), 
                reservacion.get_id_reservacion()
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
        query = "DELETE FROM reservaciones WHERE id_reservacion = %s"

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
        query = "SELECT * FROM reservaciones WHERE id_reservacion = %s"

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

    def getnombreUsuario(self, id_reservacion):
        cursor = self.__connection.cursor()
        query = "SELECT nombres FROM reservaciones join usuarios on reservaciones.id_usuario = usuarios.id where id_reservacion = %s"
        try:
            cursor.execute(query, (id_reservacion,))
            data = cursor.fetchone()
            return data[0]
        except Exception as e:
            print(f"Error al obtener el nombre del usuario: {e}")
        finally:
            cursor.close()

    def getnombreLibro(self, id_reservacion):
        cursor = self.__connection.cursor()
        query = "SELECT titulo FROM reservaciones join libros on reservaciones.id_libro = libros.id where id_reservacion = %s"
        try:
            cursor.execute(query, (id_reservacion,))
            data = cursor.fetchone()
            return data[0]
        except Exception as e:
            print(f"Error al obtener el nombre del libro: {e}")
        finally:
            cursor.close()