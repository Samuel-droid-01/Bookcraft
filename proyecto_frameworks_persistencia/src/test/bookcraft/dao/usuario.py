from ....main.bookcraft.dao.usuario.usuarioDAO import UsuarioDAO
from ....main.bookcraft.bd.domain.usuario import Usuario

test_usuario = UsuarioDAO()
print(test_usuario.iniciar_sesion("juan@ejemplo.com","contrasena123"))

test_usuario.cerrar_sesion()
