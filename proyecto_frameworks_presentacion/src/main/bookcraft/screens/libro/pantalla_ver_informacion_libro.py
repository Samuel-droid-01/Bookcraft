from proyecto_frameworks_persistencia.src.main.bookcraft.dao.libro.libroDAO import LibroDAO
from tkinter import *
from tkinter import messagebox as ms

class InformacionLibro:
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
        
        # Filtrar búsqueda
        self.MarcoBusqueda = Frame(self.MarcoPrincipal, bd=0, relief=RIDGE)
        self.MarcoBusqueda.pack(side=TOP, fill=X, padx=10, pady=10)

        lblFiltrar = Label(self.MarcoBusqueda, text="Buscar libro por id:", font=('arial', 12, 'bold'))
        lblFiltrar.grid(row=0, column=0, padx=10, pady=10, sticky=W)

        self.entryBusqueda = Entry(self.MarcoBusqueda, font=('arial', 12))
        self.entryBusqueda.grid(row=0, column=2, padx=10, pady=10)

        btnBuscar = Button(self.MarcoBusqueda, padx=10, pady=5, bd=5, font=('arial', 9, 'bold'), text='Buscar', bg="#2E4053", fg="white", command=self.buscar_libro)
        btnBuscar.grid(row=0, column=3, padx=10, pady=10)

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

    def limpiar_detalles(self):
        # Limpiar el marco de detalles antes de mostrar nuevos contenidos
        for widget in self.MarcoDetalles.winfo_children():
            widget.destroy()
    
    def buscar_libro(self):
        termino = self.entryBusqueda.get()
        if not termino.isdigit():
            ms.showerror("Error", "El ID del libro debe ser un número.")
            return
        
        libroDAO = LibroDAO()
        libro = libroDAO.ver_libro(int(termino))
        
        if libro:
            self.mostrar_libro(libro)
        else:
            ms.showinfo("Buscar", f"No se encontró el libro con ID: {termino}")

    def mostrar_libro(self, libro):
        self.limpiar_detalles()
        
        frame_libro = Frame(self.MarcoDetalles, bd=2, relief=SOLID, bg="white", padx=10, pady=10)
        frame_libro.pack(fill=BOTH, expand=True, padx=10, pady=10)
        
        Label(frame_libro, text=f"Titulo: {libro.get_titulo()}", bg="white").pack(anchor="w")
        Label(frame_libro, text=f"Isbn: {libro.get_isbn()}", bg="white").pack(anchor="w")
        Label(frame_libro, text=f"Autor: {libro.get_autor()}", bg="white").pack(anchor="w")
        Label(frame_libro, text=f"Editorial: {libro.get_editorial()}", bg="white").pack(anchor="w")
        Label(frame_libro, text=f"Fecha de publicacion: {libro.get_fecha_publicacion()}", bg="white").pack(anchor="w")
        Label(frame_libro, text=f"Id categoria: {libro.get_id_categoria()}", bg="white").pack(anchor="w")
        Label(frame_libro, text=f"Edicion: {libro.get_edicion()}", bg="white").pack(anchor="w")
        Label(frame_libro, text=f"Numero de paginas: {libro.get_numero_paginas()}", bg="white").pack(anchor="w")
        Label(frame_libro, text=f"Numero de copias: {libro.get_numero_copias()}", bg="white").pack(anchor="w")
        Label(frame_libro, text=f"Copias disponibles: {libro.get_copias_disponibles()}", bg="white").pack(anchor="w")

if __name__ == '__main__':
    raiz = Tk()
    aplicacion = InformacionLibro(raiz)
    raiz.mainloop()
