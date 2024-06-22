from tkinter import *
from proyecto_frameworks_persistencia.src.main.bookcraft.dao.sancion.sancionDAO import SancionDAO
from proyecto_frameworks_presentacion.src.main.bookcraft.screens.sancion.pantalla_estado_sancion import PantallaEstadoSancion

if __name__ == "__main__":
    root = Tk()
    app = PantallaEstadoSancion(root,id_sancion=1)
    root.mainloop()