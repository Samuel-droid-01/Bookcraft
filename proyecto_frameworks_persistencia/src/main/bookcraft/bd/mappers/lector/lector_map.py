from ...domain.lector import Lector
from ...config.db_connector import DBConnector
from .lector_map_intf import LectorMapperInterface

class LectorMapper(LectorMapperInterface):
    def __init__(self):
        super().__init__()  # Call parent class constructor
        self.__connection = DBConnector().get_connection()
