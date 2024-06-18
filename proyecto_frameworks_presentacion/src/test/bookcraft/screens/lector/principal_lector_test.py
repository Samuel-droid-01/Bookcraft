from .....main.bookcraft.screens.lector.principal_lector import PrincipalLector
from tkinter import Tk

def test_Principal_Lector():
    raiz = Tk()
    aplicacion = PrincipalLector(raiz)
    raiz.mainloop()

if __name__ == '__main__':
    test_Principal_Lector()