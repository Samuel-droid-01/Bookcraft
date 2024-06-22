from tkinter import Tk

from proyecto_frameworks_presentacion.src.main.bookcraft.screens.libro.pantalla_reservar_libro import PantallaReservarLibro


def test_Pantalla_Prestar_Libro():
    raiz = Tk()
    aplicacion = PantallaReservarLibro(raiz,id_usuario=5)
    raiz.mainloop()

if __name__ == '__main__':
    test_Pantalla_Prestar_Libro()