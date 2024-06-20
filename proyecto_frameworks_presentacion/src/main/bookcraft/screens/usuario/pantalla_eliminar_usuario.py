from tkinter import *
from tkinter import messagebox as ms


class EliminarUsuario:
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
        
        # Filtrar búsqueda
        self.MarcoBusqueda = Frame(self.MarcoPrincipal, bd=0, relief=RIDGE)
        self.MarcoBusqueda.pack(side=TOP, fill=X, padx=10, pady=10)

        lblFiltrar = Label(self.MarcoBusqueda, text="Ingresa el id del Usuario:", font=('arial', 12, 'bold'))
        lblFiltrar.grid(row=0, column=0, padx=10, pady=10, sticky=W)

        self.entryBusqueda = Entry(self.MarcoBusqueda, font=('arial', 12))
        self.entryBusqueda.grid(row=0, column=2, padx=10, pady=10)

        btnBuscar = Button(self.MarcoBusqueda, padx=10, pady=5, bd=5, font=('arial', 9, 'bold'), text='Buscar', bg="#2E4053",fg="white", command=self.eliminar_usuario)
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
    
    def eliminar_usuario(self):
        criterio = "id"
        termino = self.entryBusqueda.get()
        # Aquí iría la lógica para buscar usuario según el criterio y término
        ms.showinfo("Eliminar", f"Usuario eliminado {criterio}: {termino}")
if __name__ == '__main__':
    raiz = Tk()
    aplicacion = EliminarUsuario(raiz)
    raiz.mainloop()
