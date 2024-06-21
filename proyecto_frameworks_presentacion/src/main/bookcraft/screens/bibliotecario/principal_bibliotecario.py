# -------para libros-----
from proyecto_frameworks_presentacion.src.main.bookcraft.screens.libro.pantalla_listar_libro import ListarLibro
from proyecto_frameworks_presentacion.src.main.bookcraft.screens.libro.pantalla_actualizar_libro import ActualizarLibro
from proyecto_frameworks_presentacion.src.main.bookcraft.screens.libro.pantalla_registrar_libro import RegistrarLibro
from proyecto_frameworks_presentacion.src.main.bookcraft.screens.libro.pantalla_ver_informacion_libro import InformacionLibro
from proyecto_frameworks_presentacion.src.main.bookcraft.screens.libro.pantalla_eliminar_libro import EliminarLibro

# -------para sanciones-----
from proyecto_frameworks_presentacion.src.main.bookcraft.screens.sancion.pantalla_ver_sancion import PantallaIDSancion
from proyecto_frameworks_presentacion.src.main.bookcraft.screens.sancion.pantalla_listar_lectores_sancionados import PantallaListarLectoresSancionados

from tkinter import *
from tkinter import messagebox as ms
import os
from PIL import Image, ImageTk
from pathlib import Path

