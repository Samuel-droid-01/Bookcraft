from proyecto_frameworks_persistencia.src.main.bookcraft.dao.libro.libroDAO import LibroDAO
from tkinter import *
from tkinter import messagebox as ms
from tkcalendar import DateEntry  

class RegistrarLibro:
    def __init__(self, raiz):
        self.raiz = raiz
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
        
        self.lblTitulo2 = Label(self.MarcoPrincipal, font=('arial', 24, 'bold'), text="Registrar Libro")
        self.lblTitulo2.pack(side=TOP, fill=X)
        
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
        self.mostrar_formulario()

    def limpiar_detalles(self):
        # Limpiar el marco de detalles antes de mostrar nuevos contenidos
        for widget in self.MarcoDetalles.winfo_children():
            widget.destroy()

    def mostrar_formulario(self):
        self.limpiar_detalles()

        form_frame = Frame(self.MarcoDetalles, bg="#CACFD2")
        form_frame.pack(expand=True)

        Label(form_frame, text="Título:", font=('arial', 12, 'bold'), bg="#CACFD2").grid(row=1, column=0, padx=10, pady=5, sticky="e")
        self.entry_titulo = Entry(form_frame, font=('arial', 12, 'bold'))
        self.entry_titulo.grid(row=1, column=1, padx=10, pady=5, sticky="w")

        Label(form_frame, text="ISBN:", font=('arial', 12, 'bold'), bg="#CACFD2").grid(row=2, column=0, padx=10, pady=5, sticky="e")
        self.entry_isbn = Entry(form_frame, font=('arial', 12, 'bold'))
        self.entry_isbn.grid(row=2, column=1, padx=10, pady=5, sticky="w")

        Label(form_frame, text="Autor:", font=('arial', 12, 'bold'), bg="#CACFD2").grid(row=3, column=0, padx=10, pady=5, sticky="e")
        self.entry_autor = Entry(form_frame, font=('arial', 12, 'bold'))
        self.entry_autor.grid(row=3, column=1, padx=10, pady=5, sticky="w")

        Label(form_frame, text="Editorial:", font=('arial', 12, 'bold'), bg="#CACFD2").grid(row=4, column=0, padx=10, pady=5, sticky="e")
        self.entry_editorial = Entry(form_frame, font=('arial', 12, 'bold'))
        self.entry_editorial.grid(row=4, column=1, padx=10, pady=5, sticky="w")

        Label(form_frame, text="Fecha de Publicación:", font=('arial', 12, 'bold'), bg="#CACFD2").grid(row=5, column=0, padx=10, pady=5, sticky="e")
        self.entry_fecha_publicacion = DateEntry(form_frame, font=('arial', 12, 'bold'), date_pattern='yyyy-mm-dd')  # Usar DateEntry para mostrar un calendario
        self.entry_fecha_publicacion.grid(row=5, column=1, padx=10, pady=5, sticky="w")

        Label(form_frame, text="ID Categoría:", font=('arial', 12, 'bold'), bg="#CACFD2").grid(row=6, column=0, padx=10, pady=5, sticky="e")
        self.entry_id_categoria = Entry(form_frame, font=('arial', 12, 'bold'))
        self.entry_id_categoria.grid(row=6, column=1, padx=10, pady=5, sticky="w")

        Label(form_frame, text="Edición:", font=('arial', 12, 'bold'), bg="#CACFD2").grid(row=7, column=0, padx=10, pady=5, sticky="e")
        self.entry_edicion = Entry(form_frame, font=('arial', 12, 'bold'))
        self.entry_edicion.grid(row=7, column=1, padx=10, pady=5, sticky="w")

        Label(form_frame, text="Número de Páginas:", font=('arial', 12, 'bold'), bg="#CACFD2").grid(row=8, column=0, padx=10, pady=5, sticky="e")
        self.entry_numero_paginas = Entry(form_frame, font=('arial', 12, 'bold'))
        self.entry_numero_paginas.grid(row=8, column=1, padx=10, pady=5, sticky="w")

        Label(form_frame, text="Número de Copias:", font=('arial', 12, 'bold'), bg="#CACFD2").grid(row=9, column=0, padx=10, pady=5, sticky="e")
        self.entry_numero_copias = Entry(form_frame, font=('arial', 12, 'bold'))
        self.entry_numero_copias.grid(row=9, column=1, padx=10, pady=5, sticky="w")

        Label(form_frame, text="Copias Disponibles:", font=('arial', 12, 'bold'), bg="#CACFD2").grid(row=10, column=0, padx=10, pady=5, sticky="e")
        self.entry_copias_disponibles = Entry(form_frame, font=('arial', 12, 'bold'))
        self.entry_copias_disponibles.grid(row=10, column=1, padx=10, pady=5, sticky="w")

        # Botón de envío
        self.boton_enviar = Button(form_frame, text="Enviar", font=('arial', 12, 'bold'), command=self.enviar_formulario)
        self.boton_enviar.grid(row=11, column=1, pady=10, sticky="e")

    def enviar_formulario(self):
        libro = LibroDAO(
            self.entry_titulo.get(),
            self.entry_isbn.get(),
            self.entry_autor.get(),
            self.entry_editorial.get(),
            self.entry_fecha_publicacion.get(),
            int(self.entry_id_categoria.get()),
            int(self.entry_edicion.get()),
            int(self.entry_numero_paginas.get()),
            int(self.entry_numero_copias.get()),
            int(self.entry_copias_disponibles.get())
        )
        try:
            libro.set_libro()
            ms.showinfo("Éxito", "Libro insertado correctamente")
        except Exception as e:
            ms.showerror("Error", f"Error al insertar el libro: {e}")

if __name__ == '__main__':
    raiz = Tk()
    aplicacion = RegistrarLibro(raiz)
    raiz.mainloop()
