import unittest
from unittest.mock import patch, MagicMock
from ....main.bookcraft.dao.prestamo.prestamoDAO import PrestamoDAO
from ....main.bookcraft.bd.domain.usuario import Usuario
from ....main.bookcraft.bd.mappers.prestamo.prestamo_map import PrestamoMapper

class TestPrestamo(unittest.TestCase):
    def setUp(self):
        self.prestamo = PrestamoDAO()
    

    def test_set_prestamo(self):
        print("test_set_prestamo")
        mappers= PrestamoMapper()
        registro=mappers.get_all()
        tamaño=len(registro)
        prestamo = PrestamoDAO(0, 0, '2021-10-10', '2021-10-10', 0, 0)
        try:
            prestamo.set_prestamo()
            self.assertEqual(len(mappers.get_all()), tamaño+1)
        except Exception as e:
            self.fail(f"\tError al insertar el prestamo: {e}")
    def test_get_prestamo(self):
        print("test_get_prestamo")
        prestamo=PrestamoDAO(id=9)
        try:
            info_prestamo=prestamo.get_prestamo()
            print("\tprestamo{",info_prestamo,"}")
        except Exception as e:
            self.fail(f"\tError al obtener el prestamo: {e}")
    def test_sancionar(self):
        print("test_sancionar")
        prestamo=PrestamoDAO(id=9)
        try:
            prestamo.sancionar("Sancion por retraso")
        except Exception as e:
            self.fail(f"\tError al sancionar el prestamo: {e}")

if __name__ == '__main__':
    unittest.main()

