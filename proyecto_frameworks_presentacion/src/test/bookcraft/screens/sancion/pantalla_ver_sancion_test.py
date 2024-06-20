from tkinter import *
from proyecto_frameworks_persistencia.src.main.bookcraft.dao.sancion.sancionDAO import SancionDAO
from proyecto_frameworks_presentacion.src.main.bookcraft.screens.sancion.pantalla_ver_sancion import PantallaVerSancion

if __name__ == "__main__":
    root = Tk()
    sancionDao = SancionDAO()
    sancion = sancionDao.buscar_sancion(1)
    app = PantallaVerSancion(root, sancion)
    root.mainloop()
