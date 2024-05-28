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
    