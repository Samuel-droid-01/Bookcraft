from proyecto_frameworks_persistencia.src.main.bookcraft.dao.libro.libroDAO import LibroDAO
from proyecto_frameworks_persistencia.src.main.bookcraft.dao.catalogo.catalogoDAO import CatalogoDAO
from tkinter import *
from tkinter.ttk import Combobox
from tkinter import messagebox as ms


class ListarLibro:
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
        
        self.lblTitulo2 = Label(self.MarcoPrincipal, font=('arial', 24, 'bold'), text="Libros")
        self.lblTitulo2.pack(side=TOP, fill=X)

        # Barra de navegación
        self.BarraNavegacion = Frame(self.MarcoPrincipal, bd=0, relief=RIDGE)
        self.BarraNavegacion.pack( side=TOP, fill=X)  # Fill X para expandirse horizontalmente

        self.marcoBusqueda = Frame(self.MarcoPrincipal, bd=20, pady=5, bg="#B9BED3",height=100)
        self.marcoBusqueda.pack(side=TOP, fill=X, expand=False)
        # Marco para detalles de contenido y filtro
        self.MarcoDetallesLector = LabelFrame(self.MarcoPrincipal, bd=20, pady=5, relief=RIDGE, bg="#B9BED3")
        self.MarcoDetallesLector.pack(side=BOTTOM, fill=BOTH, expand=True)

        self.stringBusqueda = StringVar().set("")
        self.fuente=("Arial", 14)
        self.lblBusqueda = Label(self.marcoBusqueda, text="Buscar por:", bg="#B9BED3", font=self.fuente)
        self.lblBusqueda.grid(row=0, column=0, padx=10, pady=10)

        self.opciones = ["Titulo", "Autor", "Editorial","Categoria"]
        self.comboBusqueda = Combobox(self.marcoBusqueda, values=self.opciones, state="readonly",font=self.fuente)
        self.comboBusqueda.grid(row=0, column=1, padx=10, pady=10)
        self.comboBusqueda.current(0)

        self.comboBusqueda.bind("<<ComboboxSelected>>", self.on_combo_change)
        self.comboCategorias = Combobox()#Se inicializa vacio
        self.txtBusqueda = Entry(self.marcoBusqueda,font=self.fuente)
        self.txtBusqueda.grid(row=0, column=2, padx=10, pady=10)

        self.btnBuscar = Button(self.marcoBusqueda, text="Buscar",font=self.fuente ,command=lambda: self.filtrar(self.comboBusqueda.get(), self.txtBusqueda.get()))
        self.btnBuscar.grid(row=0, column=3, padx=10, pady=10)

        self.btnLimpiar = Button(self.marcoBusqueda, text="Limpiar",font=self.fuente, command=self.limpiar_detalles)
        self.btnLimpiar.grid(row=0, column=4, padx=10, pady=10)

        # Canvas y scrollbar
        self.canvas = Canvas(self.MarcoDetallesLector, bg="#CACFD2")
        self.canvas.pack(side=LEFT, fill=BOTH, expand=True, padx=10, pady=10)

        self.scrollbar = Scrollbar(self.MarcoDetallesLector, orient=VERTICAL, command=self.canvas.yview)
        self.scrollbar.pack(side=RIGHT, fill=Y)
        self.canvas.configure(yscrollcommand=self.scrollbar.set)
        self.scrollable_frame = Frame(self.canvas, bg="#CACFD2")
        self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")

        self.scrollable_frame.bind("<Configure>", self.on_frame_configure)
        self.scrollable_frame.bind_all("<MouseWheel>", self._on_mousewheel)

        libroDAO = LibroDAO()
        self.admin = libroDAO.listar_libros()
        
        # Mostrar tarjetas de usuarios obtenidos del servicio
        self.mostrar_libros(self.admin)

    def on_combo_change(self, event):
        seleccion = self.comboBusqueda.get()
        if seleccion == "Categoria" or seleccion == "Editorial":
            # Reemplazar Entry con un nuevo Combobox
            self.txtBusqueda.grid_forget()  # Oculta el Entry actual
            categorias = CatalogoDAO().ver_categorias()
            editoriales=LibroDAO().ver_editoriales()
            if seleccion == "Editorial":
                self.comboCategorias = Combobox(self.marcoBusqueda, values=editoriales, state="readonly",font=self.fuente)
            else:
                self.comboCategorias = Combobox(self.marcoBusqueda, values=categorias, state="readonly",font=self.fuente)
            self.comboCategorias.grid(row=0, column=2, padx=10, pady=10)
            self.comboCategorias.current(0)
        else:
            # Reemplazar Combobox con un Entry
            self.comboCategorias.grid_forget()  # Oculta el Combobox de categorías si existe
            self.txtBusqueda = Entry(self.marcoBusqueda, font=self.fuente)
            self.txtBusqueda.grid(row=0, column=2, padx=10, pady=10)
        
    def filtrar(self,opcion,valor):#opcion y nombre del libro o autor
        if opcion=="Titulo":
            libros=LibroDAO().filtrar_titulo(valor)
            if libros[0]!=None:
                self.mostrar_libros(libros[1])
            else:
                ms.showerror("Error", libros[1])
        elif opcion=="Autor":
            libros=LibroDAO().filtrar_autor(valor)
            if libros[0]!=None:
                self.mostrar_libros(libros[1])
            else:
                ms.showerror("Error", libros[1])

        elif opcion=="Editorial":
            valor=self.comboCategorias.get()
            libros=LibroDAO().filtrar_editorial(valor)
            if libros[0]!=None:
                self.mostrar_libros(libros[1])
            else:
                ms.showerror("Error", libros[1])
        elif opcion=="Categoria":
            valor=self.comboCategorias.get()
            libros=LibroDAO().filtrar_categoria(valor)
            if libros[0]!=None:
                self.mostrar_libros(libros[1])
            else:
                ms.showerror("Error", libros[1])

    def _on_mousewheel(self, event):
        self.canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")

    def on_frame_configure(self, event):
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))


    def limpiar_detalles(self):
        # Limpiar el marco de detalles antes de mostrar nuevos contenidos
        for widget in self.scrollable_frame.winfo_children():
            widget.destroy()

        

    def mostrar_libros(self, libros):
        self.limpiar_detalles()
        for index, libro in enumerate(libros):
            frame_libro = Frame(self.scrollable_frame, bd=2, relief=SOLID, bg="white", padx=10, pady=10,width=250,height=250)
            frame_libro.grid(row=index // 2, column=index % 2, padx=10, pady=10, sticky="nsew")#
            
            Label(frame_libro, text=f"Titulo: {libro.get_titulo()}", bg="white").pack(anchor="w")
            Label(frame_libro, text=f"Isbn: {libro.get_isbn()}", bg="white").pack(anchor="w")
            Label(frame_libro, text=f"Autor: {libro.get_autor()}", bg="white").pack(anchor="w")
            Label(frame_libro, text=f"Editorial: {libro.get_editorial()}", bg="white").pack(anchor="w")
            Label(frame_libro, text=f"Fecha de publicacion: {libro.get_fecha_publicacion()}", bg="white").pack(anchor="w")
            Label(frame_libro, text=f"Edicion: {libro.get_edicion()}", bg="white").pack(anchor="w")
            Label(frame_libro, text=f"Numero de paginas: {libro.get_numero_paginas()}", bg="white").pack(anchor="w")
            Label(frame_libro, text=f"Numero de copias: {libro.get_numero_copias()}", bg="white").pack(anchor="w")
            Label(frame_libro, text=f"Copias disponibles: {libro.get_copias_disponibles()}", bg="white").pack(anchor="w")



