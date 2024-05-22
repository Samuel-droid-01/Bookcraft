from ...domain.sancion import Sancion
from ...config.db_connector import DBConnector
from .sancion_map_intf import SancionMapperInterface
class SancionMapper(SancionMapperInterface):
    def __init__(self):
        self.__connection = DBConnector().get_connection()
    def insert(self, sancion):
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
                sancion.get_descripcion()
            ))
            self.__connection.commit()
            print("Sancion insertada correctamente.")
        except Exception as e:
            self.__connection.rollback()
            print(f"Error al insertar la sancion: {e}")
        finally:
            cursor.close()
            self.__connection.close()

    def update(self, sancion):
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
            self.__connection.close()
            
    def delete(self, sancion):
        cursor = self.__connection.cursor()
        query = """
            DELETE FROM sanciones WHERE id = %s
        """
        try:
            cursor.execute(query, (sancion.get_id(),))
            self.__connection.commit()
            print("Sancion eliminada correctamente.")
        except Exception as e:
            self.__connection.rollback()
            print(f"Error al eliminar la sancion: {e}")
        finally:
            cursor.close()
            self.__connection.close()

    def find_by_id(self, id):#No recibe un objeto pero retorna uno de la clase Sancion
        cursor = self.__connection.cursor()
        query = """
            SELECT * FROM sanciones WHERE id = %s
        """
        try:
            cursor.execute(query, (id,))
            sancion = cursor.fetchone()
            return Sancion(
                sancion[0],sancion[1], sancion[2], sancion[3]
            )
        except Exception as e:
            print(f"Error al buscar la sancion: {e}")
        finally:
            cursor.close()
            self.__connection.close()

    def find_all(self):
        cursor = self.__connection.cursor()
        query = """
            SELECT * FROM sanciones
        """
        try:
            cursor.execute(query)
            sanciones = cursor.fetchall()
            return [Sancion(
               sancion[0], sancion[1], sancion[2], sancion[3]
            ) for sancion in sanciones]
        except Exception as e:
            print(f"Error al buscar las sanciones: {e}")
        finally:
            cursor.close()
            self.__connection.close()