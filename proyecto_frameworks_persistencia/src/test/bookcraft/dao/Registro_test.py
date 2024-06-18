import unittest
from unittest.mock import patch, MagicMock
from ....main.bookcraft.dao.registro.registroDAO import RegistroDAO

class Test_registro(unittest.TestCase):
    print("Test de Registro")
    def test_finalizar_prestamo(self):
        registro=RegistroDAO()
        id=1
        text="sansion"
        try:
            registro.finalizar_prestamo(id,text)
            print("Prestamo finalizado")
        except:
            self.fail(f"\tError al insetar")
    def test_extender_prestamo(self):
        registro=RegistroDAO()
        try:
            registro.extender_prestamo(1,1,"2024-02-03","2024-02-03")
            print("Prestamo extendido")
        except:
            self.fail(f"")
    def test_realizar_prestamo(self):
        registro=RegistroDAO()
        try:
            registro.realizar_prestamo(1,1,"2024-02-03","2024-02-03")
            print("Prestamo realizado")
        except:
            self.fail(f"error al realizar el prestamo")
    def test_reservar_prestamo(self):
        registro=RegistroDAO()
        try:
            registro.reservar_prestamo(1,1,"2024-02-03")
            print("Prestamo reservado")
        except:
            self.fail(f"error al reservar")

