from .....main.bookcraft.screens.libro.pantalla_devolver_libro import DevolverLibro
from tkinter import Tk

def test_Pantalla_Eliminar_Libro():
    raiz = Tk()
    aplicacion = DevolverLibro(raiz,3)#se manda el id desde la principal
    raiz.mainloop()

if __name__ == '__main__':
    test_Pantalla_Eliminar_Libro()