from .....main.bookcraft.screens.libro.pantalla_prestar_libro import PantallaPrestarLibro
from tkinter import Tk

def test_Pantalla_Eliminar_Libro():
    raiz = Tk()
    aplicacion = PantallaPrestarLibro(raiz)
    raiz.mainloop()

if __name__ == '__main__':
    test_Pantalla_Eliminar_Libro()