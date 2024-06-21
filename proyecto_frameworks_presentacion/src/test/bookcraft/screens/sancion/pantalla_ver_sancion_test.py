from tkinter import *
from proyecto_frameworks_persistencia.src.main.bookcraft.dao.sancion.sancionDAO import SancionDAO
from proyecto_frameworks_presentacion.src.main.bookcraft.screens.sancion.pantalla_ver_sancion import PantallaIDSancion

if __name__ == "__main__":
    root = Tk()
    app = PantallaIDSancion(root)
    root.mainloop()
