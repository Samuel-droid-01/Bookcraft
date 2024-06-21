from ...domain.rol import Rol
from ...config.db_connector import DBConnector
from .rol_map_intf import RolMapperInterface

class RolMapper(RolMapperInterface):
    def __init__(self):
        self.__connection = DBConnector().get_connection()

    def insert(self, rol: Rol):
        cursor = self.__connection.cursor()
        query = """
            INSERT INTO roles (rol)
            VALUES (%s)
        """

        try:
            cursor.execute(query, (rol.get_rol(),))
            self.__connection.commit()
            print("Rol insertado correctamente.")
        except Exception as e:
            self.__connection.rollback()
            print(f"Error al insertar el rol: {e}")
        finally:
            cursor.close()
            self.__connection.close()

    def get_by_id(self, id: int) -> Rol:
        cursor = self.__connection.cursor()
        query = """
            SELECT * FROM roles WHERE id = %s
        """

        try:
            cursor.execute(query, (id,))
            result = cursor.fetchone()

            if result:
                rol = Rol(
                    result['id'],
                    result['rol']
                )
                return rol
            else:
                return None
        except Exception as e:
            print(f"Error al obtener el rol por ID: {e}")
        finally:
            cursor.close()
            self.__connection.close()

    def get_all(self):
        cursor = self.__connection.cursor()
        query = """
            SELECT * FROM roles
        """

        try:
            cursor.execute(query)
            result = cursor.fetchall()
            roles = []

            for row in result:
                rol = Rol(
                    row['id'],
                    row['rol']
                )
                roles.append(rol)

            return roles
        except Exception as e:
            print(f"Error al obtener todos los roles: {e}")
        finally:
            cursor.close()
            self.__connection.close()

    def update(self, rol: Rol):
        cursor = self.__connection.cursor()
        query = """
            UPDATE roles SET 
                rol = %s
            WHERE id = %s
        """

        try:
            cursor.execute(query, (
                rol.get_rol(),
                rol.get_id()
            ))
            self.__connection.commit()
            print("Rol actualizado correctamente.")
        except Exception as e:
            self.__connection.rollback()
            print(f"Error al actualizar el rol: {e}")
        finally:
            cursor.close()
            self.__connection.close()

    def delete(self, id: int):
        cursor = self.__connection.cursor()
        query = """
            DELETE FROM roles WHERE id = %s
        """

        try:
            cursor.execute(query, (id,))
            self.__connection.commit()
            print("Rol eliminado correctamente.")
        except Exception as e:
            self.__connection.rollback()
            print(f"Error al eliminar el rol: {e}")
        finally:
            cursor.close()
            self.__connection.close()
