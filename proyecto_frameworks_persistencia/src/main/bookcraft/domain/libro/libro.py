class Libro:
    def __init__(self, titulo, autor, genero):
        self.titulo = titulo
        self.autor = autor
        self.genero = genero

    def obtener_titulo(self):
        return self.titulo

    def obtener_autor(self):
        return self.autor

    def obtener_genero(self):
        return self.genero

    def establecer_titulo(self, titulo):
        self.titulo = titulo

    def establecer_autor(self, autor):
        self.autor = autor

    def establecer_genero(self, genero):
        self.genero = genero