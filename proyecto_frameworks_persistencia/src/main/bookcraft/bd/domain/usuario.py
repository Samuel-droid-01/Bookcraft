class Usuario:
    def __init__(self, id, nombres, apellidos, id_rol, correo, contrasena):
        self.__id = id
        self.__nombres = nombres
        self.__apellidos = apellidos
        self.__id_rol = id_rol
        self.__correo = correo
        self.__contrasena = contrasena

    def get_id(self):
        return self.__id

    def get_nombres(self):
        return self.__nombres

    def get_apellidos(self):
        return self.__apellidos

    def get_id_rol(self):
        return self.__id_rol

    def get_correo(self):
        return self.__correo

    def get_contrasena(self):
        return self.__contrasena

    def set_nombres(self, nombres):
        self.__nombres = nombres

    def set_apellidos(self, apellidos):
        self.__apellidos = apellidos

    def set_id_rol(self, id_rol):
        self.__id_rol = id_rol

    def set_correo(self, correo):
        self.__correo = correo

    def set_contrasena(self, contrasena):
        self.__contrasena = contrasena