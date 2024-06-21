from proyecto_frameworks_persistencia.src.main.bookcraft.dao.usuario.usuarioDAO import UsuarioDAO
from proyecto_frameworks_persistencia.src.main.bookcraft.bd.mappers.usuario.usuario_map import UsuarioMapper
from proyecto_frameworks_persistencia.src.main.bookcraft.bd.domain.usuario import Usuario
from proyecto_frameworks_persistencia.src.main.bookcraft.bd.mappers.libro.libro_map import LibroMapper
from proyecto_frameworks_persistencia.src.main.bookcraft.bd.domain.libro import Libro
class AdministradorDAO(UsuarioDAO):
    def __init__(self):
        self.__rol = "Administrador"

    def get_rol(self):
        return self.__rol
    
    def set_rol(self, rol):
        self.__rol = rol

    def registrar_usuario(self, nombre:str, apellido:str, id_rol:int, email:str, contrasena:str):
        mapper = UsuarioMapper()
        usuario = Usuario(None, nombre, apellido, id_rol, email, contrasena)
        if mapper.validar_correo(email):
            mapper.insert(usuario)
            return True,"Usuario registrado"
        else:
            return False,"Correo repetido,intente con otro correo"
    
    def actualizar_usuario(self, id: int, nombres:str, apellidos:str, id_rol:int, correo:str, contrasena:str):
        mapper = UsuarioMapper()
        usuario = Usuario(id, nombres, apellidos, id_rol, correo, contrasena)
        mapper.update(usuario)
        return True,"Usuario actualizado"
    
    def ver_usuario(self,id: int):
        mapper = UsuarioMapper()
        return mapper.get_by_id(id)

    def listar_usuarios(self):
        mapper = UsuarioMapper()
        return mapper.get_all()
    
    def eliminar_usuario(self,id: int,opcion:str):
        mapper = UsuarioMapper()
        if opcion == "aceptar":
            mapper.delete(id)
            return True,"Usuario eliminado"
        elif opcion == "cancelar":
            return False,"Operacion cancelada"



    
