from ...bd.mappers.usuario.usuario_map import UsuarioMapper
class UsuarioDAO:
    def __init__(self):
        self.__usuario = None

    def set_usuario(self, usuario):
        self.__usuario = usuario

    def get_usuario(self):
        return self.__usuario

    def iniciar_sesion(self, correo, contrasena):
        mapper = UsuarioMapper()
        aux = mapper.validar_credenciales(correo, contrasena)
        if aux:
            self.set_usuario(aux)
            return True, aux
        else:
            return False, "Error al iniciar sesion"
            
    def cerrar_sesion(self):
        self.set_usuario(None)
        return True, "Sesion cerrada"