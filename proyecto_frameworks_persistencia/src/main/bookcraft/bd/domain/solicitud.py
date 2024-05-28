class Solicitud:
    def __init__(self,id,id_usuario,id_libro,tipo,fecha):
        self.__id = id
        self.__id_usuario = id_usuario
        self.__id_libro = id_libro
        self.__tipo = tipo
        self.__fecha = fecha

    def get_id(self):
        return self.__id
    
    def get_id_usuario(self):
        return self.__id_usuario
    
    def get_id_libro(self):
        return self.__id_libro
    
    def get_tipo(self):
        return self.__tipo
    
    def get_fecha(self):
        return self.__fecha
    
    def set_id_usuario(self,id_usuario):
        self.__id_usuario = id_usuario

    def set_id_libro(self,id_libro):
        self.__id_libro = id_libro
    
    def set_tipo(self,tipo):
        self.__tipo = tipo
    
    def set_fecha(self,fecha):
        self.__fecha = fecha
    
