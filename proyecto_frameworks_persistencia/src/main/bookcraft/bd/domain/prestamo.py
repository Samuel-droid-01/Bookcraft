class Prestamo:
    def __init__(self, id, id_usuario, id_libro, fecha_prestamo, fecha_devolucion, id_sancion, activo):
        self.__id = id
        self.__id_usuario = id_usuario
        self.__id_libro = id_libro
        self.__fecha_prestamo = fecha_prestamo
        self.__fecha_devolucion = fecha_devolucion
        self.__id_sancion = id_sancion
        self.__activo = activo

    def get_id(self):
        return self.__id
    
    def get_id_usuario(self):
        return self.__id_usuario
    
    def get_id_libro(self):
        return self.__id_libro
    
    def get_fecha_prestamo(self):
        return self.__fecha_prestamo
    
    def get_fecha_devolucion(self):
        return self.__fecha_devolucion
    
    def get_id_sancion(self):
        return self.__id_sancion
    
    def get_activo(self):
        return self.__activo

    def set_id_usuario(self,id_usuario):
        self.__id_usuario = id_usuario

    def set_id_libro(self,id_libro):
        self.__id_libro = id_libro

    def set_fecha_prestamo(self,fecha_prestamo):
        self.__fecha_prestamo = fecha_prestamo

    def set_fecha_devolucion(self,fecha_devolucion):
        self.__fecha_devolucion = fecha_devolucion

    def set_id_sancion(self,id_sancion):
        self.__id_sancion = id_sancion
        
    def set_activo(self,activo):
        self.__activo = activo