from proyecto_frameworks_persistencia.src.main.bookcraft.dao.administrador.administradorDAO import AdministradorDAO
from tkinter import *
from tkinter import messagebox as ms

class RegistrarUsuario:
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
        
        self.lblTitulo2 = Label(self.MarcoPrincipal, font=('arial', 24, 'bold'), text="Registrar Usuario")
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

        Label(form_frame, text="Nombres:", font=('arial', 12, 'bold'), bg="#CACFD2").grid(row=1, column=0, padx=10, pady=5, sticky="e")
        self.entry_nombre = Entry(form_frame, font=('arial', 12, 'bold'))
        self.entry_nombre.grid(row=1, column=1, padx=10, pady=5, sticky="w")

        Label(form_frame, text="Apellidos:", font=('arial', 12, 'bold'), bg="#CACFD2").grid(row=2, column=0, padx=10, pady=5, sticky="e")
        self.entry_apellido = Entry(form_frame, font=('arial', 12, 'bold'))
        self.entry_apellido.grid(row=2, column=1, padx=10, pady=5, sticky="w")

        Label(form_frame, text="id_rol:", font=('arial', 12, 'bold'), bg="#CACFD2").grid(row=3, column=0, padx=10, pady=5, sticky="e")
        self.entry_rol = Entry(form_frame, font=('arial', 12, 'bold'))
        self.entry_rol.grid(row=3, column=1, padx=10, pady=5, sticky="w")

        Label(form_frame, text="Correo:", font=('arial', 12, 'bold'), bg="#CACFD2").grid(row=4, column=0, padx=10, pady=5, sticky="e")
        self.entry_correo = Entry(form_frame, font=('arial', 12, 'bold'))
        self.entry_correo.grid(row=4, column=1, padx=10, pady=5, sticky="w")

        Label(form_frame, text="Contraseña:", font=('arial', 12, 'bold'), bg="#CACFD2").grid(row=6, column=0, padx=10, pady=5, sticky="e")
        self.entry_contrasena = Entry(form_frame, font=('arial', 12, 'bold'), show='*')
        self.entry_contrasena.grid(row=6, column=1, padx=10, pady=5, sticky="w")

        # Botón de envío
        self.boton_enviar = Button(form_frame, text="Enviar", font=('arial', 12, 'bold'), command=self.enviar_formulario)
        self.boton_enviar.grid(row=11, column=1, pady=10, sticky="e")

    def enviar_formulario(self):
        usuario = AdministradorDAO()
        try:
            usuario.registrar_usuario(
                self.entry_nombre.get(),
                self.entry_apellido.get(),
                int(self.entry_rol.get()),
                self.entry_correo.get(),
                self.entry_contrasena.get()
            )
            ms.showinfo("Éxito", "Usuario insertado correctamente")
        except Exception as e:
            ms.showerror("Error", f"Error al insertar el Usuario: {e}")
if __name__ == '__main__':
    raiz = Tk()
    aplicacion = RegistrarUsuario(raiz)
    raiz.mainloop()
