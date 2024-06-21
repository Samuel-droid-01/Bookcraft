from .....main.bookcraft.screens.bibliotecario.principal_bibliotecario import PrincipalBibliotecario
from tkinter import Tk
def test_Principal():
    raiz = Tk()
    aplicacion = PrincipalBibliotecario (raiz)
    raiz.mainloop()

if __name__ == '__main__':
    test_Principal()