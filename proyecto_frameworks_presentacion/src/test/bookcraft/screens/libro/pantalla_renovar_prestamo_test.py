from tkinter import Tk
from proyecto_frameworks_persistencia.src.main.bookcraft.dao.libro.libroDAO import LibroDAO
from proyecto_frameworks_presentacion.src.main.bookcraft.screens.libro.pantalla_renovar_prestamo import PantallaRenovarPrestamo


def test_Pantalla_Prestar_Libro():
    raiz = Tk()
    aplicacion = PantallaRenovarPrestamo(raiz,id_usuario=1)
    raiz.mainloop()

if __name__ == '__main__':
    test_Pantalla_Prestar_Libro()