from tkinter import *
from tkinter import messagebox as ms

class ActualizarUsuario:
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
        
        Label(form_frame, text="Id:", font=('arial', 12, 'bold'), bg="#CACFD2").grid(row=0, column=0, padx=10, pady=5, sticky="e")
        self.entry_id = Entry(form_frame, font=('arial', 12, 'bold'))
        self.entry_id.grid(row=0, column=1, padx=10, pady=5, sticky="w")

        Label(form_frame, text="Nombres:", font=('arial', 12, 'bold'), bg="#CACFD2").grid(row=1, column=0, padx=10, pady=5, sticky="e")
        self.entry_nombres = Entry(form_frame, font=('arial', 12, 'bold'))
        self.entry_nombres.grid(row=1, column=1, padx=10, pady=5, sticky="w")

        Label(form_frame, text="Apellidos:", font=('arial', 12, 'bold'), bg="#CACFD2").grid(row=2, column=0, padx=10, pady=5, sticky="e")
        self.entry_apellidos = Entry(form_frame, font=('arial', 12, 'bold'))
        self.entry_apellidos.grid(row=2, column=1, padx=10, pady=5, sticky="w")

        Label(form_frame, text="ID Rol:", font=('arial', 12, 'bold'), bg="#CACFD2").grid(row=3, column=0, padx=10, pady=5, sticky="e")
        self.entry_id_rol = Entry(form_frame, font=('arial', 12, 'bold'))
        self.entry_id_rol.grid(row=3, column=1, padx=10, pady=5, sticky="w")

        Label(form_frame, text="Correo:", font=('arial', 12, 'bold'), bg="#CACFD2").grid(row=4, column=0, padx=10, pady=5, sticky="e")
        self.entry_correo = Entry(form_frame, font=('arial', 12, 'bold'))
        self.entry_correo.grid(row=4, column=1, padx=10, pady=5, sticky="w")

        Label(form_frame, text="Contraseña:", font=('arial', 12, 'bold'), bg="#CACFD2").grid(row=5, column=0, padx=10, pady=5, sticky="e")
        self.entry_contrasena = Entry(form_frame, show="*", font=('arial', 12, 'bold'))
        self.entry_contrasena.grid(row=5, column=1, padx=10, pady=5, sticky="w")

        # Botón de envío
        self.boton_enviar = Button(form_frame, text="Enviar", font=('arial', 12, 'bold'), command=self.enviar_formulario)
        self.boton_enviar.grid(row=6, column=1, pady=10, sticky="e")

    def enviar_formulario(self):
        ms.showinfo("Formulario","Usuario registrado")

if __name__ == '__main__':
    raiz = Tk()
    aplicacion = ActualizarUsuario(raiz)
    raiz.mainloop()