from tkinter import *
from tkinter import messagebox as ms
from tkcalendar import DateEntry
from proyecto_frameworks_persistencia.src.main.bookcraft.dao.sancion.sancionDAO import SancionDAO

class PantallaListarLectoresSancionados:
    def __init__(self, raiz):
        self.raiz = raiz
        self.raiz.title("Sistema de biblioteca Bookcraft")
        
        # Configurar geometría y fondo
        geometria = "500x400+220+200"
        self.raiz.geometry(geometria)
        self.raiz.configure(background='black')

        # Marco principal
        self.MarcoPrincipal = Frame(self.raiz)
        self.MarcoPrincipal.pack(fill=BOTH, expand=True)

        self.lblTitulo = Label(self.MarcoPrincipal, font=('arial', 24, 'bold'), text="Bookcraft Library System", bg="black", fg="white")
        self.lblTitulo.pack(side=TOP, fill=X)
        
        self.lblTitulo2 = Label(self.MarcoPrincipal, font=('arial', 24, 'bold'), text="Sanciones")
        self.lblTitulo2.pack(side=TOP, fill=X)

        # Barra de navegación
        self.BarraNavegacion = Frame(self.MarcoPrincipal, bd=0, relief=RIDGE)
        self.BarraNavegacion.pack(side=TOP, fill=X)  # Fill X para expandirse horizontalmente

        # Agregar entrada de fecha y botón de filtro
        self.MarcoFiltro = Frame(self.BarraNavegacion, bg="#B9BED3")
        self.MarcoFiltro.pack(side=LEFT, padx=10, pady=10)
        
        self.lblFecha = Label(self.MarcoFiltro, text="Seleccionar Fecha:", bg="#B9BED3")
        self.lblFecha.pack(side=LEFT, padx=5)

        self.date_entry = DateEntry(self.MarcoFiltro, date_pattern='yyyy-mm-dd')
        self.date_entry.pack(side=LEFT, padx=5)

        self.btnFiltrar = Button(self.MarcoFiltro, text="Aplicar", command=self.filtrar_sanciones)
        self.btnFiltrar.pack(side=LEFT, padx=5)

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

        # Lista de sanciones de ejemplo
        """self.sanciones = [
            {'nombre': 'Juan Pérez', 'fecha_inicio': '2023-01-01', 'fecha_fin': '2023-01-10', 'descripcion': 'Retraso en la devolución de libros'},
            {'nombre': 'Ana Gómez', 'fecha_inicio': '2023-02-15', 'fecha_fin': '2023-02-20', 'descripcion': 'Daño en material bibliográfico'},
            {'nombre': 'Luis Martínez', 'fecha_inicio': '2023-03-05', 'fecha_fin': '2023-03-15', 'descripcion': 'Pérdida de libros'},
            {'nombre': 'María Rodríguez', 'fecha_inicio': '2023-04-01', 'fecha_fin': '2023-04-10', 'descripcion': 'Uso inapropiado de instalaciones'},
            {'nombre': 'Carlos López', 'fecha_inicio': '2023-05-01', 'fecha_fin': '2023-05-10', 'descripcion': 'Comportamiento inapropiado'},
        ]"""
        sancionDAO = SancionDAO()
        self.sanciones = sancionDAO.obtener_sanciones()

        # Mostrar tarjetas de sanciones
        self.mostrar_sanciones(self.sanciones)

    def limpiar_detalles(self):
        # Limpiar el marco de detalles antes de mostrar nuevos contenidos
        for widget in self.MarcoDetalles.winfo_children():
            widget.destroy()

    def mostrar_sanciones(self, sanciones):
        self.limpiar_detalles()
        
        for index, sancion in enumerate(sanciones):
            frame_sancion = Frame(self.MarcoDetalles, bd=2, relief=SOLID, bg="white", padx=10, pady=10)
            frame_sancion.grid(row=index // 2, column=index % 2, padx=10, pady=10, sticky="nsew")
            
            Label(frame_sancion, text=f"Nombre: {sancion.get_nombre()}", bg="white").pack(anchor="w")
            Label(frame_sancion, text=f"Fecha de Inicio: {sancion.get_fecha_inicio()}", bg="white").pack(anchor="w")
            Label(frame_sancion, text=f"Fecha de Fin: {sancion.get_fecha_fin()}", bg="white").pack(anchor="w")
            Label(frame_sancion, text=f"Descripción: {sancion.get_fecha_fin()}", bg="white").pack(anchor="w")

    def filtrar_sanciones(self):
        fecha_seleccionada = self.date_entry.get_date().strftime('%Y-%m-%d')
        sanciones_filtradas = [s for s in self.sanciones if s['fecha_inicio'] <= fecha_seleccionada <= s['fecha_fin']]

        if sanciones_filtradas:
            self.mostrar_sanciones(sanciones_filtradas)
        else:
            ms.showinfo("Sin sanciones", "Al parecer nadie tiene sanciones en esta fecha")

if __name__ == '__main__':
    raiz = Tk()
    aplicacion = PantallaListarLectoresSancionados(raiz)
    raiz.mainloop()
