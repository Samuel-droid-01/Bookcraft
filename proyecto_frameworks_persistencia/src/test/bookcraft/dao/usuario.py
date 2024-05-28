from ....main.bookcraft.dao.usuario.usuarioDAO import UsuarioDAO
from ....main.bookcraft.bd.domain.usuario import Usuario

test_usuario = UsuarioDAO()
test_usuario.iniciar_sesion("alan@gmail.com","xd")
test_usuario.cerrar_sesion()
