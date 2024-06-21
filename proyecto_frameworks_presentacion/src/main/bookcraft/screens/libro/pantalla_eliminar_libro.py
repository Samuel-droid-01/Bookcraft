from tkinter import *
from proyecto_frameworks_persistencia.src.main.bookcraft.dao.libro.libroDAO import LibroDAO
from tkinter import messagebox as ms

class EliminarLibro:
    def __init__(self,raiz):
        self.raiz = raiz
        self.raiz.title("Sistema de biblioteca Bookcraft")
        
        # Configurar geometría y fondo
        geometría = "600x600+220+220"
        self.raiz.geometry(geometría)
        self.raiz.configure(background='black')

        # Marco principal
        self.MarcoPrincipal = Frame(self.raiz)
        self.MarcoPrincipal.pack(fill=BOTH, expand=True)

        self.lblTitulo = Label(self.MarcoPrincipal, font=('arial', 24, 'bold'), text="Bookcraft Library System", bg="black", fg="white")
        self.lblTitulo.pack(side=TOP, fill=X)
        
        self.lblTitulo2 = Label(self.MarcoPrincipal, font=('arial', 24, 'bold'), text="Eliminar Libro")
        self.lblTitulo2.pack(side=TOP, fill=X)
        
        # Marco para detalles de contenido
        self.MarcoDetallesLector = LabelFrame(self.MarcoPrincipal, bd=20, pady=5, relief=RIDGE, bg="#B9BED3")#Aqui va el contenido
        self.MarcoDetallesLector.pack(side=BOTTOM, fill=BOTH, expand=True)

        self.fuente=("Arial", 14)
        self.lblTitulo = Label(self.MarcoDetallesLector, text="Ingrese el ISBN o nombre del libro:", bg="#B9BED3", font=self.fuente)
        self.lblTitulo.grid(row=0, column=0, padx=10, pady=10)

        self.txtTitulo = Entry(self.MarcoDetallesLector, font=self.fuente)
        self.txtTitulo.grid(row=0, column=1, padx=10, pady=10)
        self.txtTitulo.focus_set()

        self.btnBuscar = Button(self.MarcoDetallesLector, text="Buscar", font=self.fuente, command=self.buscar_libro)
        self.btnBuscar.grid(row=0, column=2, padx=10, pady=10)
        self.btnEliminar = Button(self.MarcoDetallesLector, text="Eliminar", font=self.fuente, command=self.eliminar_libro)
        self.btnEliminar.grid(row=0, column=3, padx=10, pady=10)

    def buscar_libro(self):
        cadena=self.txtTitulo.get()
        if len(cadena)==17:#Si es un ISBN
            #print("ISBN")
            libro = LibroDAO().get_libro_by_isbn(cadena)
        elif len(cadena)>0:
            libro = LibroDAO().filtrar_titulo(cadena)
        else:
            ms.showerror("Error","Ingrese un ISBN o nombre de libro")
            return
        if  libro[0]:#caso de 1 solo libro
            aux=libro[1]
            if type(libro[1])!=list:
                aux= [libro[1]]#Se convierte en lista
            for i,j in enumerate(aux):
                libroFrame = Frame(self.MarcoDetallesLector, bg="#CACFD2")
                libroFrame.grid(row=i+1, column=0, padx=10, pady=10)

                lblTitulo = Label(libroFrame, text="Titulo:", bg="#CACFD2", anchor="w", width=20)
                lblTitulo.grid(row=0, column=0)
                lblTitulo = Label(libroFrame, text=j.get_titulo(), bg="#CACFD2", anchor="w", width=20)
                lblTitulo.grid(row=0, column=1)

                lblAutor = Label(libroFrame, text="Autor:", bg="#CACFD2", anchor="w", width=20)
                lblAutor.grid(row=1, column=0)
                lblAutor = Label(libroFrame, text=j.get_autor(), bg="#CACFD2", anchor="w", width=20)
                lblAutor.grid(row=1, column=1)

                lblEditorial = Label(libroFrame, text="Editorial:", bg="#CACFD2", anchor="w", width=20)
                lblEditorial.grid(row=2, column=0)
                lblEditorial = Label(libroFrame, text=j.get_editorial(), bg="#CACFD2", anchor="w", width=20)
                lblEditorial.grid(row=2, column=1)

                lblCopias = Label(libroFrame, text="Copias disponibles:", bg="#CACFD2", anchor="w", width=20)
                lblCopias.grid(row=3, column=0)
                lblCopias = Label(libroFrame, text=j.get_copias_disponibles(), bg="#CACFD2", anchor="w", width=20)
                lblCopias.grid(row=3, column=1)

                

        else:
            ms.showerror("Error","No se encontró el libro")
            return


    def eliminar_libro(self):
        pass
