class prestamo:
    def __init__(self,idPrestamo,idLibro,idUsuario,fechaInicio,fechaFin,activo):
        self.__idPrestamo = idPrestamo
        self.__idLibro = idLibro
        self.__idUsuario = idUsuario
        self.__fechaInicio = fechaInicio
        self.__fechaFin = fechaFin
        self.__activo = activo
        
    def get_idPrestamo(self):
        return self.__idPrestamo
    def get_idLibro(self):
        return self.__idLibro
    def get_idUsuario(self):
        return self.__idUsuario
    def get_FechaInicio(self):
        return self.__FechaInicio
    def get_FechaFin(self):
        return self.__FechaFin
    def get_activo(self):
        return self.__activo
    def set_idPrestamo(self,idPrestamo):
        self.__idPrestamo = idPrestamo
    def set_idLibro(self,idLibro):
        self.__idLibro = idLibro
    def set_idUsuario(self,idUsuario):
        self.__idUsuario = idUsuario
    def set_FechaInicio(self,fechaInicio):
        self.__FechaInicio = fechaInicio
    def set_FechaFin(self,fechaFin):
        self.__FechaFin = fechaFin
    def set_activo(self,activo):
        self.__activo = activo
    def sancionar():
        pass
    