from tkinter import *
from tkinter import messagebox as ms
from tkcalendar import DateEntry

class PantallaEliminarSancion:
    def __init__(self, raiz, sanciones):
        self.raiz = raiz
        self.sanciones = sanciones
        self.raiz.title("Eliminar Sanción - Bookcraft Library System")
        
        # Configurar geometría y fondo
        geometria = "450x200+220+200"
        self.raiz.geometry(geometria)
        self.raiz.configure(background='black')

        # Marco principal
        self.MarcoPrincipal = Frame(self.raiz)
        self.MarcoPrincipal.pack(fill=BOTH, expand=True)

        self.lblTitulo = Label(self.MarcoPrincipal, font=('arial', 24, 'bold'), text="Eliminar Sanción", bg="black", fg="white")
        self.lblTitulo.pack(side=TOP, fill=X)

        # Marco para el contenido
        self.MarcoContenido = Frame(self.MarcoPrincipal, bg="#B9BED3", pady=20)
        self.MarcoContenido.pack(fill=BOTH, expand=True)

        self.lblID = Label(self.MarcoContenido, text="ID de la Sanción:", bg="#B9BED3")
        self.lblID.pack(side=LEFT, padx=10)

        self.id_entry = Entry(self.MarcoContenido)
        self.id_entry.pack(side=LEFT, padx=10)

        self.btnEliminar = Button(self.MarcoContenido, text="Eliminar", command=self.eliminar_sancion)
        self.btnEliminar.pack(side=LEFT, padx=10)

    def eliminar_sancion(self):
        sancion_id = self.id_entry.get()
        
        if not sancion_id.isdigit():
            ms.showerror("Error", "Por favor, ingrese un ID válido")
            return

        sancion_id = int(sancion_id)
        sancion_encontrada = False

        for sancion in self.sanciones:
            if sancion['id'] == sancion_id:
                self.sanciones.remove(sancion)
                sancion_encontrada = True
                break

        if sancion_encontrada:
            ms.showinfo("Éxito", f"La sanción con ID {sancion_id} ha sido eliminada.")
        else:
            ms.showerror("Error", f"No se encontró ninguna sanción con ID {sancion_id}.")

if __name__ == "__main__":
    root = Tk()
    sanciones = [
        {'id': 1, 'nombre': 'Juan Pérez', 'fecha_inicio': '2023-01-01', 'fecha_fin': '2023-01-10', 'descripcion': 'Retraso en la devolución de libros'},
        {'id': 2, 'nombre': 'Ana Gómez', 'fecha_inicio': '2023-02-15', 'fecha_fin': '2023-02-20', 'descripcion': 'Daño en material bibliográfico'},
        {'id': 3, 'nombre': 'Luis Martínez', 'fecha_inicio': '2023-03-05', 'fecha_fin': '2023-03-15', 'descripcion': 'Pérdida de libros'},
        {'id': 4, 'nombre': 'María Rodríguez', 'fecha_inicio': '2023-04-01', 'fecha_fin': '2023-04-10', 'descripcion': 'Uso inapropiado de instalaciones'},
        {'id': 5, 'nombre': 'Carlos López', 'fecha_inicio': '2023-05-01', 'fecha_fin': '2023-05-10', 'descripcion': 'Comportamiento inapropiado'},
    ]
    app = PantallaEliminarSancion(root, sanciones)
    root.mainloop()
