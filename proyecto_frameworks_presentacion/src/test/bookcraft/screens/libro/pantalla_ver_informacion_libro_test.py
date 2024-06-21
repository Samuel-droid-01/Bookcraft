from tkinter import *
from proyecto_frameworks_presentacion.src.main.bookcraft.screens.libro.pantalla_ver_informacion_libro import InformacionLibro

if __name__ == '__main__':
    raiz = Tk()
    aplicacion = InformacionLibro(raiz)
    raiz.mainloop()
