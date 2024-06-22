from tkinter import *
from proyecto_frameworks_presentacion.src.main.bookcraft.screens.usuario.pantalla_historial_usuario import HistorialUsuario

if __name__ == '__main__':
    raiz = Tk()
    aplicacion = HistorialUsuario(raiz,id_usuario=1)
    raiz.mainloop()
