from ...domain.categoria import Categoria
from ...config.db_connector import DBConnector
from .categoria_map_intf import CategoriaMapperInterface

class CategoriaMapper(CategoriaMapperInterface):
    def __init__(self):
        self.__connection = DBConnector().get_connection()

    def insert(self, categoria: Categoria):
        cursor = self.__connection.cursor()
        query = """
            INSERT INTO usuarios (
                categoria
            ) VALUES (%s)
        """

        try:
            cursor.execute(query, (
                categoria.get_categoria()
            ))
            self.__connection.commit()
            print("Categoria insertada correctamente.")
        except Exception as e:
            self.__connection.rollback()
            print(f"Error al insertar la categoria: {e}")
        finally:
            cursor.close()
            self.__connection.close()

    def get_by_id(self, id: int) -> Categoria:
        cursor = self.__connection.cursor()
        query = """
            SELECT * FROM categorias WHERE id = %s
        """

        try:
            cursor.execute(query, (id,))
            result = cursor.fetchone()

            if result:
                categoria = Categoria(
                    result['id'],
                    result['categoria']
                )
                return categoria
            else:
                return None
        except Exception as e:
            print(f"Error al obtener la categoría por ID: {e}")
        finally:
            cursor.close()
            self.__connection.close()

    def update(self, categoria: Categoria):
        cursor = self.__connection.cursor()
        query = """
            UPDATE categorias SET 
                categoria = %s
            WHERE id = %s
        """

        try:
            cursor.execute(query, (
                categoria.get_categoria(),
                categoria.get_id()
            ))
            self.__connection.commit()
            print("Categoría actualizada correctamente.")
        except Exception as e:
            self.__connection.rollback()
            print(f"Error al actualizar la categoría: {e}")
        finally:
            cursor.close()
            self.__connection.close()

    def delete(self, id: int):
        cursor = self.__connection.cursor()
        query = """
            DELETE FROM categorias WHERE id = %s
        """

        try:
            cursor.execute(query, (id,))
            self.__connection.commit()
            print("Categoría eliminada correctamente.")
        except Exception as e:
            self.__connection.rollback()
            print(f"Error al eliminar la categoría: {e}")
        finally:
            cursor.close()
            self.__connection.close()

    def get_categoria(self,id:int):
        cursor = self.__connection.cursor()
        query = """
            SELECT categoria FROM categorias WHERE id = %s
        """
        try:
            cursor.execute(query,(id,))
            result = cursor.fetchone()
            if result:
                return result[0]
        except Exception as e:
            print(f"Error al obtener las categorías: {e}")
        finally:
            cursor.close()
            self.__connection.close()

    def get_categorias(self):
        cursor = self.__connection.cursor()
        query = """
            SELECT categoria FROM categorias
        """
        try:
            cursor.execute(query)
            result = cursor.fetchall()
            categorias = []
            for categoria in result:
                categorias.append(categoria[0])
            return categorias
        except Exception as e:
            print(f"Error al obtener las categorías: {e}")
        finally:
            cursor.close()
            self.__connection.close()