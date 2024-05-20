import unittest
from ..main.bookcraft.bd.domain.libro import Libro 

class TestLibro(unittest.TestCase):

    def setUp(self):
        self.libro = Libro("Título inicial", "Autor inicial", "Género inicial")

    def test_establecer_y_obtener_titulo(self):
        self.libro.establecer_titulo("1984")
        self.assertEqual(self.libro.obtener_titulo(), "1984")

    def test_establecer_y_obtener_autor(self):
        self.libro.establecer_autor("George Orwell")
        self.assertEqual(self.libro.obtener_autor(), "George Orwell")

    def test_establecer_y_obtener_genero(self):
        self.libro.establecer_genero("Distopía")
        self.assertEqual(self.libro.obtener_genero(), "Distopía")

if __name__ == '__main__':
    unittest.main()