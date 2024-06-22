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
        self.prestamo=[]
    def set_prestamo(self):
        mapper = PrestamoMapper()
        mapper.insert(self.__prestamo)

    def get_prestamo(self):
        if isinstance(self.__prestamo, Prestamo):
            return self.__prestamo
        else:
            print("No hay una instancia válida.")
            return None
    
    def delete_prestamo(self):
        mapper = PrestamoMapper()
        try:
            
            mapper.delete(self.__prestamo.get_id())
            self.__prestamo = None
        except:
            print("El id no existe.")

    def update_prestamo(self):
        try:
            mapper = PrestamoMapper()
            mapper.update(self.__prestamo)
        except:
            print("El id no existe.")

    def sancionar(self, descripcion):
        mapper = PrestamoMapper()
        nuevaSancion = SancionDAO()
        id_sancion = nuevaSancion.crear_sancion(descripcion)
        self.__prestamo.set_id_sancion(id_sancion)
        mapper.update(self.__prestamo)
    def obtener_id(self, id_usuario, id_libro):
        mapper = PrestamoMapper()
        self.__prestamo =mapper.get_by_user_and_book(id_usuario, id_libro)
        return mapper.get_by_user_and_book(id_usuario, id_libro)
        # print("prestamo=",self.__prestamo.get_id())
    def obtener_prestamos_usuario(self, id_usuario):
        mapper = PrestamoMapper()
        id=mapper.get_by_user(id_usuario)
        return id