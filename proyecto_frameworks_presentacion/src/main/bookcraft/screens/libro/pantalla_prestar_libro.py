from tkinter import *
from tkinter import ttk
from tkinter import messagebox as ms
from tkcalendar import DateEntry
import os
from PIL import Image, ImageTk
from datetime import datetime
from proyecto_frameworks_persistencia.src.main.bookcraft.bd.domain.libro import Libro
from proyecto_frameworks_persistencia.src.main.bookcraft.dao.libro.libroDAO import LibroDAO
from proyecto_frameworks_persistencia.src.main.bookcraft.dao.lector.lectorDAO import LectorDAO
from proyecto_frameworks_persistencia.src.main.bookcraft.dao.usuario.usuarioDAO import UsuarioDAO
from proyecto_frameworks_persistencia.src.main.bookcraft.bd.mappers.usuario.usuario_map import UsuarioMapper

from proyecto_frameworks_persistencia.src.main.bookcraft.bd.mappers.categoria.categoria_map import CategoriaMapper
class PantallaPrestarLibro():
    def __init__(self,raiz) :
        self.raiz = raiz
        self.raiz.title("Sistema de biblioteca Bookcraft")
        # Configurar geometría y fondo
        geometria = "775x450+320+200"
        self.raiz.geometry(geometria)
        self.raiz.configure(background='black')

        # Marco principal
        self.MarcoPrincipal = Frame(self.raiz)
        self.MarcoPrincipal.pack(fill=BOTH, expand=True)

        Superior = Frame(self.MarcoPrincipal, bd=0, relief=RIDGE, bg="black")
        Superior.pack(side=TOP, fill=X)

        # Configurar columnas para distribuir los elementos en la parte superior
        Superior.columnconfigure(0, weight=1)
        Superior.columnconfigure(1, weight=1)

        # Imagen y texto "Lector" en la parte superior izquierda
        img_path = "proyecto_frameworks_presentacion/src/main/bookcraft/img/lectura-de-libros.png"
        if os.path.exists(img_path):
            # Redimensionar la imagen
            img = Image.open(img_path)
            img = img.resize((50, 50), Image.LANCZOS)  # Redimensionar a 50x50 píxeles
            self.imgLector = ImageTk.PhotoImage(img)
            self.lblLector = Label(Superior, image=self.imgLector, text="Lector", compound=LEFT, font=('arial', 18, 'bold'), fg="white", bg="black")
        else:
            self.lblLector = Label(Superior, text="Admin", font=('arial', 18, 'bold'), fg="white")
            ms.showerror("Error", f"No se pudo encontrar el archivo de imagen: {img_path}")

        self.lblLector.grid(row=0, column=0, sticky=W)

        # Título debajo de la línea con el botón de logout
        self.lblTitulo = Label(self.MarcoPrincipal, font=('arial', 24, 'bold'), text="Prestar Libro")
        self.lblTitulo.pack(side=TOP, fill=X, pady=10)

        # Botón de logout en la parte superior derecha
        self.btnLogout = Button(Superior, text="Logout", font=('arial', 12, 'bold'),command=self.logout)
        self.btnLogout.grid(row=0, column=1, sticky=E)

        # Barra de navegación
        self.BarraNavegacion = Frame(self.MarcoPrincipal, bd=0, relief=RIDGE)
        self.BarraNavegacion.pack(side=TOP, fill=X)  # Fill X para expandirse horizontalmente

        self.MarcoDetallesLector = LabelFrame(self.MarcoPrincipal, bd=20, pady=5, relief=RIDGE, bg="#B9BED3")
        self.MarcoDetallesLector.pack(side=BOTTOM, fill=BOTH, expand=True)

        self.MarcoDetalles = Frame(self.MarcoDetallesLector, bd=10, relief=RIDGE, bg="#CACFD2")
        self.MarcoDetalles.pack(side=LEFT, fill=BOTH, expand=True)

        self.tituloLabel= Label(self.MarcoDetalles, text="ISBN del libro", bg="#CACFD2", anchor="w", width=15)  
        self.tituloLabel.place(x=10,y=10)


        self.tituloEntry=Entry(self.MarcoDetalles,width=15,bg="#CACFD2")
        self.tituloEntry.place(x=130,y=10)
        self.tituloEntry.focus_set()

        self.nombreLabel= Label(self.MarcoDetalles, text="id del lector", bg="#CACFD2", anchor="w", width=15)  
        self.nombreLabel.place(x=10,y=60)


        self.nombreEntry=Entry(self.MarcoDetalles,width=15,bg="#CACFD2")
        self.nombreEntry.place(x=130,y=60)


        self.fechaInicioLabel= Label(self.MarcoDetalles,text="Fecha préstamo", bg="#CACFD2",anchor="w", width=15)  
        self.fechaInicioLabel.place(x=10,y=110)

        self.fechaInicioEntry=Entry(self.MarcoDetalles,width=15,bg="#CACFD2")
        self.fechaInicioEntry.place(x=130,y=110)
        self.fechaInicioEntry.insert(0,datetime.now().strftime("%Y-%m-%d"))

        self.fechaFinLabel= Label(self.MarcoDetalles,text="Fecha devolución", bg="#CACFD2",anchor="w", width=15)
        self.fechaFinLabel.place(x=10,y=160)


        self.fechaFinEntry=DateEntry(self.MarcoDetalles,width=15,bg="#CACFD2",date_pattern='yyyy-mm-dd')
        self.fechaFinEntry.place(x=130,y=160)

        self.btnPrestar = Button(self.MarcoDetalles, text="Continuar", font=('arial', 10, 'bold'),command=lambda: self.continuar(self.MarcoDetalles,self.btnPrestar))
        self.btnPrestar.place(x=130,y=210)

        self.btnCancelar = Button(self.MarcoDetalles, text="Cancelar", font=('arial', 10, 'bold'),command=self.limpiar)
        self.btnCancelar.place(x=10,y=210)
        
    def continuar(self,frame,boton):
        libro=LibroDAO().get_libro_by_id(self.tituloEntry.get())#retorna un objeto libro
        lector=UsuarioMapper().get_by_id(self.nombreEntry.get())#retorna un objeto usuario
        lectorDAO=LectorDAO()
        lectorDAO.set_usuario(lector)
        #
        if not self.verificarEntradas():
            return
        if libro is None or lector is None:
            ms.showerror("Error", "El libro o el lector no existen")
            return
        #comprobar si el libro esta disponible
        if libro.get_copias_disponibles()<1:#al menos una copia disponible
            ms.showerror("Error", "El libro no está disponible")
            return
        
        boton.config(text="Realizar préstamo",command=lambda: self.realizarPrestamo(frame,lectorDAO))
        self.resumenFrame = Frame(frame, bd=10, relief=RIDGE, width=400,height=250,bg="#E6E5E4")
        self.resumenFrame.place(x=300,y=10)
        self.resumenLabel= Label(self.resumenFrame, text="Resumen de préstamo", bg="#E6E5E4", font=('arial', 12, 'bold'), anchor="center")
        self.resumenLabel.place(x=10,y=10)

        self.isbnLabel= Label(self.resumenFrame, text=f"ISBN: {libro.get_id()}", bg="#E6E5E4", anchor="w", width=15)
        self.isbnLabel.place(x=10,y=40)

        self.tituloLabel= Label(self.resumenFrame, text=f"Titulo {libro.get_titulo()}", bg="#E6E5E4", anchor="w", width=50)
        self.tituloLabel.place(x=10,y=70)

        self.categoriaLabel= Label(self.resumenFrame, text=f"Categoría: {CategoriaMapper().get_categoria(libro.get_id_categoria())}", bg="#E6E5E4", anchor="w", width=20)
        self.categoriaLabel.place(x=10,y=100)

        self.autorLabel= Label(self.resumenFrame, text=f"Autor: {libro.get_autor()}", bg="#E6E5E4", anchor="w", width=30)
        self.autorLabel.place(x=10,y=130)

        self.nombreLabel= Label(self.resumenFrame, text=f"Nombre del lector: {lector.get_nombres()+" "+lector.get_apellidos()}", bg="#E6E5E4", anchor="w", width=50)
        self.nombreLabel.place(x=10,y=160)

        self.fechaInicioLabel= Label(self.resumenFrame,text=f"Fecha préstamo: {self.fechaInicioEntry.get()}", bg="#E6E5E4",anchor="w", width=22)
        self.fechaInicioLabel.place(x=10,y=190)

        self.fechaFinLabel= Label(self.resumenFrame,text=f"Fecha devolución: {self.fechaFinEntry.get()}", bg="#E6E5E4",anchor="w", width=22)
        self.fechaFinLabel.place(x=10,y=210)
        
    def realizarPrestamo(self,frame,lectorDAO):
        if self.fechaFinEntry.get()<self.fechaInicioEntry.get():
            ms.showerror("Error", "La fecha de devolución no puede ser anterior a la fecha de préstamo")
            return
        
        resultado=lectorDAO.solicitar_prestamo(self.tituloEntry.get(),self.fechaFinEntry.get(),0,1)
        if resultado[0]:
            ms.showinfo("Éxito", resultado[1])
        else:
            ms.showerror("Error", resultado[1])
        self.limpiar()

    def verificarEntradas(self):
        if self.tituloEntry.get()=="" or self.nombreEntry.get()=="" or self.fechaInicioEntry.get()=="" or self.fechaFinEntry.get()=="":
            ms.showerror("Error", "Todos los campos son requeridos")
            return False
        return True

    def limpiar(self):
        self.tituloEntry.delete(0,END)
        self.nombreEntry.delete(0,END)
        self.fechaInicioEntry.delete(0,END)
        self.fechaFinEntry.delete(0,END)
        self.resumenFrame.destroy()
        self.btnPrestar.config(text="Continuar",command=lambda: self.continuar(self.MarcoDetalles,self.btnPrestar))
        self.tituloEntry.focus_set()
        self.fechaInicioEntry.insert(0,datetime.now().strftime("%Y-%m-%d"))

    def logout(self):
        ms.showinfo("Logout", "Sesión cerrada exitosamente.")
        self.raiz.quit()

if __name__ == '__main__':
    raiz = Tk()
    aplicacion = PantallaPrestarLibro(raiz)
    raiz.mainloop()