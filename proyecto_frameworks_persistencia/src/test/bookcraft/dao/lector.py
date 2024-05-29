from ....main.bookcraft.dao.lector.lectorDAO import LectorDAO

test_lector = LectorDAO()

print(test_lector.iniciar_sesion("juan@ejemplo.com", "contrasena123"))
test_lector.solicitar_devolucion(1)