class Reservacion:
    def __init__(self, id_reservacion, id_usuario, id_libro, fecha_reservacion):
        self.__id_reservacion = id_reservacion
        self.__id_usuario = id_usuario
        self.__id_libro = id_libro
        self.__fecha_reservacion = fecha_reservacion
    
    def get_id_reservacion(self):
        return self.__id_reservacion
    
    def get_id_usuario(self):
        return self.__id_usuario
    
    def get_id_libro(self):
        return self.__id_libro
    
    def get_fecha_reservacion(self):
        return self.__fecha_reservacion
    
    def set_id_usuario(self, id_usuario):
        self.__id_usuario = id_usuario

    def set_id_libro(self, id_libro):
        self.__id_libro = id_libro

    def set_fecha_reservacion(self, fecha_reservacion):
        self.__fecha_reservacion = fecha_reservacion
