import tkinter as tk
from tkinter import Canvas, Scrollbar, Frame, Label, BOTH, RIGHT, Y, LEFT

class Aplicacion(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Ejemplo de Scrollbar dentro de un Frame que contiene un Canvas")

        self.MarcoPrincipal = Frame(self)
        self.MarcoPrincipal.pack(fill=BOTH, expand=True)

        self.MarcoDetallesLector = Frame(self.MarcoPrincipal, bd=2, relief="sunken", bg="#B9BED3")
        self.MarcoDetallesLector.pack(fill=BOTH, expand=True)

        # Canvas y scrollbar
        self.canvas = Canvas(self.MarcoDetallesLector, bg="#CACFD2")
        self.canvas.pack(side=LEFT, fill=BOTH, expand=True, padx=10, pady=10)

        self.scrollbar = Scrollbar(self.MarcoDetallesLector, orient="vertical", command=self.canvas.yview)
        self.scrollbar.pack(side=RIGHT, fill=Y)

        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        # Crear un Frame interno dentro del Canvas
        self.scrollable_frame = Frame(self.canvas, bg="#CACFD2")
        self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")

        self.scrollable_frame.bind("<Configure>", self.on_frame_configure)
        self.bind_all("<MouseWheel>", self._on_mousewheel)
        

        # Añadir contenido de ejemplo al Frame interno
        for i in range(50):
            lbl = Label(self.scrollable_frame, text=f"Label {i+1}", bg="#CACFD1", height=2)
            lbl.pack()

    def _on_mousewheel(self, event):
        self.canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")

    def on_frame_configure(self, event):
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))

if __name__ == "__main__":
    app = Aplicacion()
    app.mainloop()
