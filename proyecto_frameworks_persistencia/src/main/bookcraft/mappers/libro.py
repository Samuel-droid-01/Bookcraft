from domain.libro.libro import Libro
from config.BD.keysData import Database

class InterfazLibro:
    def __init__(self):
        self.libro = Libro()

    def obtener_titulo(self):

        return self.libro.titulo

    def establecer_titulo(self, titulo):
        self.libro.titulo = titulo

    def obtener_autor(self):
        return self.libro.autor

    def establecer_autor(self, autor):
        self.libro.autor = autor

    # Agrega más métodos de interfaz según tus necesidades

# Ejemplo de uso
# interfaz_libro = InterfazLibro()
# titulo = interfaz_libro.obtener_titulo()
# print(titulo)