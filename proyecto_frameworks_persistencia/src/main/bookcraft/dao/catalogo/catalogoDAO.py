from ...dao.libro.libroDAO import LibroDAO

class CatalogoDAO:
    def __init__(self):
        self.__catalogo_libros = []
        aux = LibroDAO(id=0)
        lista_ids = aux.get_libros()
        for i in lista_ids:
            self.__catalogo_libros.append(LibroDAO(id=i))
    
    def get_catalogo(self):
        return self.__catalogo_libros

catalogoMain = CatalogoDAO()
catalogo_de_Libros = catalogoMain.get_catalogo()

for libro in catalogo_de_Libros:
    print(libro.get_libro().get_id(), " | ", libro.get_libro().get_titulo())