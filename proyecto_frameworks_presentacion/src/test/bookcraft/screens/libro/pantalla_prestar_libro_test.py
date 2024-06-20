from tkinter import Tk
from proyecto_frameworks_persistencia.src.main.bookcraft.dao.libro.libroDAO import LibroDAO
from proyecto_frameworks_presentacion.src.main.bookcraft.screens.libro.pantalla_prestar_libro import PantallaPrestarLibro


def test_Pantalla_Prestar_Libro():
    raiz = Tk()
    libro=LibroDAO()
    aplicacion = PantallaPrestarLibro(raiz,libro)
    raiz.mainloop()

if __name__ == '__main__':
    test_Pantalla_Prestar_Libro()