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
        fecha_inicio = datetime.now()
        fecha_fin = fecha_inicio + timedelta(days=3)

        fecha_inicio_modificada = fecha_inicio.strftime('%Y-%m-%d')
        fecha_fin_modificada = fecha_fin.strftime('%Y-%m-%d')
        
        self.__sancion = Sancion(fecha_inicio=fecha_inicio_modificada, fecha_fin=fecha_fin_modificada, descripcion=descripcion)
        id_sancion = self.set_sancion(self.__sancion)
        return id_sancion