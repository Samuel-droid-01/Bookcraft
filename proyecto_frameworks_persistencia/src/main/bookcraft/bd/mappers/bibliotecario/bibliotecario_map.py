from ...domain.bibliotecario import Bibliotecario
from ...config.db_connector import DBConnector
from .bibliotecario_map_intf import BibliotecarioMapperInterface

class BibliotecarioMapper(BibliotecarioMapperInterface):
    def __init__(self):
        super().__init__()  # Call parent class constructor
        self.__connection = DBConnector().get_connection()
