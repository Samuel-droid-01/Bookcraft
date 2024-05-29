from ...bd.mappers.prestamo.prestamo_map import PrestamoMapper
from ...bd.domain.prestamo import Prestamo
from ...dao.sancion.sancionDAO import SancionDAO

class PrestamoDAO:
    def __init__(self, id_usuario = None, id_libro = None, fecha_prestamo = None, fecha_devolucion = None, id_sancion = None, activo = None, id=None):
        if id != None:
            mapper = PrestamoMapper()
            self.__prestamo = mapper.get_by_id(id)
        else:
            self.__prestamo = Prestamo(id, id_usuario, id_libro, fecha_prestamo, fecha_devolucion, id_sancion, activo)

    def set_prestamo(self):
        mapper = PrestamoMapper()
        mapper.insert(self.__prestamo)

    def get_prestamo(self):
        return str(self.__prestamo.get_id_usuario())+" : "+ str(self.__prestamo.get_id_libro())

    def sancionar(self, descripcion):
        mapper = PrestamoMapper()
        nuevaSancion = SancionDAO()
        id_sancion = nuevaSancion.crear_sancion(descripcion)
        self.__prestamo.set_id_sancion(id_sancion)
        mapper.update(self.__prestamo)