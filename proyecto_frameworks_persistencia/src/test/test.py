from ..main.bookcraft.domain.libro.libro import Libro

# Crear una instancia de la clase Libro
mi_libro = Libro("El principito", "Antoine de Saint-Exupéry", "Ficción")

# Imprimir los atributos del libro
print("Título:", mi_libro.obtener_titulo())
print("Autor:", mi_libro.obtener_autor())
print("Género:", mi_libro.obtener_genero())

# Cambiar algunos atributos
mi_libro.establecer_titulo("1984")
mi_libro.establecer_autor("George Orwell")
mi_libro.establecer_genero("Distopía")

# Imprimir los atributos del libro después de cambiarlos
print("Título:", mi_libro.obtener_titulo())
print("Autor:", mi_libro.obtener_autor())
print("Género:", mi_libro.obtener_genero())