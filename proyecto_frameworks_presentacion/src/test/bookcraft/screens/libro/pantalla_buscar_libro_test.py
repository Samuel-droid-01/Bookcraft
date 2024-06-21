from .....main.bookcraft.screens.libro.pantalla_eliminar_libro import PantallaBuscarLibro
from tkinter import Tk

def test_Pantalla_Eliminar_Libro():
    raiz = Tk()
    aplicacion = PantallaBuscarLibro(raiz)
    raiz.mainloop()

if __name__ == '__main__':
    test_Pantalla_Eliminar_Libro()