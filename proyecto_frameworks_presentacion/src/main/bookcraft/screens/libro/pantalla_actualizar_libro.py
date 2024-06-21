from proyecto_frameworks_persistencia.src.main.bookcraft.dao.libro.libroDAO import LibroDAO
from tkinter import *
from tkinter import messagebox as ms
from tkcalendar import DateEntry  

class ActualizarLibro:
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
        
        self.lblTitulo2 = Label(self.MarcoPrincipal, font=('arial', 24, 'bold'), text="Actualizar Libros")
        self.lblTitulo2.pack(side=TOP, fill=X)
        
        # Filtrar búsqueda
        self.MarcoBusqueda = Frame(self.MarcoPrincipal, bd=0, relief=RIDGE)
        self.MarcoBusqueda.pack(side=TOP, fill=X, padx=10, pady=10)

        lblFiltrar = Label(self.MarcoBusqueda, text="Ingresa el id del Libro:", font=('arial', 12, 'bold'))
        lblFiltrar.grid(row=0, column=0, padx=10, pady=10, sticky=W)

        self.entryBusqueda = Entry(self.MarcoBusqueda, font=('arial', 12))
        self.entryBusqueda.grid(row=0, column=2, padx=10, pady=10)

        btnBuscar = Button(self.MarcoBusqueda, padx=10, pady=5, bd=5, font=('arial', 9, 'bold'), text='Buscar', bg="#2E4053",fg="white", command=self.ver_libro)
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
    
    def ver_libro(self):
        termino = self.entryBusqueda.get()
        if not termino.isdigit():
            ms.showerror("Error", "El ID del libro debe ser un número.")
            return
        
        self.libro_id = int(termino)
        libro = LibroDAO(id=self.libro_id)
        
        if libro:
            self.mostrar_formulario(libro)
        else:
            ms.showinfo("Error", "Libro no encontrado")
            
    def mostrar_formulario(self,libro):
        self.limpiar_detalles()

        form_frame = Frame(self.MarcoDetalles, bg="#CACFD2")
        form_frame.pack(expand=True)

        Label(form_frame, text="Título:", font=('arial', 12, 'bold'), bg="#CACFD2").grid(row=1, column=0, padx=10, pady=5, sticky="e")
        self.entry_titulo = Entry(form_frame, font=('arial', 12, 'bold'), width=30)
        self.entry_titulo.grid(row=1, column=1, padx=10, pady=5, sticky="w")
        self.entry_titulo.insert(0, libro.get_libro().get_titulo())

        Label(form_frame, text="ISBN:", font=('arial', 12, 'bold'), bg="#CACFD2").grid(row=2, column=0, padx=10, pady=5, sticky="e")
        self.entry_isbn = Entry(form_frame, font=('arial', 12, 'bold'), width=30)
        self.entry_isbn.grid(row=2, column=1, padx=10, pady=5, sticky="w")
        self.entry_isbn.insert(0, libro.get_libro().get_isbn())

        Label(form_frame, text="Autor:", font=('arial', 12, 'bold'), bg="#CACFD2").grid(row=3, column=0, padx=10, pady=5, sticky="e")
        self.entry_autor = Entry(form_frame, font=('arial', 12, 'bold'), width=30)
        self.entry_autor.grid(row=3, column=1, padx=10, pady=5, sticky="w")
        self.entry_autor.insert(0, libro.get_libro().get_autor())

        Label(form_frame, text="Editorial:", font=('arial', 12, 'bold'), bg="#CACFD2").grid(row=4, column=0, padx=10, pady=5, sticky="e")
        self.entry_editorial = Entry(form_frame, font=('arial', 12, 'bold'), width=30)
        self.entry_editorial.grid(row=4, column=1, padx=10, pady=5, sticky="w")
        self.entry_editorial.insert(0, libro.get_libro().get_editorial())

        Label(form_frame, text="Fecha de Publicación:", font=('arial', 12, 'bold'), bg="#CACFD2").grid(row=5, column=0, padx=10, pady=5, sticky="e")
        self.entry_fecha_publicacion = Entry(form_frame, font=('arial', 12, 'bold'), width=30) 
        self.entry_fecha_publicacion.grid(row=5, column=1, padx=10, pady=5, sticky="w")
        self.entry_fecha_publicacion.insert(0, libro.get_libro().get_fecha_publicacion())

        Label(form_frame, text="ID Categoría:", font=('arial', 12, 'bold'), bg="#CACFD2").grid(row=6, column=0, padx=10, pady=5, sticky="e")
        self.entry_id_categoria = Entry(form_frame, font=('arial', 12, 'bold'), width=30)
        self.entry_id_categoria.grid(row=6, column=1, padx=10, pady=5, sticky="w")
        self.entry_id_categoria.insert(0, libro.get_libro().get_id_categoria())

        Label(form_frame, text="Edición:", font=('arial', 12, 'bold'), bg="#CACFD2").grid(row=7, column=0, padx=10, pady=5, sticky="e")
        self.entry_edicion = Entry(form_frame, font=('arial', 12, 'bold'), width=30)
        self.entry_edicion.grid(row=7, column=1, padx=10, pady=5, sticky="w")
        self.entry_edicion.insert(0, libro.get_libro().get_edicion())

        Label(form_frame, text="Número de Páginas:", font=('arial', 12, 'bold'), bg="#CACFD2").grid(row=8, column=0, padx=10, pady=5, sticky="e")
        self.entry_numero_paginas = Entry(form_frame, font=('arial', 12, 'bold'), width=30)
        self.entry_numero_paginas.grid(row=8, column=1, padx=10, pady=5, sticky="w")
        self.entry_numero_paginas.insert(0, libro.get_libro().get_numero_paginas())

        Label(form_frame, text="Número de Copias:", font=('arial', 12, 'bold'), bg="#CACFD2").grid(row=9, column=0, padx=10, pady=5, sticky="e")
        self.entry_numero_copias = Entry(form_frame, font=('arial', 12, 'bold'), width=30)
        self.entry_numero_copias.grid(row=9, column=1, padx=10, pady=5, sticky="w")
        self.entry_numero_copias.insert(0, libro.get_libro().get_numero_copias())

        Label(form_frame, text="Copias Disponibles:", font=('arial', 12, 'bold'), bg="#CACFD2").grid(row=10, column=0, padx=10, pady=5, sticky="e")
        self.entry_copias_disponibles = Entry(form_frame, font=('arial', 12, 'bold'), width=30)
        self.entry_copias_disponibles.grid(row=10, column=1, padx=10, pady=5, sticky="w")
        self.entry_copias_disponibles.insert(0, libro.get_libro().get_copias_disponibles())

        # Botón de envío
        self.boton_enviar = Button(form_frame, text="Enviar", font=('arial', 12, 'bold'), command=self.enviar_formulario)
        self.boton_enviar.grid(row=11, column=1, pady=10, sticky="e")
    
    def enviar_formulario(self):
        libro=LibroDAO(id=self.entryBusqueda.get())
        libro.get_libro().set_titulo(self.entry_titulo.get()),
        libro.get_libro().set_isbn(self.entry_isbn.get()),
        libro.get_libro().set_autor(self.entry_autor.get()),
        libro.get_libro().set_editorial(self.entry_editorial.get()),
        libro.get_libro().set_fecha_publicacion(self.entry_fecha_publicacion.get()),
        libro.get_libro().set_id_categoria(int(self.entry_id_categoria.get())),
        libro.get_libro().set_edicion(int(self.entry_edicion.get())),
        libro.get_libro().set_numero_paginas(int(self.entry_numero_paginas.get())),
        libro.get_libro().set_numero_copias(int(self.entry_numero_copias.get())),
        libro.get_libro().set_copias_disponibles(int(self.entry_copias_disponibles.get()))
        try:
            libro.update_libro()
            ms.showinfo("Éxito", "Libro actualizado correctamente")
        except Exception as e:
            ms.showerror("Error", f"Error al actualizar el libro: {e}")

if __name__ == '__main__':
    raiz = Tk()
    aplicacion = ActualizarLibro(raiz)
    raiz.mainloop()
