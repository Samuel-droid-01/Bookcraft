from .....main.bookcraft.screens.administrador.principal_admin import PrincipalAdmin
from tkinter import Tk

def test_Principal():
    raiz = Tk()
    aplicacion = PrincipalAdmin(raiz)
    assert aplicacion != None
    raiz.destroy()

if __name__ == '__main__':
    test_Principal()