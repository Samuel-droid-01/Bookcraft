from ....main.bookcraft.dao.bibliotecario.bibliotecarioDAO import BibliotecarioDAO

test_b = BibliotecarioDAO()

print(test_b.iniciar_sesion("juan@ejemplo.com", "contrasena123"))
test_b.recibir_solicitudes_reservacion()
s = test_b.get_solicitudes_reservacion()
for i in s:
    print("E: ", i.get_id(),i.get_id_usuario(),i.get_id_libro(),i.get_tipo(),i.get_fecha())