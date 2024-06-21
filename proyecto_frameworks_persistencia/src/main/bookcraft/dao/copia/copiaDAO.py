class CopiaDAO:
    def __init__(self, id_libro, copias):
        self.__id_libro = id_libro
        self.__estado = copias
    
    def get_id_libro(self):
        return self.__id_libro
    
    def get_estado(self):
        return self.__estado
