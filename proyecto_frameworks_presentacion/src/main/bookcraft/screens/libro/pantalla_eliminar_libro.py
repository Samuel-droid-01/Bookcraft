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

        self.marcoBusqueda = Frame(self.MarcoPrincipal, bd=20, pady=5, bg="#B9BED3",height=100)
        self.marcoBusqueda.pack(side=TOP, fill=X, expand=False)
        
        self.marcoDetalles=Frame(self.MarcoPrincipal, bd=20, pady=5, bg="#B9BED3",height=100, relief=RIDGE)
        self.marcoDetalles.pack(side=BOTTOM, fill=BOTH, expand=True)

        self.canvas = Canvas(self.marcoDetalles, bg="#F1EFED")
        self.canvas.pack(side=LEFT, fill=BOTH, expand=True, padx=10, pady=10)

        self.scrollbar = Scrollbar(self.marcoDetalles, orient="vertical", command=self.canvas.yview)
        self.scrollbar.pack(side="right", fill="y")
        self.canvas.configure(yscrollcommand=self.scrollbar.set)
        self.MarcoDetallesLector = Frame(self.canvas,bg="#F1EFED")
        self.canvas.create_window((0, 0), window=self.MarcoDetallesLector, anchor="nw")
        # Marco para detalles de contenido
        #self.MarcoDetallesLector = LabelFrame(self.canvas, bd=20, pady=5, relief=RIDGE, bg="#B9BED3")#Aqui va el contenido
        #self.MarcoDetallesLector.pack(side=BOTTOM, fill=BOTH, expand=True)
        self.MarcoDetallesLector.bind("<Configure>", self.on_frame_configure)
        self.MarcoDetallesLector.bind_all("<MouseWheel>", self._on_mousewheel)

        self.fuente=("Arial", 14)
        self.lblTitulo = Label(self.marcoBusqueda, text="Ingrese el ISBN o nombre del libro:", bg="#B9BED3", font=self.fuente)
        self.lblTitulo.grid(row=0, column=0, padx=10, pady=10)

        self.txtTitulo = Entry(self.marcoBusqueda, font=self.fuente)
        self.txtTitulo.grid(row=0, column=1, padx=10, pady=10)
        self.txtTitulo.focus_set()

        self.btnBuscar = Button(self.marcoBusqueda, text="Buscar", font=self.fuente, command=self.buscar_libro)
        self.btnBuscar.grid(row=0, column=2, padx=10, pady=10)
        self.btnEliminar = Button(self.marcoBusqueda, text="Eliminar", font=self.fuente, command=self.eliminar_libro)
        self.btnEliminar.grid(row=0, column=3, padx=10, pady=10)

        self.limpiarButton = Button(self.marcoBusqueda, text="Limpiar", font=self.fuente, command=self.limpiar_detalles)
        self.limpiarButton.grid(row=0, column=4, padx=10, pady=10)



        #agregar scrollbar
    def _on_mousewheel(self, event):
        self.canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")

    def on_frame_configure(self, event):
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))

    def limpiar_detalles(self):
        for widget in self.MarcoDetallesLector.winfo_children():
            if  isinstance(widget, Frame):
                widget.destroy()
        self.txtTitulo.delete(0, END)

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
                libroFrame.bind("<Button-1>", self.on_frame_click)#Se agrega evento de click

                lblISBN = Label(libroFrame, text="ISBN:", bg="#CACFD2", anchor="w", width=20)
                lblISBN.grid(row=0, column=0,padx=10, pady=10)
                lblISBN = Label(libroFrame, text=j.get_isbn(), bg="#CACFD2", anchor="w", width=40)
                lblISBN.grid(row=0, column=1)

                lblTitulo = Label(libroFrame, text="Titulo:", bg="#CACFD2", anchor="w", width=20)
                lblTitulo.grid(row=1, column=0)
                lblTitulo = Label(libroFrame, text=j.get_titulo(), bg="#CACFD2", anchor="w", width=40)
                lblTitulo.grid(row=1, column=1)

                lblAutor = Label(libroFrame, text="Autor:", bg="#CACFD2", anchor="w", width=20)
                lblAutor.grid(row=2, column=0)
                lblAutor = Label(libroFrame, text=j.get_autor(), bg="#CACFD2", anchor="w", width=40)
                lblAutor.grid(row=2, column=1)

                lblEditorial = Label(libroFrame, text="Editorial:", bg="#CACFD2", anchor="w", width=20)
                lblEditorial.grid(row=3, column=0)
                lblEditorial = Label(libroFrame, text=j.get_editorial(), bg="#CACFD2", anchor="w", width=40)
                lblEditorial.grid(row=3, column=1)

                lblCopias = Label(libroFrame, text="Copias disponibles:", bg="#CACFD2", anchor="w", width=20)
                lblCopias.grid(row=4, column=0)
                lblCopias = Label(libroFrame, text=j.get_copias_disponibles(), bg="#CACFD2", anchor="w", width=40)
                lblCopias.grid(row=4, column=1)

                #Se agrega evento de click a todos los widgets del frame libroFrame
                for widget in libroFrame.winfo_children():
                     widget.bind("<Button-1>", self.on_frame_click)
                

        else:
            ms.showerror("Error","No se encontró el libro")
            return

    def on_frame_click(self, event):
        frame = event.widget
        i=0
        while not isinstance(frame, Frame):#Se busca el frame padre del widget clickeado que dispara el evento
            frame = frame.master
            
        for widget in frame.winfo_children():
            if  widget.grid_info()['row'] == 0 and widget.grid_info()['column'] == 1:
                self.txtTitulo.delete(0, END)
                self.txtTitulo.insert(0, widget.cget('text'))
                break


    def eliminar_libro(self):
        isbn=self.txtTitulo.get()
        if len(isbn)==0:
            ms.showerror("Error","Ingrese un ISBN")
            return
        LibroDAO().delete_libro_by_isbn(isbn)
        ms.showinfo("Información","Libro eliminado correctamente")
        self.txtTitulo.delete(0, END)
        self.limpiar_detalles()

