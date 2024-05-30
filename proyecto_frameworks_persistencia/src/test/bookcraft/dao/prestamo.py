import unittest
from unittest.mock import patch, MagicMock
from ....main.bookcraft.dao.prestamo.prestamoDAO import PrestamoMapper
from ....main.bookcraft.dao.prestamo.prestamoDAO import Prestamo
from ....main.bookcraft.dao.sancion.sancionDAO import SancionDAO
from ....main.bookcraft.dao.prestamo.prestamoDAO import PrestamoDAO

class TestPrestamoDAO(unittest.TestCase):
    @patch.object(PrestamoMapper, 'get_by_id')
    @patch.object(Prestamo, '__init__', return_value=None)
    def test_init_with_id(self, mock_prestamo, mock_get_by_id):
        mock_get_by_id.return_value = MagicMock()
        PrestamoDAO(id=1)
        mock_get_by_id.assert_called_once_with(1)

    @patch.object(PrestamoMapper, 'insert')
    @patch.object(Prestamo, '__init__', return_value=None)
    def test_set_prestamo(self, mock_prestamo, mock_insert):
        mock_prestamo_instance = mock_prestamo.return_value
        dao = PrestamoDAO()
        dao.set_prestamo()
        mock_insert.assert_called_once_with(mock_prestamo_instance)

    @patch.object(Prestamo, 'get_id_usuario', return_value=1)
    @patch.object(Prestamo, 'get_id_libro', return_value=2)
    def test_get_prestamo(self, mock_get_id_usuario, mock_get_id_libro):
        dao = PrestamoDAO(id_usuario=1, id_libro=2)
        result = dao.get_prestamo()
        self.assertEqual(result, '1 : 2')

    @patch.object(PrestamoMapper, 'update')
    @patch.object(Prestamo, 'set_id_sancion')
    @patch.object(SancionDAO, 'crear_sancion', return_value=1)
    def test_sancionar(self, mock_crear_sancion, mock_set_id_sancion, mock_update):
        mock_prestamo_instance = Prestamo(id_sancion=1)
        dao = PrestamoDAO()
        dao._PrestamoDAO__prestamo = mock_prestamo_instance
        dao.sancionar('descripcion')
        mock_crear_sancion.assert_called_once_with('descripcion')
        mock_set_id_sancion.assert_called_once_with(1)
        mock_update.assert_called_once_with(mock_prestamo_instance)

if __name__ == '__main__':
    unittest.main()