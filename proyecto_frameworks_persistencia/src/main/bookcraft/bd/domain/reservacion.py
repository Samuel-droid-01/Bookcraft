class Reservacion:
    def __init__(self, id_reservacion, id_usuario, id_libro, posicion):
        self.__id_reservacion = id_reservacion
        self.__id_usuario = id_usuario
        self.__id_libro = id_libro
        self.__posicion = posicion
    
    def get_id_reservacion(self):
        return self.__id_reservacion
    
    def get_id_usuario(self):
        return self.__id_usuario
    
    def get_id_libro(self):
        return self.__id_libro
    
    def get_posicion(self):
        return self.__posicion
    
    def set_id_usuario(self, id_usuario):
        self.__id_usuario = id_usuario

    def set_id_libro(self, id_libro):
        self.__id_libro = id_libro

    def set_posicion(self, posicion):
        self.__posicion = posicion
