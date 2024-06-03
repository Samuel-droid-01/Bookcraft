from ...dao.libro.libroDAO import LibroDAO

class CatalogoDAO:
    def __init__(self):
        self.__catalogo_libros = []
        self.__aux = LibroDAO(id=0)
        self.llenar_catalogo()
    
    def llenar_catalogo(self):
        lista_ids = self.__aux.get_libros()
        for i in lista_ids:
            self.__catalogo_libros.append(LibroDAO(id=i))

    def get_catalogo(self):
        return self.__catalogo_libros
    
    def filtrar_busqueda(self, autor = None, categoria = None):
        lista_autor = []
        lista_categoria = []
        if autor != None:
            if isinstance(self.__aux.filtrar_autor(autor), list):
                lista_autor = self.__aux.filtrar_autor(autor)
        if categoria != None:
            if isinstance(self.__aux.filtrar_categoria(categoria), list):
                lista_categoria = self.__aux.filtrar_categoria(categoria)
        filtro_final = lista_autor + lista_categoria
        return filtro_final
