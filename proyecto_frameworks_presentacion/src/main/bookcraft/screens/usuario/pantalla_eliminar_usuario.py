from proyecto_frameworks_persistencia.src.main.bookcraft.dao.administrador.administradorDAO import AdministradorDAO
from tkinter import *
from tkinter import messagebox as ms

class EliminarUsuario:
    def __init__(self, raiz):
        self.raiz = raiz
        self.raiz.title("Sistema de biblioteca Bookcraft")
        
        # Configurar geometría y fondo
        geometria = "600x300+220+200"
        self.raiz.geometry(geometria)
        self.raiz.configure(background='#CACFD2')
        
        # Variables para almacenar la opción seleccionada
        self.opcion_seleccionada = StringVar()
        self.opcion_seleccionada.set("aceptar")  # Valor por defecto

        # Marco principal
        self.MarcoPrincipal = Frame(self.raiz, bg='#CACFD2')
        self.MarcoPrincipal.pack(fill=BOTH, expand=True)

        self.lblTitulo = Label(self.MarcoPrincipal, font=('arial', 24, 'bold'), text="Bookcraft Library System", bg="black", fg="white")
        self.lblTitulo.pack(side=TOP, fill=X)
        
        self.lblTitulo2 = Label(self.MarcoPrincipal, font=('arial', 24, 'bold'), text="Eliminar Usuario", bg='#CACFD2')
        self.lblTitulo2.pack(side=TOP, fill=X)
        
        # Filtrar búsqueda
        self.MarcoBusqueda = Frame(self.MarcoPrincipal, bd=0, relief=RIDGE, bg='#CACFD2')
        self.MarcoBusqueda.pack(side=TOP, fill=X, padx=10, pady=10)

        lblFiltrar = Label(self.MarcoBusqueda, text="Eliminar usuario por id:", font=('arial', 12, 'bold'), bg='#CACFD2')
        lblFiltrar.grid(row=0, column=0, padx=10, pady=10, sticky=W)

        self.entryBusqueda = Entry(self.MarcoBusqueda, font=('arial', 12))
        self.entryBusqueda.grid(row=0, column=1, padx=10, pady=10)

        btnBuscar = Button(self.MarcoBusqueda, padx=10, pady=5, bd=5, font=('arial', 9, 'bold'), text='Eliminar', bg="#2E4053", fg="white", command=self.buscar_y_eliminar_usuario)
        btnBuscar.grid(row=0, column=2, padx=10, pady=10)

        # Opciones de eliminación
        self.MarcoOpciones = Frame(self.MarcoPrincipal, bd=0, relief=RIDGE, bg='#CACFD2')
        self.MarcoOpciones.pack(side=TOP, pady=10)

        self.opcion_aceptar = Radiobutton(self.MarcoOpciones, text="Aceptar", variable=self.opcion_seleccionada, value="aceptar", font=('arial', 12, 'bold'), bg='#CACFD2')
        self.opcion_aceptar.pack(anchor=E, padx=10, pady=5)

        self.opcion_cancelar = Radiobutton(self.MarcoOpciones, text="Cancelar", variable=self.opcion_seleccionada, value="cancelar", font=('arial', 12, 'bold'), bg='#CACFD2')
        self.opcion_cancelar.pack(anchor=E, padx=10, pady=5)

    def limpiar_detalles(self):
        # Limpiar el marco de detalles antes de mostrar nuevos contenidos
        for widget in self.MarcoDetalles.winfo_children():
            widget.destroy()
    
    def buscar_y_eliminar_usuario(self):
        termino = self.entryBusqueda.get()
        if not termino.isdigit():
            ms.showerror("Error", "El ID del usuario debe ser un número.")
            return
        
        usuarioDAO = AdministradorDAO()
        eliminado, mensaje = usuarioDAO.eliminar_usuario(int(termino), self.opcion_seleccionada.get())
        
        if eliminado:
            ms.showinfo("Eliminar", mensaje)
        else:
            ms.showinfo("Eliminar", mensaje)