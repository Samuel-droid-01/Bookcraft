from ...domain.sancion import Sancion
from ...config.db_connector import DBConnector
from .sancion_map_intf import SancionMapperInterface
class SancionMapper(SancionMapperInterface):
    def __init__(self):
        self.__connection = DBConnector().get_connection()
    def insert(self, Sancion):
        cursor = self.__connection.cursor()
        query = """
            INSERT INTO sanciones (
                fecha_inicio, fecha_fin, descripcion
            ) VALUES (%s, %s, %s)
        """
        try:
            cursor.execute(query, (
                Sancion.get_fechaInicio(), 
                Sancion.get_fechaFin(), 
                Sancion.get_descripcion()
            ))
            self.__connection.commit()
            print("Sancion insertada correctamente.")
        except Exception as e:
            self.__connection.rollback()
            print(f"Error al insertar la sancion: {e}")
        finally:
            cursor.close()
            self.__connection.close()