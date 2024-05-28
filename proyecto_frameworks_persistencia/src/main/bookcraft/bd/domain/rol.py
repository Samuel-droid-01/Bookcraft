class Rol:
    def __init__(
            self, id, rol
        ):
        self.__id = id
        self.__rol = rol

    def get_id(self):
        return self.__id
    
    def get_rol(self):
        return self.__rol
    
    def set_rol(self, rol):
        self.__rol = rol
