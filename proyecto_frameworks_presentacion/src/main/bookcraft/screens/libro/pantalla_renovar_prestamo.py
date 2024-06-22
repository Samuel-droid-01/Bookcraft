from proyecto_frameworks_persistencia.src.main.bookcraft.dao.libro.libroDAO import LibroDAO
from proyecto_frameworks_persistencia.src.main.bookcraft.dao.prestamo.prestamoDAO import PrestamoDAO
from proyecto_frameworks_persistencia.src.main.bookcraft.dao.sancion.sancionDAO import SancionDAO
from proyecto_frameworks_persistencia.src.main.bookcraft.bd.mappers.usuario.usuario_map import UsuarioMapper
from datetime import datetime

from tkinter import *
from tkinter import messagebox as ms
from tkinter import Label, Frame, Button, SOLID, BOTH
from tkcalendar import Calendar

class PantallaRenovarPrestamo():
    def __init__(self, raiz, id_usuario):
        self.raiz = raiz
        self.id_usuario = id_usuario
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
        
        self.lblTitulo2 = Label(self.MarcoPrincipal, font=('arial', 24, 'bold'), text="Libros")
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
        self.buscar_libro()
    def limpiar_detalles(self):
        # Limpiar el marco de detalles antes de mostrar nuevos contenidos
        for widget in self.MarcoDetalles.winfo_children():
            widget.destroy()
    
    def buscar_libro(self):
        solicitudes=PrestamoDAO()
        IDs=solicitudes.obtener_prestamos_usuario(self.id_usuario)
        dato=[]
      
        for solicitud in IDs:
            
                usuario=UsuarioMapper().get_by_id(self.id_usuario)
                libro=LibroDAO().get_libro_by_id(id=solicitud[1])
                prestamo=PrestamoDAO(id=solicitud[0])
                p=prestamo.get_prestamo()
                
                if p.get_activo() == True and p.get_fecha_devolucion()!=None :
                    informacion = {
                        "idPrestamo": solicitud[0],
                        "idUsuario": self.id_usuario,
                        "idLibro": solicitud[1],
                        "nombre": usuario.get_nombres(),
                        "apellido": usuario.get_apellidos(),
                        "titulo": libro.get_titulo(),
                        "fechaDEV": solicitud[2],
                        "isbn": libro.get_isbn()
                    }
                    dato.append(informacion)
            
            
            
            
      
        if dato:
                self.mostrar_libro(dato)
        else:
            ms.showinfo("Buscar", f"No se le presto nigun el libro")
    def actualizarFechaPrestamo(self,idPrestamo, calendario,fecha_devolucion):
        
        if calendario < fecha_devolucion:
            ms.showerror("Error", "La fecha de devolución no puede ser menor a la fecha actual.")
            self.buscar_libro()
            return
        else:
            prestamoDAO = PrestamoDAO(id=idPrestamo)
            prestamo=prestamoDAO.get_prestamo()
            prestamo.set_fecha_devolucion(calendario)
            
            prestamoDAO.update_prestamo()
            ms.showinfo("Renovar", "Fecha de devolución actualizada con éxito")
            self.buscar_libro()
        

    def mostrar_libro(self, dato):
        self.limpiar_detalles()
        for dat in dato:
            frame_libro = Frame(self.MarcoDetalles, bd=2, relief=SOLID, bg="white", padx=10, pady=10)
            frame_libro.pack(fill=BOTH, expand=True, padx=10, pady=10)
            Label(frame_libro, text=f"Nombre: {dat['nombre']}", bg="white").pack(anchor="w")
            Label(frame_libro, text=f"Apellido: {dat['apellido']}", bg="white").pack(anchor="w")
            Label(frame_libro, text=f"Libro: {dat['titulo']}", bg="white").pack(anchor="w")
            Label(frame_libro, text=f"Fecha de devolución: {dat['fechaDEV']}", bg="white").pack(anchor="w")
            Label(frame_libro, text=f"Isbn: {dat['isbn']}", bg="white").pack(anchor="w")
            Label(frame_libro, text="Nueva Fecha", bg="#2E4053", fg="white", font=('Arial', 12, 'bold'), borderwidth=2, relief="groove").pack(anchor="w", padx=100, pady=5)
            # Crear el calendario para seleccionar la nueva fecha de devolución
            now = datetime.now()
            calendario = Calendar(frame_libro, selectmode='day', year=now.year, month=now.month, day=now.day)
            calendario.pack(pady=10)

            def confirmar_fecha():
                fecha_calendario_str = calendario.get_date()  # Obtener la fecha como string
                fecha_calendario = datetime.strptime(fecha_calendario_str, '%d/%m/%y')  # Ajustar el formato a día/mes/año abreviado
                fecha_devolucion = datetime.combine(dat['fechaDEV'], datetime.min.time())
             
                # Aquí puedes llamar a actualizarFechaPrestamo directamente o establecer las variables necesarias para hacerlo después
                self.actualizarFechaPrestamo(dat["idPrestamo"], fecha_calendario, fecha_devolucion)

            # Botón para confirmar la selección de la fecha
            Button(frame_libro, text="Confirmar fecha", command=confirmar_fecha).pack(pady=10)

            
            