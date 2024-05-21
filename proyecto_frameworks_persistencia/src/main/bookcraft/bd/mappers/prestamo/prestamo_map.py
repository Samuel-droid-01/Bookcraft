from ...domain.prestamo import Prestamo
from ...config.db_connector import DBConnector
from .prestamo_map_intf import PrestamoMapperInterface

class PrestamoMapper(PrestamoMapperInterface):
    def __init__(self):
        self.__connection = DBConnector().get_connection()

    def insert(self, Prestamo):
        cursor = self.__connection.cursor()
        query = """
            INSERT INTO prestamos (
                id_libro, id_usuario, fecha_prestamo, fecha_devolucion
            ) VALUES (%s, %s, %s, %s)
        """
        
        try:
            cursor.execute(query, (
                Prestamo.get_id_libro(), 
                Prestamo.get_id_usuario(), 
                Prestamo.get_fecha_prestamo(), 
                Prestamo.get_fecha_devolucion()
            ))
            self.__connection.commit()
            print("Prestamo insertado correctamente.")
        except Exception as e:
            self.__connection.rollback()
            print(f"Error al insertar el prestamo: {e}")
        finally:
            cursor.close()
            self.__connection.close()