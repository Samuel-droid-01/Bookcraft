from proyecto_frameworks_persistencia.src.main.bookcraft.dao.administrador.administradorDAO import AdministradorDAO
from tkinter import *
from tkinter import messagebox as ms

class ListarUsuario:
    def __init__(self, raiz):
        self.raiz = raiz
        self.raiz.title("Sistema de biblioteca Bookcraft")
        
        # Configurar geometría y fondo
        geometria = "600x400+220+200"
        self.raiz.geometry(geometria)
        self.raiz.configure(background='black')
        
        # Marco principal
        self.MarcoPrincipal = Frame(self.raiz)
        self.MarcoPrincipal.pack(fill=BOTH, expand=True)

        self.lblTitulo = Label(self.MarcoPrincipal, font=('arial', 24, 'bold'), text="Bookcraft Library System", bg="black", fg="white")
        self.lblTitulo.pack(side=TOP, fill=X)
        
        self.lblTitulo2 = Label(self.MarcoPrincipal, font=('arial', 24, 'bold'), text="Usuarios")
        self.lblTitulo2.pack(side=TOP, fill=X)

        # Barra de navegación
        self.BarraNavegacion = Frame(self.MarcoPrincipal, bd=0, relief=RIDGE)
        self.BarraNavegacion.pack(side=TOP, fill=X)  # Fill X para expandirse horizontalmente

        # Marco para detalles de contenido
        self.MarcoDetallesLector = LabelFrame(self.MarcoPrincipal, bd=20, pady=5, relief=RIDGE, bg="#B9BED3")
        self.MarcoDetallesLector.pack(side=BOTTOM, fill=BOTH, expand=True)

        # Canvas y scrollbar
        self.canvas = Canvas(self.MarcoDetallesLector, bg="#CACFD2")
        self.scrollbar = Scrollbar(self.MarcoDetallesLector, orient=VERTICAL, command=self.canvas.yview)
        self.scrollable_frame = Frame(self.canvas, bg="#CACFD2")

        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: self.canvas.configure(
                scrollregion=self.canvas.bbox("all")
            )
        )

        self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        self.canvas.pack(side=LEFT, fill=BOTH, expand=True)
        self.scrollbar.pack(side=RIGHT, fill=Y)

        self.MarcoDetalles = self.scrollable_frame
        
        AdminDAO = AdministradorDAO()
        self.admin = AdminDAO.listar_usuarios()
        
        # Mostrar tarjetas de usuarios obtenidos del servicio
        self.mostrar_usuarios(self.admin)

    def limpiar_detalles(self):
        # Limpiar el marco de detalles antes de mostrar nuevos contenidos
        for widget in self.MarcoDetalles.winfo_children():
            widget.destroy()

    def mostrar_usuarios(self,usuarios):
        self.limpiar_detalles()
        
        for index, usuario in enumerate(usuarios):
            frame_usuario = Frame(self.MarcoDetalles, bd=2, relief=SOLID, bg="white", padx=10, pady=10)
            frame_usuario.grid(row=index // 2, column=index % 2, padx=10, pady=10, sticky="nsew")
            
            Label(frame_usuario, text=f"Id: {usuario.get_id()}", bg="white").pack(anchor="w")
            Label(frame_usuario, text=f"Nombre: {usuario.get_nombres()}", bg="white").pack(anchor="w")
            Label(frame_usuario, text=f"Apellidos: {usuario.get_apellidos()}", bg="white").pack(anchor="w")
            Label(frame_usuario, text=f"Correo: {usuario.get_correo()}", bg="white").pack(anchor="w")
            Label(frame_usuario, text=f"Teléfono: {usuario.get_contrasena()}", bg="white").pack(anchor="w")
