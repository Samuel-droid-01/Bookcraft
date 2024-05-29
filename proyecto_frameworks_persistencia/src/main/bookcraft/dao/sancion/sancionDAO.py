from datetime import datetime, timedelta
from ...bd.domain.sancion import Sancion
from ...bd.mappers.sancion.sancion_map import SancionMapper

class SancionDAO:
    def __init__(self):
        self.__sancion = None

    def set_sancion(self, sancion):
        mapper = SancionMapper()
        id = mapper.insert(sancion)
        return id
        
    def get_sancion(self):
        return self.__sancion
    
    def crear_sancion(self, descripcion):
        fecha_inicio = datetime.now().date()
        fecha_fin = fecha_inicio + timedelta(days=3)
        self.__sancion = Sancion(fecha_inicio=fecha_inicio, fecha_fin=fecha_fin, descripcion=descripcion)
        id_sancion = self.set_sancion(self.__sancion)
        return id_sancion