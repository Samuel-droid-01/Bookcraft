from ...domain.usuario import Usuario
from ...config.db_connector import DBConnector
from .usuario_map_intf import UsuarioMapperInterface

class UsuarioMapper(UsuarioMapperInterface):
    def __init__(self):
        self.__connection = DBConnector().get_connection()

    def insert(self, usuario: Usuario):
        cursor = self.__connection.cursor()
        query = """
            INSERT INTO usuarios (
                nombres, apellidos, id_rol, correo, contrasena
            ) VALUES (%s, %s, %s, %s, %s)
        """

        try:
            cursor.execute(query, (
                usuario.get_nombres(),
                usuario.get_apellidos(),
                usuario.get_id_rol(),
                usuario.get_correo(),
                usuario.get_contrasena()
            ))
            self.__connection.commit()
            print("Usuario insertado correctamente.")
        except Exception as e:
            self.__connection.rollback()
            print(f"Error al insertar el usuario: {e}")
        finally:
            cursor.close()
            self.__connection.close()

    def get_by_id(self, id: int) -> Usuario:
        cursor = self.__connection.cursor()
        query = """
            SELECT * FROM usuarios WHERE id = %s
        """

        try:
            cursor.execute(query, (id,))
            result = cursor.fetchone()

            if result:
                usuario = Usuario(
                    result['id'],
                    result['nombres'],
                    result['apellidos'],
                    result['id_rol'],
                    result['correo'],
                    result['contrasena']
                )
                return usuario
            else:
                return None
        except Exception as e:
            print(f"Error al obtener el usuario por ID: {e}")
        finally:
            cursor.close()
            self.__connection.close()

    def update(self, usuario: Usuario):
        cursor = self.__connection.cursor()
        query = """
            UPDATE usuarios SET 
                nombres = %s,
                apellidos = %s,
                id_rol = %s,
                correo = %s,
                contrasena = %s
            WHERE id = %s
        """

        try:
            cursor.execute(query, (
                usuario.get_nombres(),
                usuario.get_apellidos(),
                usuario.get_id_rol(),
                usuario.get_correo(),
                usuario.get_contrasena(),
                usuario.get_id()
            ))
            self.__connection.commit()
            print("Usuario actualizado correctamente.")
        except Exception as e:
            self.__connection.rollback()
            print(f"Error al actualizar el usuario: {e}")
        finally:
            cursor.close()
            self.__connection.close()

    def delete(self, id: int):
        cursor = self.__connection.cursor()
        query = """
            DELETE FROM usuarios WHERE id = %s
        """

        try:
            cursor.execute(query, (id,))
            self.__connection.commit()
            print("Usuario eliminado correctamente.")
        except Exception as e:
            self.__connection.rollback()
            print(f"Error al eliminar el usuario: {e}")
        finally:
            cursor.close()
            self.__connection.close()
