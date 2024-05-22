class Sancion:
    def __init__(self,fechaInicio,fechaFin,descripcion):
        self.__id = None#Dejarlo asi porq es autoincremental
        self.__fecha_inicio = fechaInicio
        self.__fecha_fin = fechaFin
        self.__descripcion = descripcion
    def get_id(self):
        return self.__id
    def get_fecha_inicio(self):
        return self.__fecha_inicio
    def get_fecha_fin(self):
        return self.__fecha_fin
    def get_descripcion(self):
        return self.__descripcion
    def set_fecha_inicio(self,fecha_inicio):
        self.__fecha_inicio = fecha_inicio
    def set_fecha_fin(self,fecha_fin):
        self.__fecha_fin = fecha_fin
    def set_descripcion(self,descripcion):
        self.__descripcion = descripcion
    
    