from ..domain.administrador import Administrador
from ..domain.libro import Libro
from ..mappers.administrador.administrador_map import AdministradorMapper
from ..mappers.libro.libro_map import LibroMapper

class Bibliotecario(Administrador):
    def __init__(self, id, nombres, apellidos, id_rol, correo, contrasena):
        super().__init__(id, nombres, apellidos, id_rol, correo, contrasena)
        self.usuario_mapper = AdministradorMapper()
        self.libro_mapper = LibroMapper()