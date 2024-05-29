from ....main.bookcraft.bd.domain.usuario import Usuario
from ....main.bookcraft.dao.administrador.administradorDAO import AdministradorDAO

test_administrador = AdministradorDAO("Juan", "Perez", "ejemplo@gmail.com", "contrasena123")

test_usuario = Usuario(
    13,
    "Juan23 Yael",
    "Perez",
    1,
    "juan@ejempl1o.com",
    "contrasena123"
)
#test_administrador.registrar_usuario(test_usuario.get_nombres(), test_usuario.get_apellidos(),1, test_usuario.get_correo(), test_usuario.get_contrasena())
#test_administrador.actualizar_usuario(test_usuario.get_id(), test_usuario.get_nombres(), test_usuario.get_apellidos(), 2, test_usuario.get_correo(), test_usuario.get_contrasena())
print(test_administrador.ver_usuario(test_usuario.get_id()))
print(test_administrador.eliminar_usuario(test_usuario.get_id(),"aceptar"))
#print(test_administrador.registrar_usuario(test_usuario.get_nombres(), test_usuario.get_apellidos(), test_usuario.get_correo(), test_usuario.get_contrasena()))
#print(test_administrador.eliminar_usuario(11,"aceptar"))
#print(test_administrador.listar_usuarios()  )
#print(test_administrador.listar_usuarios())