# Clase principal
class PrincipalBibliotecario:
    def __init__(self, raiz):
        self.raiz = raiz
        self.raiz.title("Sistema de biblioteca Bookcraft")
        
        # Configurar geometría y fondo
        geometria = "775x450+320+200"
        self.raiz.geometry(geometria)
        self.raiz.configure(background='black')

        # Marco principal
        self.MarcoPrincipal = Frame(self.raiz)
        self.MarcoPrincipal.pack(fill=BOTH, expand=True)

        # Parte superior con imagen y botón de logout
        Superior = Frame(self.MarcoPrincipal, bd=0, relief=RIDGE, bg="black")
        Superior.pack(side=TOP, fill=X)

        # Configurar columnas para distribuir los elementos en la parte superior
        Superior.columnconfigure(0, weight=1)
        Superior.columnconfigure(1, weight=1)

        # Imagen y texto "Lector" en la parte superior izquierda
        # Obtener la ruta del directorio donde se encuentra el script actual
        script_dir = Path(__file__).parent

        # Construir la ruta relativa a partir de la ubicación del script actual
        # IMPORTANTE: EJECUTAR DESDE BOOKCRATF
        img_path = "proyecto_frameworks_presentacion/src/main/bookcraft/img/lectura-de-libros.png"
        if os.path.exists(img_path):
            # Redimensionar la imagen
            img = Image.open(img_path)
            img = img.resize((50, 50), Image.LANCZOS)  # Redimensionar a 50x50 píxeles
            self.imgLector = ImageTk.PhotoImage(img)
            self.lblLector = Label(Superior, image=self.imgLector, text="Bibliotecario", compound=LEFT, font=('arial', 18, 'bold'), fg="white", bg="black")
        else:
            self.lblLector = Label(Superior, text="Lector", font=('arial', 18, 'bold'), fg="white")
            ms.showerror("Error", f"No se pudo encontrar el archivo de imagen: {img_path}")

        self.lblLector.grid(row=0, column=0, sticky=W)

        # Título debajo de la línea con el botón de logout
        self.lblTitulo = Label(self.MarcoPrincipal, font=('arial', 24, 'bold'), text="Bookcraft Library System")
        self.lblTitulo.pack(side=TOP, fill=X, pady=10)

        # Botón de logout en la parte superior derecha
        self.btnLogout = Button(Superior, text="Logout", font=('arial', 12, 'bold'), command=self.logout)
        self.btnLogout.grid(row=0, column=1, sticky=E)

        # Barra de navegación
        self.BarraNavegacion = Frame(self.MarcoPrincipal, bd=0, relief=RIDGE)
        self.BarraNavegacion.pack(side=TOP, fill=X)  # Fill X para expandirse horizontalmente

        # Configurar columnas para que se expandan uniformemente
        for i in range(4):
            self.BarraNavegacion.grid_columnconfigure(i, weight=1)

        # Botones de navegación

        self.btnLibros = Button(self.BarraNavegacion, padx=10, pady=5, bd=5, font=('arial', 9, 'bold'), text='Libros', bg="#B9BED3", width=10, command=self.mostrar_libros)
        self.btnLibros.grid(row=0, column=0, sticky='nsew', padx=5, pady=5)

        self.btnSanciones = Button(self.BarraNavegacion, padx=10, pady=5, bd=5, font=('arial', 9, 'bold'), text='Sanciones', bg="#B9BED3", command=self.mostrar_sanciones)
        self.btnSanciones.grid(row=0, column=1, sticky='nsew', padx=5, pady=5)

        self.btnPrestamos = Button(self.BarraNavegacion, padx=10, pady=5, bd=5, font=('arial', 9, 'bold'), text='Préstamos', bg="#B9BED3", command=self.mostrar_prestamos)
        self.btnPrestamos.grid(row=0, column=2, sticky='nsew', padx=5, pady=5)

        self.btnCategoria = Button(self.BarraNavegacion, padx=10, pady=5, bd=5, font=('arial', 9, 'bold'), text='Categoría', bg="#B9BED3", command=self.mostrar_categoria)
        self.btnCategoria.grid(row=0, column=3, sticky='nsew', padx=5, pady=5)


        # Marco para detalles de contenido
        self.MarcoDetallesLector = LabelFrame(self.MarcoPrincipal, bd=20, pady=5, relief=RIDGE, bg="#B9BED3")
        self.MarcoDetallesLector.pack(side=BOTTOM, fill=BOTH, expand=True)

        self.MarcoDetalles = Frame(self.MarcoDetallesLector, bd=10, relief=RIDGE,bg="#CACFD2")
        self.MarcoDetalles.pack(side=LEFT, fill=BOTH, expand=True)


    def mostrar_libros(self):
        self.limpiar_detalles()
        # Aquí iría la lógica para mostrar los detalles de libros
        btn1 = Button(self.MarcoDetalles, padx=2, pady=2, bd=4, font=('arial', 9, 'bold'), text='Listar Libros', bg="#2E4053",fg="white",command=self.ventana_listar_libros)
        btn1.grid(row=0, column=0, padx=10, pady=10)
        btn2 = Button(self.MarcoDetalles, padx=2, pady=2, bd=4, font=('arial', 9, 'bold'), text="Registrar libros", bg="#2E4053",fg="white",command=self.ventana_registrar_libro)
        btn2.grid(row=0, column=1, padx=10, pady=10)
        btn3 = Button(self.MarcoDetalles, padx=2, pady=2, bd=4, font=('arial', 9, 'bold'), text="Eliminar Libro", bg="#2E4053",fg="white",command=self.ventana_eliminar_libro)
        btn3.grid(row=0, column=2, padx=10, pady=10)
        btn4 = Button(self.MarcoDetalles, padx=2, pady=2, bd=4, font=('arial', 9, 'bold'), text="Ver informacion Libro", bg="#2E4053",fg="white",command=self.ventana_ver_informacion_libro)
        btn4.grid(row=0, column=3, padx=10, pady=10)
        btn4 = Button(self.MarcoDetalles, padx=2, pady=2, bd=4, font=('arial', 9, 'bold'), text="Actualizar Libro", bg="#2E4053",fg="white",command=self.ventana_actualizar_libro)
        btn4.grid(row=0, column=4, padx=10, pady=10)

    #def mostrar_usuarios(self):
    #    self.limpiar_detalles()
    #    # Aquí iría la lógica para mostrar los detalles de usuarios
    #    btn1 = Button(self.MarcoDetalles, padx=2, pady=2, bd=4, font=('arial', 9, 'bold'), text="Crear Usuario", bg="#2E4053",fg="white")
    #    btn1.grid(row=0, column=0, padx=10, pady=10)
    #    btn2 = Button(self.MarcoDetalles, padx=2, pady=2, bd=4, font=('arial', 9, 'bold'), text="Editar Usuario", bg="#2E4053",fg="white")
    #    btn2.grid(row=0, column=1, padx=10, pady=10)
    #    btn3 = Button(self.MarcoDetalles, padx=2, pady=2, bd=4, font=('arial', 9, 'bold'), text="Eliminar Usuario", bg="#2E4053",fg="white")
    #    btn3.grid(row=0, column=2, padx=10, pady=10)

    def mostrar_sanciones(self):
        self.limpiar_detalles()
        # Aquí iría la lógica para mostrar los detalles de sanciones
        btn1 = Button(self.MarcoDetalles, padx=2, pady=2, bd=4, font=('arial', 9, 'bold'), text="Aplicar Sanción", bg="#2E4053",fg="white")
        btn1.grid(row=0, column=0, padx=10, pady=10)
        btn2 = Button(self.MarcoDetalles, padx=2, pady=2, bd=4, font=('arial', 9, 'bold'), text="Ver Sanción", bg="#2E4053",fg="white", command=self.ventana_ver_sancion)
        btn2.grid(row=0, column=1, padx=10, pady=10)
        btn3 = Button(self.MarcoDetalles, padx=2, pady=2, bd=4, font=('arial', 9, 'bold'), text="Ver Historial", bg="#2E4053",fg="white", command=self.ventana_listar_sanciones)
        btn3.grid(row=0, column=2, padx=10, pady=10)

    def mostrar_prestamos(self):
        self.limpiar_detalles()
        # Aquí iría la lógica para mostrar los detalles de préstamos
        btn1 = Button(self.MarcoDetalles, padx=2, pady=2, bd=4, font=('arial', 9, 'bold'), text="Mostar prestamos", bg="#2E4053",fg="white")
        btn1.grid(row=0, column=0, padx=10, pady=10)
        btn2 = Button(self.MarcoDetalles, padx=2, pady=2, bd=4, font=('arial', 9, 'bold'), text="historial prestamos", bg="#2E4053",fg="white")
        btn2.grid(row=0, column=1, padx=10, pady=10)
        btn3 = Button(self.MarcoDetalles, padx=2, pady=2, bd=4, font=('arial', 9, 'bold'), text="Renovar prestamo", bg="#2E4053",fg="white")
        btn3.grid(row=0, column=2, padx=10, pady=10)

    def mostrar_categoria(self):
        self.limpiar_detalles()
        # Aquí iría la lógica para mostrar los detalles de categoría
        btn1 = Button(self.MarcoDetalles, padx=2, pady=2, bd=4, font=('arial', 9, 'bold'), text="Mostar Categorias", bg="#2E4053",fg="white")
        btn1.grid(row=0, column=0, padx=10, pady=10)
        btn2 = Button(self.MarcoDetalles, padx=2, pady=2, bd=4, font=('arial', 9, 'bold'), text="Eliminar Categoria", bg="#2E4053",fg="white")
        btn2.grid(row=0, column=1, padx=10, pady=10)
        btn3 = Button(self.MarcoDetalles, padx=2, pady=2, bd=4, font=('arial', 9, 'bold'), text="Agregar Categoria", bg="#2E4053",fg="white")
        btn3.grid(row=0, column=2, padx=10, pady=10)

    def limpiar_detalles(self):
        # Limpiar el marco de detalles antes de mostrar nuevos contenidos
        for widget in self.MarcoDetalles.winfo_children():
            widget.destroy()
    
    def ventana_listar_libros(self):
        # Crear una ventana secundaria con Toplevel en lugar de Tk()
        ventana_secundaria = Toplevel(self.raiz)
        ListarLibro(ventana_secundaria)
    
    def ventana_actualizar_libro(self):
        ventana_secundaria = Toplevel(self.raiz)
        ActualizarLibro(ventana_secundaria)
        
    def ventana_registrar_libro(self):
        # Crear una ventana secundaria con Toplevel en lugar de Tk()
        ventana_secundaria = Toplevel(self.raiz)
        RegistrarLibro(ventana_secundaria)
    
    def ventana_ver_informacion_libro(self):
        # Crear una ventana secundaria con Toplevel en lugar de Tk()
        ventana_secundaria = Toplevel(self.raiz)
        InformacionLibro(ventana_secundaria)

    def ventana_eliminar_libro(self):
        # Crear una ventana secundaria con Toplevel en lugar de Tk()
        ventana_secundaria = Toplevel(self.raiz)
        EliminarLibro(ventana_secundaria)

    def ventana_ver_sancion(self):
        # Crear una ventana secundaria con Toplevel en lugar de Tk()
        ventana_secundaria = Toplevel(self.raiz)
        PantallaIDSancion(ventana_secundaria)

    def ventana_listar_sanciones(self):
        ventana_secundaria = Toplevel(self.raiz)
        PantallaListarLectoresSancionados(ventana_secundaria)

    def logout(self):
        ms.showinfo("Logout", "Sesión cerrada exitosamente.")
        self.raiz.quit()
