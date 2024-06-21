from ...domain.sancion import Sancion
from ...config.db_connector import DBConnector
from .sancion_map_intf import SancionMapperInterface
class SancionMapper(SancionMapperInterface):
    def __init__(self):
        self.__connection = DBConnector().get_connection()
        
    def insert(self, sancion: Sancion):
        cursor = self.__connection.cursor()
        query = """
            INSERT INTO sanciones (
                fecha_inicio, fecha_fin, descripcion
            ) VALUES (%s, %s, %s)
        """
        try:
            cursor.execute(query, (
                sancion.get_fecha_inicio(), 
                sancion.get_fecha_fin(), 
                sancion.get_descripcion(),
            ))
            self.__connection.commit()
            # Recupera el último id insertado
            ultimo_id = "SELECT LAST_INSERT_ID()"
            cursor.execute(ultimo_id)
            inserted_id = cursor.fetchone()[0]
            print("Sancion insertada correctamente.")
            return inserted_id
            
        except Exception as e:
            self.__connection.rollback()
            print(f"Error al insertar la sancion: {e}")
            return -1
        finally:
            cursor.close()
            

    def update(self, sancion: Sancion):
        cursor = self.__connection.cursor()
        query = """
            UPDATE sanciones SET 
                fecha_inicio = %s, fecha_fin = %s, descripcion = %s
            WHERE id = %s
        """
        try:
            cursor.execute(query, (
                sancion.get_fecha_inicio(), 
                sancion.get_fecha_fin(), 
                sancion.get_descripcion(),
                sancion.get_id()
            ))
            self.__connection.commit()
            print("Sancion actualizada correctamente.")
        except Exception as e:
            self.__connection.rollback()
            print(f"Error al actualizar la sancion: {e}")
        finally:
            cursor.close()
            
            
    def delete(self, fecha_fin: str, fecha_inicio: str):
        cursor = self.__connection.cursor()
        query = """
            DELETE FROM sanciones WHERE fecha_fin = %s AND fecha_inicio = %s
        """
        try:
            cursor.execute(query, (fecha_fin, fecha_inicio))
            self.__connection.commit()
            print("Sancion eliminada correctamente.")
        except Exception as e:
            self.__connection.rollback()
            print(f"Error al eliminar la sancion: {e}")
        finally:
            cursor.close()
            

    def get_by_id(self, id: int):#No recibe un objeto pero retorna uno de la clase Sancion
        cursor = self.__connection.cursor()
        query = """
            SELECT CONCAT(usuarios.nombres, ' ', usuarios.apellidos) AS nombre, sanciones.fecha_inicio, sanciones.fecha_fin, sanciones.descripcion 
            FROM prestamos JOIN sanciones ON prestamos.id_sancion = sanciones.id JOIN usuarios ON prestamos.id_usuario = usuarios.id
            WHERE sanciones.id = %s
        """
        try:
            cursor.execute(query, (id,))
            data = cursor.fetchone()
            if data:
                sancion = Sancion(*data)
                return sancion
        except Exception as e:
            print(f"Error al buscar la sancion: {e}")
        finally:
            cursor.close()
            

    def get_all(self):
        cursor = self.__connection.cursor()
        query = """
            SELECT CONCAT(usuarios.nombres, ' ', usuarios.apellidos) AS nombre, sanciones.fecha_inicio, sanciones.fecha_fin, sanciones.descripcion 
            FROM prestamos JOIN sanciones ON prestamos.id_sancion = sanciones.id JOIN usuarios ON prestamos.id_usuario = usuarios.id
        """
        try:
            cursor.execute(query)
            sanciones = cursor.fetchall()
            sanciones = [Sancion(*data) for data in sanciones]
            return sanciones
        except Exception as e:
            print(f"Error al buscar las sanciones: {e}")
        finally:
            cursor.close()
    
    def get_by_date(self, fecha: str):
        cursor = self.__connection.cursor()
        query = """
            SELECT CONCAT(usuarios.nombres, ' ', usuarios.apellidos) AS nombre, sanciones.fecha_inicio, sanciones.fecha_fin, sanciones.descripcion 
            FROM prestamos JOIN sanciones ON prestamos.id_sancion = sanciones.id JOIN usuarios ON prestamos.id_usuario = usuarios.id
            WHERE sanciones.fecha_inicio = %s OR sanciones.fecha_fin = %s
        """
        try:
            cursor.execute(query, (fecha, fecha))
            sanciones = cursor.fetchall()
            sanciones = [Sancion(*data) for data in sanciones]
            return sanciones
        except Exception as e:
            print(fecha)
            print(f"Error al buscar las sanciones: {e}")
        finally:
            cursor.close()

    def get_by_user(self, id_usuario: int):
        cursor = self.__connection.cursor()
        query = """
            SELECT CONCAT(usuarios.nombres, ' ', usuarios.apellidos) AS nombre, sanciones.fecha_inicio, sanciones.fecha_fin, sanciones.descripcion 
            FROM prestamos JOIN sanciones ON prestamos.id_sancion = sanciones.id JOIN usuarios ON prestamos.id_usuario = usuarios.id
            WHERE usuarios.id = %s LIMIT 1
        """
        try:
            cursor.execute(query, (id_usuario,))
            sancion = cursor.fetchone()
            print(sancion)
            sanciones = Sancion(*sancion)
            return sanciones
        except Exception as e:
            print(f"Error al buscar las sanciones: {e}")
        finally:
            cursor.close()