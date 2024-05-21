class Sancion:
    def __init__(self,fechaInicio,fechaFin,descripcion):
        self.__fechaInicio = fechaInicio
        self.__fechaFin = fechaFin
        self.__descripcion = descripcion
    def get_fechaInicio(self):
        return self.__fechaInicio
    def get_fechaFin(self):
        return self.__fechaFin
    def get_descripcion(self):
        return self.__descripcion
    def set_fechaInicio(self,fechaInicio):
        self.__fechaInicio = fechaInicio
    def set_fechaFin(self,fechaFin):
        self.__fechaFin = fechaFin
    def set_descripcion(self,descripcion):
        self.__descripcion = descripcion
    