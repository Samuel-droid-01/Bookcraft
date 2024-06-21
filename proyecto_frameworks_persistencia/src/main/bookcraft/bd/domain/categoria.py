class Categoria:
    def __init__(
            self, id, categoria
        ):
        self.__id = id
        self.__categoria = categoria

    def get_id(self):
        return self.__id
    
    def get_categoria(self):
        return self.__categoria
    
    def set_categoria(self, categoria):
        self.__categoria = categoria
