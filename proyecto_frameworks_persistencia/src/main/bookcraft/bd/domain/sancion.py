class Sancion:
    def __init__(self, fecha_inicio, fecha_fin, descripcion,nombre=None):
        self.__nombre = nombre
        self.__fecha_inicio = fecha_inicio
        self.__fecha_fin = fecha_fin
        self.__descripcion = descripcion

    def get_nombre(self):    
        return self.__nombre
    
    def get_fecha_inicio(self):
        return self.__fecha_inicio
    
    def get_fecha_fin(self):
        return self.__fecha_fin
    
    def get_descripcion(self):
        return self.__descripcion
    
    def set_nombre(self,nombre):
        self.__nombre = nombre
        
    def set_fecha_inicio(self,fecha_inicio):
        self.__fecha_inicio = fecha_inicio

    def set_fecha_fin(self,fecha_fin):
        self.__fecha_fin = fecha_fin
        
    def set_descripcion(self,descripcion):
        self.__descripcion = descripcion