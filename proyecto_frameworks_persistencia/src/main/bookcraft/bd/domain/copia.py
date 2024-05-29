class Copia:
    def __init__(self, id_libro, estado):
        self.__id_libro = id_libro
        self.__estado = estado
    
    def get_id_libro(self):
        return self.__id_libro
    
    def get_estado(self):
        return self.__estado
    
    def set_id_libro(self,id_libro):
        self.__id_libro = id_libro

    def set_estado(self,estado):
        self.__estado = estado