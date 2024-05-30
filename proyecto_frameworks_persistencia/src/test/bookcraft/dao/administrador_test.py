import unittest
from unittest.mock import patch, MagicMock
from ....main.bookcraft.dao.administrador.administradorDAO import AdministradorDAO

class TestAbministrador(unittest.TestCase):
    def test_registrar_usuario(self):
        administrador=AdministradorDAO()
        try:
            administrador.registrar_usuario("pedro","pedro",1,"example","hola")
        except:
            self.fail(f"error al registrar")
    def test_actualizar_usuario(self):
        administrador=AdministradorDAO()
        try:
            administrador.actualizar_usuario(1,"pedro","pedro",1,"example","hola")
        except:
            self.fail(f"error al actualizar")
    def test_eliminar_usuario(self):
        administrador=AdministradorDAO()
        try:
            administrador.eliminar_usuario(1,"cancelar")
        except:
            self.fail(f"error al eliminar")
    def test_ver_usuarios(self):
        administrador=AdministradorDAO()
        try:
            administrador.ver_usuario(1)
        except:
            self.fail(f"error al ver usuario")
    def test_listar_usuario(self):
        administrador=AdministradorDAO()
        try:
            administrador.listar_usuarios()
        except:
            self.fail(f"error al listar")
