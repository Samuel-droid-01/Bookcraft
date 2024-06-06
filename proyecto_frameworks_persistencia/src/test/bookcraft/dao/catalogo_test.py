import unittest
from unittest.mock import patch, MagicMock
from ....main.bookcraft.dao.catalogo.catalogoDAO import CatalogoDAO

class TestCatalogo(unittest.TestCase):
    print("Test de Catalogo")
    def test_llenar_catalogo(self):
        catalogo=CatalogoDAO()
        try:
            catalogo.llenar_catalogo()
            print("catalogo lleno")
        except:
            self.fail(f"no se pudo llenar la lista de catalogo")
    def test_get_catalogo(self):
        catalogo=CatalogoDAO()
        try:
            catalogo.get_catalogo()
            print("catalogo obtenido")
        except:
            self.fail(f"no se pudo obtener el catalogo")
    def test_filtrar_busqueda(self):
        catalogo=CatalogoDAO()
        autor="mario"
        try:
            catalogo.filtrar_busqueda("mario","fantasia")
            print("busqueda filtrada")
        except:
            self.fail(f"error al filtrar")
    