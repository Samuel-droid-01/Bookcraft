from tkinter import *
from proyecto_frameworks_presentacion.src.main.bookcraft.screens.libro.pantalla_listar_libro import ListarLibro

if __name__ == '__main__':
    raiz = Tk()
    aplicacion = ListarLibro(raiz)
    raiz.mainloop()
