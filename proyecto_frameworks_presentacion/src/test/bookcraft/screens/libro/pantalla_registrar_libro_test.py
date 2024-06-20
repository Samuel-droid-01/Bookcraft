from tkinter import *
from proyecto_frameworks_presentacion.src.main.bookcraft.screens.libro.pantalla_registrar_libro import RegistrarLibro

if __name__ == '__main__':
    raiz = Tk()
    aplicacion = RegistrarLibro(raiz)
    raiz.mainloop()
