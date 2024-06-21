from tkinter import *
from .....main.bookcraft.screens.libro.pantalla_eliminar_libro import EliminarLibro

def test_Pantalla_Eliminar_Libro():
    raiz = Tk()
    aplicacion = EliminarLibro(raiz)
    raiz.mainloop()

if __name__ == '__main__':
    test_Pantalla_Eliminar_Libro()