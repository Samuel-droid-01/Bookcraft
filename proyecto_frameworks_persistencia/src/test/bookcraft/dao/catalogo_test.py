import unittest
from unittest.mock import patch, MagicMock
from ....main.bookcraft.dao.catalogo.catalogoDAO import CatalogoDAO

class TestCatalogo(unittest.TestCase):
    def test_llenar_catalogo(self):
        catalogo=CatalogoDAO()
        try:
            catalogo.llenar_catalogo()
        except:
            self.fail(f"no se pudo llenar la lista de catalogo")
    def test_get_catalogo(self):
        catalogo=CatalogoDAO()
        try:
            catalogo.get_catalogo()
        except:
            self.fail(f"no se pudo obtener el catalogo")
    def test_filtrar_busqueda(self):
        catalogo=CatalogoDAO()
        autor="mario"
        try:
            catalogo.filtrar_busqueda("mario","fantasia")
        except:
            self.fail(f"error al filtrar")
    