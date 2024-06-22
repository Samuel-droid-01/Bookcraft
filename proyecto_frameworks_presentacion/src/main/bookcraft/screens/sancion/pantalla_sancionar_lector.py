
from proyecto_frameworks_persistencia.src.main.bookcraft.dao.libro.libroDAO import LibroDAO
from proyecto_frameworks_persistencia.src.main.bookcraft.dao.prestamo.prestamoDAO import PrestamoDAO
from proyecto_frameworks_persistencia.src.main.bookcraft.dao.administrador.administradorDAO import AdministradorDAO
from proyecto_frameworks_persistencia.src.main.bookcraft.bd.mappers.prestamo.prestamo_map import PrestamoMapper
from proyecto_frameworks_persistencia.src.main.bookcraft.dao.sancion.sancionDAO import SancionDAO
from tkinter import *
from tkinter import messagebox as ms

class SacionarLector:
    def __init__(self, raiz,id_libro,id_usuario):
        self.raiz = raiz
        self.id_libro = id_libro
        self.id_usuario = id_usuario
        self.raiz.title("Sistema de biblioteca Bookcraft")
        
        # Configurar geometría y fondo
        geometría = "600x500+220+200"
        self.raiz.geometry(geometría)
        self.raiz.configure(background='black')
        
        # Marco principal
        self.MarcoPrincipal = Frame(self.raiz)
        self.MarcoPrincipal.pack(fill=BOTH, expand=True)
        
        self.lblTitulo = Label(self.MarcoPrincipal, font=('arial', 24, 'bold'), text="Bookcraft Library System", bg="black", fg="white")
        self.lblTitulo.pack(side=TOP, fill=X)
        
        self.lblTitulo2 = Label(self.MarcoPrincipal, font=('arial', 24, 'bold'), text="Sancionar Lector")
        self.lblTitulo2.pack(side=TOP, fill=X)
        
        frame_usuario = Frame(self.MarcoPrincipal, bd=2, relief=SOLID, bg="white", padx=10, pady=10)
        frame_usuario.pack(fill=BOTH, expand=True, padx=10, pady=10)
        # Configura el layout usando grid en lugar de pack
        frame_usuario.grid_columnconfigure(0, weight=1)
        frame_usuario.grid_columnconfigure(1, weight=3)
        
        Label(frame_usuario, text="Descripcion de la sancion", bg="white").grid(row=0, column=0, sticky="w")
        self.descripcion_sancion_entry = Entry(frame_usuario)
        self.descripcion_sancion_entry.grid(row=0, column=1, sticky="ew")
        
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
        
        # Añadir el formulario al marco de detalles
        # self.mostrar_formulario()
        self.buscar_prestammo()
    def limpiar_detalles(self):
        # Limpiar el marco de detalles antes de mostrar nuevos contenidos
        for widget in self.MarcoDetalles.winfo_children():
            widget.destroy()
    
    def buscar_prestammo(self):
        prestamoDAO=PrestamoDAO()
        Ids=prestamoDAO.obtener_prestamos_usuario(self.id_usuario)
        usuarioDAO=AdministradorDAO()
        usuario=usuarioDAO.ver_usuario(self.id_usuario)
        
        i=0
        bandera=0
        while i<len(Ids) and Ids[i][1]!=self.id_libro:
            if Ids[i][1]!=self.id_libro:
                bandera=1
            i+=1 
        if i==0:
            bandera=1  
        libroDAO=LibroDAO()
        if bandera==1:
           libro=libroDAO.get_libro_by_id(self.id_libro)
           prestamoMapper= PrestamoMapper()
           presamo=prestamoMapper.get_by_id(Ids[i][0])
     
           self.mostrar_usuario(usuario,libro,presamo)
        else:
            return
        
    
    def Sancionar(self,id,descripcion):
        
        
        prestamoDAO=PrestamoDAO(id=id)
        prestamo=prestamoDAO.get_prestamo()
        prestamo.set_activo(False)
        
        sancionDAO=SancionDAO()
        descripcion="Entrega tardía de libro"
        idSancio=sancionDAO.crear_sancion(descripcion=descripcion)
        prestamo.set_id_sancion(idSancio)
        prestamoDAO.update_prestamo()
        ms.showinfo("Sancionar", "El lector ha sido sancionado.")
        self.raiz.destroy()
    def mostrar_usuario(self, usuario,libro,presta):
        self.limpiar_detalles()
        
        frame_usuario = Frame(self.MarcoDetalles, bd=2, relief=SOLID, bg="white", padx=10, pady=10)
        frame_usuario.pack(fill=BOTH, expand=True, padx=10, pady=10)
        
        Label(frame_usuario, text=f"Nombres: {usuario.get_nombres()}", bg="white").pack(anchor="w")
        Label(frame_usuario, text=f"Apellido: {usuario.get_apellidos()}", bg="white").pack(anchor="w")
        Label(frame_usuario, text=f"id_rol: {usuario.get_id_rol()}", bg="white").pack(anchor="w")
        Label(frame_usuario, text=f"correo: {usuario.get_correo()}", bg="white").pack(anchor="w")
        Label(frame_usuario, text=f"titulo:{libro.get_titulo()}", bg="white").pack(anchor="w")
        Label(frame_usuario, text=f"isbn: {libro.get_isbn()}", bg="white").pack(anchor="w")
        Label(frame_usuario, text=f"fecha de prestamo: {presta.get_fecha_prestamo()}", bg="white").pack(anchor="w")
        Label(frame_usuario, text=f"fecha de devolucion: {presta.get_fecha_devolucion()}", bg="white").pack(anchor="w")
        Label(frame_usuario, text=f"activo: {presta.get_activo()}", bg="white").pack(anchor="w")
        
        frame_boton = Frame(frame_usuario, bg="white")
        frame_boton.pack(fill=BOTH, expand=True)
        Button(frame_boton, text="Sancionar", font=('arial', 9, 'bold'), bg="#2E4053", fg="white", command=lambda: self.Sancionar(id=presta.get_id(),descripcion=self.descripcion_sancion_entry.get())).grid(row=0, column=0, padx=10, pady=10)