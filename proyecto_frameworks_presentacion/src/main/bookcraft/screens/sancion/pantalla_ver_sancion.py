from tkinter import *
from tkinter import messagebox as ms
from proyecto_frameworks_persistencia.src.main.bookcraft.dao.sancion.sancionDAO import SancionDAO

class PantallaIDSancion:
    def __init__(self, raiz):
        self.raiz = raiz
        self.raiz.title("Ver Sanción - Bookcraft Library System")
        
        # Configurar geometría y fondo
        geometria = "450x200+220+200"
        self.raiz.geometry(geometria)
        self.raiz.configure(background='black')

        # Marco principal
        self.MarcoPrincipal = Frame(self.raiz)
        self.MarcoPrincipal.pack(fill=BOTH, expand=True)

        self.lblTitulo = Label(self.MarcoPrincipal, font=('arial', 24, 'bold'), text="Eliminar Sanción", bg="black", fg="white")
        self.lblTitulo.pack(side=TOP, fill=X)

        # Marco para el contenido
        self.MarcoContenido = Frame(self.MarcoPrincipal, bg="#B9BED3", pady=20)
        self.MarcoContenido.pack(fill=BOTH, expand=True)

        self.lblID = Label(self.MarcoContenido, text="ID de la Sanción:", bg="#B9BED3")
        self.lblID.pack(side=LEFT, padx=10)

        self.id_entry = Entry(self.MarcoContenido)
        self.id_entry.pack(side=LEFT, padx=10)

        self.btnEliminar = Button(self.MarcoContenido, text="Aceptar", command=self.ver_sancion)
        self.btnEliminar.pack(side=LEFT, padx=10)

    def ver_sancion(self):
        sancion_id = self.id_entry.get()
        sancion_dao = SancionDAO()
        sancion = sancion_dao.buscar_sancion(sancion_id)

        if not sancion_id.isdigit() or not sancion:
            ms.showerror("Error", "Por favor, ingrese un ID válido")
            return

        root = Tk()
        app = PantallaVerSancion(root, sancion)
        root.mainloop()


class PantallaVerSancion:
    def __init__(self, raiz, sancion):
        self.raiz = raiz
        self.sanciones = sancion
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

        if sancion:
            self.mostrar_sancion(sancion)
        else:
            ms.showerror("Error", f"No se encontró ninguna sanción para el lector con ID {self.id_lector}")

    def mostrar_sancion(self, sancion):
        Label(self.MarcoDetallesSancion, font=('Arial', 12, 'bold'), text="Nombre:", bg="white", fg="#333333").grid(row=0, column=0, sticky="w", padx=10, pady=5)
        Label(self.MarcoDetallesSancion, font=('Arial', 10), text=sancion.get_nombre(), bg="white").grid(row=0, column=1, sticky="w", padx=10, pady=5)

        Label(self.MarcoDetallesSancion, font=('Arial', 12, 'bold'), text="Fecha de Inicio:", bg="white", fg="#333333").grid(row=1, column=0, sticky="w", padx=10, pady=5)
        Label(self.MarcoDetallesSancion, font=('Arial', 10), text=sancion.get_fecha_inicio(), bg="white").grid(row=1, column=1, sticky="w", padx=10, pady=5)

        Label(self.MarcoDetallesSancion, font=('Arial', 12, 'bold'), text="Fecha de Fin:", bg="white", fg="#333333").grid(row=2, column=0, sticky="w", padx=10, pady=5)
        Label(self.MarcoDetallesSancion, font=('Arial', 10), text=sancion.get_fecha_fin(), bg="white").grid(row=2, column=1, sticky="w", padx=10, pady=5)

        Label(self.MarcoDetallesSancion, font=('Arial', 12, 'bold'), text="Descripción:", bg="white", fg="#333333").grid(row=3, column=0, sticky="nw", padx=10, pady=5)
        descripcion = Label(self.MarcoDetallesSancion, font=('Arial', 10), text=sancion.get_descripcion(), bg="white", wraplength=350, justify="left")
        descripcion.grid(row=3, column=1, sticky="nw", padx=10, pady=5)
