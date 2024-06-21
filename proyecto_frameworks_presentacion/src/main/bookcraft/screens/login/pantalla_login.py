from proyecto_frameworks_persistencia.src.main.bookcraft.dao.usuario.usuarioDAO import UsuarioDAO
from tkinter import *
from tkinter import messagebox as ms
from PIL import Image, ImageTk  # Necesario para manejar imágenes

class Login:
    def __init__(self, raiz):
        self.raiz = raiz
        self.raiz.title("Sistema de biblioteca Bookcraft")
        
        # Configurar geometría y fondo
        geometria = "600x300+220+200"
        self.raiz.geometry(geometria)
        self.raiz.configure(background='#CACFD2')
        
        # Marco principal
        self.MarcoPrincipal = Frame(self.raiz, bg='#CACFD2')
        self.MarcoPrincipal.pack(fill=BOTH, expand=True)

        self.lblTitulo = Label(self.MarcoPrincipal, font=('arial', 24, 'bold'), text="Bookcraft Library System", bg="black", fg="white")
        self.lblTitulo.pack(side=TOP, fill=X)
        
        # Marco para la imagen y el formulario de login
        self.MarcoContenido = Frame(self.MarcoPrincipal, bg='#CACFD2')
        self.MarcoContenido.pack(fill=BOTH, expand=True, padx=10, pady=10)

        # Cargar y colocar la imagen
        self.imagen = Image.open("proyecto_frameworks_presentacion/src/main/bookcraft/img/bookcraft.png")  # Reemplaza con la ruta de tu imagen
        self.imagen = self.imagen.resize((200, 200), Image.LANCZOS)  # Corregido el método de reducción
        self.imagen_tk = ImageTk.PhotoImage(self.imagen)

        self.lblImagen = Label(self.MarcoContenido, image=self.imagen_tk, bg='#CACFD2')
        self.lblImagen.grid(row=0, column=0, padx=10, pady=10)

        # Marco para el formulario de login
        self.MarcoLogin = Frame(self.MarcoContenido, bg='#CACFD2')
        self.MarcoLogin.grid(row=0, column=1, padx=10, pady=(50, 10))  # Ajuste del pady

        self.lblCorreo = Label(self.MarcoLogin, text="Correo:", font=('arial', 15, 'bold'), bg='#CACFD2', fg='black')
        self.lblCorreo.grid(row=0, column=0, padx=10, pady=10, sticky=E)

        self.entryCorreo = Entry(self.MarcoLogin, font=('arial', 12))
        self.entryCorreo.grid(row=0, column=1, padx=10, pady=10)

        self.lblContrasena = Label(self.MarcoLogin, text="Contraseña:", font=('arial', 15, 'bold'), bg='#CACFD2', fg='black')
        self.lblContrasena.grid(row=1, column=0, padx=10, pady=10, sticky=E)

        self.entryContrasena = Entry(self.MarcoLogin, font=('arial', 12), show='*')
        self.entryContrasena.grid(row=1, column=1, padx=10, pady=10)

        self.btnLogin = Button(self.MarcoLogin, text="Login", padx=10, pady=5, bd=5, font=('arial', 9, 'bold'), bg="#2E4053", fg="white", command=self.verificar_login)
        self.btnLogin.grid(row=2, columnspan=2, pady=10)

    def verificar_login(self):
        correo = self.entryCorreo.get()
        contrasena = self.entryContrasena.get()
        
        usuarioDAO = UsuarioDAO()
        login_exitoso, resultado = usuarioDAO.iniciar_sesion(correo, contrasena)
        
        if login_exitoso:
            ms.showinfo("Login Exitoso", f"Sesión iniciada. ID Rol: {resultado.get_id_rol()}, {resultado.get_nombres()}")
        else:
            ms.showerror("Error de Login", resultado)  # 'resultado' contiene el mensaje de error en caso de fallo

if __name__ == '__main__':
    raiz = Tk()
    aplicacion = Login(raiz)
    raiz.mainloop()
