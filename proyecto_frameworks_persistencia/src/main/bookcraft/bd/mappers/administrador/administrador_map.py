from ...domain.administrador import Administrador
from ...config.db_connector import DBConnector
from .administrador_map_intf import AdministradorMapperInterface

class AdministradorMapper(AdministradorMapperInterface):
    def __init__(self):
        super().__init__()  # Call parent class constructor
        self.__connection = DBConnector().get_connection()
