from tkinter import *
from proyecto_frameworks_presentacion.src.main.bookcraft.screens.sancion.pantalla_listar_lectores_sancionados import PantallaListarLectoresSancionados

if __name__ == '__main__':
    raiz = Tk()
    aplicacion = PantallaListarLectoresSancionados(raiz)
    raiz.mainloop()
