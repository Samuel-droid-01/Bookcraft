from tkinter import *
from tkinter import messagebox as ms
from proyecto_frameworks_persistencia.src.main.bookcraft.dao.sancion.sancionDAO import SancionDAO
from datetime import datetime

class PantallaEstadoSancion:
    def __init__(self, raiz, id_sancion=1):
        self.raiz = raiz
        self.id_sancion = id_sancion
        self.raiz.title("Ver Sanción - Bookcraft Library System")
        
        # Configurar geometría y fondo
        geometria = "450x300+300+200"  # Ajustar tamaño de la ventana
        self.raiz.geometry(geometria)
        self.raiz.configure(background='#E8E8E8')  # Color de fondo claro

        # Marco principal
        self.MarcoPrincipal = Frame(self.raiz, bg='#E8E8E8')  # Fondo claro para el marco principal
        self.MarcoPrincipal.pack(fill=BOTH, expand=True)

        # Título
        self.lblTitulo = Label(self.MarcoPrincipal, font=('Arial', 18, 'bold'), text="Bookcraft Library System", bg='#E8E8E8', fg='#333333')
        self.lblTitulo.pack(side=TOP, fill=X, pady=10)

        # Título de la sección
        self.lblTitulo2 = Label(self.MarcoPrincipal, font=('Arial', 16, 'bold'), text="Detalles de la Sanción", bg='#E8E8E8', fg='#333333')
        self.lblTitulo2.pack(side=TOP, fill=X, pady=5)

        # Marco para detalles de la sanción
        self.MarcoDetallesSancion = LabelFrame(self.MarcoPrincipal, bd=10, pady=10, relief=RIDGE, bg="white")
        self.MarcoDetallesSancion.pack(side=TOP, fill=BOTH, padx=20, pady=10, expand=True)
        sancionDAO= SancionDAO()
        
        sancion=sancionDAO.obtener_sancion_usuario(self.id_sancion)
        if sancion:
            self.mostrar_sancion(sancion)
        else:
            ms.showerror("Error", f"No se encontró ninguna sanción para el lector")

    def mostrar_sancion(self, sancion):
        Label(self.MarcoDetallesSancion, font=('Arial', 12, 'bold'), text="Descreipcion", bg="white", fg="#333333").grid(row=0, column=0, sticky="w", padx=10, pady=5)
        Label(self.MarcoDetallesSancion, font=('Arial', 10), text=sancion.get_nombre(), bg="white").grid(row=0, column=1, sticky="w", padx=10, pady=5)

        Label(self.MarcoDetallesSancion, font=('Arial', 12, 'bold'), text="", bg="white", fg="#333333").grid(row=1, column=0, sticky="w", padx=10, pady=5)
        Label(self.MarcoDetallesSancion, font=('Arial', 10), text=sancion.get_fecha_inicio(), bg="white").grid(row=1, column=1, sticky="w", padx=10, pady=5)

        Label(self.MarcoDetallesSancion, font=('Arial', 12, 'bold'), text="", bg="white", fg="#333333").grid(row=2, column=0, sticky="w", padx=10, pady=5)
        Label(self.MarcoDetallesSancion, font=('Arial', 10), text=sancion.get_fecha_fin(), bg="white").grid(row=2, column=1, sticky="w", padx=10, pady=5)

        Label(self.MarcoDetallesSancion, font=('Arial', 12, 'bold'), text="", bg="white", fg="#333333").grid(row=3, column=0, sticky="nw", padx=10, pady=5)
        descripcion = Label(self.MarcoDetallesSancion, font=('Arial', 10), text=sancion.get_descripcion(), bg="white", wraplength=350, justify="left")
        descripcion.grid(row=3, column=1, sticky="nw", padx=10, pady=5)
        
        temporal = sancion.get_descripcion()  # Este nombre de método parece incorrecto para obtener una fecha. Verifica que sea el correcto.

        tiempo_hoy = datetime.now().date()  # Convertir a datetime.date para asegurar compatibilidad de tipos
        tiempotrancurrido = tiempo_hoy - temporal

        # Ahora tiempotrancurrido es un objeto timedelta que representa la diferencia entre las fechas
        Label(self.MarcoDetallesSancion, font=('Arial', 12, 'bold'), text="Tiempo para devolver el libro", bg="white", fg="#333333").grid(row=3, column=0, sticky="nw", padx=10, pady=5)
        descripcion = Label(self.MarcoDetallesSancion, font=('Arial', 10), text=str(tiempotrancurrido), bg="white", wraplength=350, justify="left")
        descripcion.grid(row=3, column=1, sticky="nw", padx=10, pady=5)
        
