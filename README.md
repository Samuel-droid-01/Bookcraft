# Bookcraft
BookCraft es un sistema de gestión bibliotecaria que simplifica el préstamo, devolución y búsqueda de libros. Ofrece una interfaz intuitiva para usuarios y funciones de catalogación para bibliotecarios. Ideal para bibliotecas escolares, universitarias y comunitarias.
## Preparación del entorno: --->Solo para linux, en windows no es nesesario

Antes de iniciar, es necesario instalar Python 3.12 y su correspondiente módulo venv. Esto se puede hacer con el siguiente comando:

```bash
apt install python3.12-venv
```

instalacion e inicializacion del proyecto 
Aquí tienes una explicación de los comandos que podrías incluir en tu archivo README:

1. **Crear un entorno virtual de Python**:
   ```bash
   python3 -m venv my_modulos
   ```
   Este comando crea un entorno virtual de Python llamado `my_modulos`. Un entorno virtual es un ambiente aislado donde puedes instalar paquetes de Python sin afectar a tu instalación global de Python.

2. **Activar el entorno virtual**:
   ```bash
   source my_modulos/bin/activate
   ```
   Este comando activa el entorno virtual que acabas de crear. Una vez activado, cualquier paquete que instales con `pip` se instalará en este entorno virtual.

3. **Listar los paquetes instalados**:
   ```bash
   pip freeze
   ```
   Este comando muestra una lista de todos los paquetes instalados en el entorno virtual, junto con sus versiones.

4. **Guardar la lista de paquetes en un archivo**:
   ```bash
   pip freeze > requirements.txt
   ```
   Este comando guarda la lista de paquetes instalados en un archivo llamado `requirements.txt`. Este archivo puede ser utilizado para instalar los mismos paquetes en otro entorno.

5. **Instalar paquetes desde un archivo**:
   ```bash
   pip install -r requirements.txt
   ```
   Este comando instala todos los paquetes listados en el archivo `requirements.txt` en el entorno virtual.
6. **Desactivar el entorno virtual**:
   deactivate
   ```
   Este comando desactiva el entorno virtual

Recuerda que los usuarios deben tener Python y `pip` instalados en sus sistemas para poder ejecutar estos comandos. Además, deben activar el entorno virtual con `source my_modulos/bin/activate` antes de instalar o usar cualquier paquete.
## En windows:
   3. **Listar los paquetes instalados**:
   ```bash
   pip freeze
   ```
   Este comando muestra una lista de todos los paquetes instalados en el entorno virtual, junto con sus versiones.

   4. **Guardar la lista de paquetes en un archivo**:
      ```bash
      pip freeze > requirements.txt
      ```
      Este comando guarda la lista de paquetes instalados en un archivo llamado `requirements.txt`. Este archivo puede ser utilizado para instalar los mismos paquetes en otro entorno.

   5. **Instalar paquetes del proyecto**:
      ```bash
      pip install -r requirements.txt
      ```

