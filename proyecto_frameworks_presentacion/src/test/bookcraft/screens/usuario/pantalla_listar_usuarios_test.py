from tkinter import *
from proyecto_frameworks_presentacion.src.main.bookcraft.screens.usuario.pantalla_listar_usuario import ListarUsuario

if __name__ == '__main__':
    raiz = Tk()
    aplicacion = ListarUsuario(raiz)
    raiz.mainloop()
