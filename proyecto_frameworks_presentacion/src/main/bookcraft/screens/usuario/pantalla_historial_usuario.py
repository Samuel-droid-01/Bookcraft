from proyecto_frameworks_persistencia.src.main.bookcraft.dao.prestamo.prestamoDAO import PrestamoDAO
from proyecto_frameworks_persistencia.src.main.bookcraft.bd.mappers.prestamo.prestamo_map import PrestamoMapper
from proyecto_frameworks_persistencia.src.main.bookcraft.bd.mappers.usuario.usuario_map import UsuarioMapper
from proyecto_frameworks_persistencia.src.main.bookcraft.dao.libro.libroDAO import LibroDAO
from tkinter import *
from tkinter import messagebox as ms

class HistorialUsuario:
    def __init__(self, raiz,id_usuario):
        self.raiz = raiz
        self.id_usuario = id_usuario
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
        
        self.lblTitulo2 = Label(self.MarcoPrincipal, font=('arial', 24, 'bold'), text="Ver Historial de Prestamo")
        self.lblTitulo2.pack(side=TOP, fill=X)
        
        # Filtrar búsqueda
        # self.MarcoBusqueda = Frame(self.MarcoPrincipal, bd=0, relief=RIDGE)
        # self.MarcoBusqueda.pack(side=TOP, fill=X, padx=10, pady=10)

        # lblFiltrar = Label(self.MarcoBusqueda, text="Buscar usuario por id:", font=('arial', 12, 'bold'))
        # lblFiltrar.grid(row=0, column=0, padx=10, pady=10, sticky=W)

        # self.entryBusqueda = Entry(self.MarcoBusqueda, font=('arial', 12))
        # self.entryBusqueda.grid(row=0, column=2, padx=10, pady=10)

        # btnBuscar = Button(self.MarcoBusqueda, padx=10, pady=5, bd=5, font=('arial', 9, 'bold'), text='Buscar', bg="#2E4053", fg="white", command=self.buscar_libro)
        # btnBuscar.grid(row=0, column=3, padx=10, pady=10)

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
        self.buscar_libro()

    def limpiar_detalles(self):
        # Limpiar el marco de detalles antes de mostrar nuevos contenidos
        for widget in self.MarcoDetalles.winfo_children():
            widget.destroy()
    
    def buscar_libro(self):
        historia=[]
        prestamo=PrestamoDAO()
        
        prestamos=prestamo.obtener_prestamos_usuario(self.id_usuario)
        for solicitud in prestamos:
            
            presta=PrestamoDAO()
            usuario=UsuarioMapper().get_by_id(self.id_usuario)
            libro=LibroDAO().get_libro_by_id(solicitud[1])
           
        
            informacion = {
                "idUsuario": self.id_usuario,
                "idLibro": solicitud[0],
                "nombre": usuario.get_nombres(),
                "apellido": usuario.get_apellidos(),
                "titulo": libro.get_titulo(),
                "fechaDEV": solicitud[2],
                "isbn": libro.get_isbn()
            }
            historia.append(informacion)
        if historia:
                
                self.mostrar_libro(historia)
        else:
            ms.showinfo("Buscar", f"No se le presto nigun el libro")
    def mostrar_libro(self, dato):
        self.limpiar_detalles()
        for dat in dato:
            frame_libro = Frame(self.MarcoDetalles, bd=2, relief=SOLID, bg="white", padx=10, pady=10)
            frame_libro.pack(fill=BOTH, expand=True, padx=10, pady=10)
            Label(frame_libro, text=f"Nombre: {dat['nombre']}", bg="white").pack(anchor="w")
            Label(frame_libro, text=f"Apellido: {dat['apellido']}", bg="white").pack(anchor="w")
            Label(frame_libro, text=f"Libro: {dat['titulo']}", bg="white").pack(anchor="w")
            Label(frame_libro, text=f"Fecha de devolución: {dat['fechaDEV']}", bg="white").pack(anchor="w")
            Label(frame_libro, text=f"Isbn: {dat['isbn']}", bg="white").pack(anchor="w")
            
