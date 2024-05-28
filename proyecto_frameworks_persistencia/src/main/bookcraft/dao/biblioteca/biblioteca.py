class Biblioteca:
    def __init__(self):
        self.__nombre = "Bookcraft"
        self.__direccion = "Calle 123, Colonia 456"
        self.__telefono = "1234567890"
        self.__correo = "bookcraft@gmail.com"

    def get_nombre(self):
        return self.__nombre
    
    def get_direccion(self):
        return self.__direccion
    
    def get_telefono(self):
        return self.__telefono
    
    def get_correo(self):
        return self.__correo