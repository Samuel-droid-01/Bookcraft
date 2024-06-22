from tkinter import *
from proyecto_frameworks_presentacion.src.main.bookcraft.screens.sancion.pantalla_sancionar_lector import SacionarLector

if __name__ == '__main__':
    raiz = Tk()
    aplicacion = SacionarLector(raiz,id_libro=1,id_usuario=1)
    raiz.mainloop()
