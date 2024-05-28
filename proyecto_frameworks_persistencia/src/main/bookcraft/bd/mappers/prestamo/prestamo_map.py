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
            print("Prestamo insertado correctamente.")
        except Exception as e:
            self.__connection.rollback()
            print(f"Error al insertar el prestamo: {e}")
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
           