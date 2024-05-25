from ..domain.usuario import Usuario
from ..domain.libro import Libro
from ..mappers.usuario.usuario_map import UsuarioMapper
from ..mappers.libro.libro_map import LibroMapper

class Lector(Usuario):
    def __init__(self, id, nombres, apellidos, id_rol, correo, contrasena):
        super().__init__(id, nombres, apellidos, id_rol, correo, contrasena)
        self.usuario_mapper = UsuarioMapper()
        self.libro_mapper = LibroMapper()