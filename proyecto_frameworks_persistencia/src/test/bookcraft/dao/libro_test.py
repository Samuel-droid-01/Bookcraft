import unittest
from unittest.mock import patch, MagicMock
from ....main.bookcraft.dao.libro.libroDAO import LibroDAO
from ....main.bookcraft.bd.domain.usuario import Usuario
from ....main.bookcraft.bd.mappers.libro.libro_map import LibroMapper

class TestLibro(unittest.TestCase):
    print("Test de Libro")
    def setUp(self):
        self.libro = LibroDAO()
    
    def test_set_libro(self):
       print("test_set_libro")
       mappers= LibroMapper()
       registro=mappers.get_all()
       tamaño=len(registro)
       libro = LibroDAO('pedro pedro', '978-84-206-5060-2','pedro', 'pepe', '2021-10-10',2,1,69,69,69)
       try:
           libro.set_libro()
           self.assertEqual(len(mappers.get_all()), tamaño+1)
       except Exception as e:
           self.fail(f"\tError al insertar el libro: {e}")

    def test_get_libro(self):
       print("test_get_libro")
       libro=LibroDAO(id=9)
       try:
           info_libro=libro.get_libro()
           print("libro{",info_libro,"}")
       except Exception as e:
           self.fail(f"\tError al obtener el libro: {e}")
    
    @unittest.skip("funcionando con un id existente")
    def test_delete_libro(self):
       print("test_delete_libro")
       libro=LibroDAO(id=12)
       try:
           libro.delete_libro()
           print("libro eliminado correctamente")
       except Exception as e:
           self.fail(f"\tError al eliminar el libro: {e}")
    @unittest.skip("funcionando con un id existente")
    def test_update_libro(self):
        print("test_update_libro")
        libro = LibroDAO(id=10)
        libro.get_libro().set_autor("pepe")
        try:
            libro.update_libro()
            print("libro actualizado correctamente")
        except Exception as e:
            self.fail(f"\tError al insertar el libro: {e}")
    def test_get_copias(self):
        libro=LibroDAO(id=1)
        
        copia=libro.get_copias()
        try:
            print(copia.get_estado())
        except Exception as e:
            self.fail("Error al obtener las copias:",e)
    def test_filtrar_autor(self):
        libro=LibroDAO()
        autor="mario bennedeti"
        try:
            libro.filtrar_autor(autor)
        except:
            self.fail(f"error al filtrar")
    
    def test_filtrar_categoria(self):
        libro=LibroDAO()
        category="fantasia"
        try:
            libro.filtrar_categoria(category)
        except:
            self.fail(f"error al filtrar con categoria")
