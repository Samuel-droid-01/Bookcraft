# Bookcraft
BookCraft es un sistema de gestión bibliotecaria que simplifica el préstamo, devolución y búsqueda de libros. Ofrece una interfaz intuitiva para usuarios y funciones de catalogación para bibliotecarios. Ideal para bibliotecas escolares, universitarias y comunitarias.

apt install python3.12-venv -------------> instalacion obligatoria antes de iniciar

instalacion e inicializacion del proyecto 
Aquí tienes una explicación de los comandos que podrías incluir en tu archivo README:

1. **Crear un entorno virtual de Python**:
  
   python3 -m venv my_modulos
  
   Este comando crea un entorno virtual de Python llamado `my_modulos`. Un entorno virtual es un ambiente aislado donde puedes instalar paquetes de Python sin afectar a tu instalación global de Python.

2. **Activar el entorno virtual**:

   source my_modulos/bin/activate
  
   Este comando activa el entorno virtual que acabas de crear. Una vez activado, cualquier paquete que instales con `pip` se instalará en este entorno virtual.

3. **Instalar un paquete**:
  
   pip install mysql-connector-python
   
   Este comando instala el paquete `mysql-connector-python` en el entorno virtual. Puedes reemplazar `mysql-connector-python` con el nombre de cualquier otro paquete que quieras instalar.

4. **Listar los paquetes instalados**:
   
   pip freeze
   
   Este comando muestra una lista de todos los paquetes instalados en el entorno virtual, junto con sus versiones.

5. **Guardar la lista de paquetes en un archivo**:
   
   pip freeze > requirements.txt

   Este comando guarda la lista de paquetes instalados en un archivo llamado `requirements.txt`. Este archivo puede ser utilizado para instalar los mismos paquetes en otro entorno.

6. **Instalar paquetes desde un archivo**:

   pip install -r requirements.txt
   
   Este comando instala todos los paquetes listados en el archivo `requirements.txt` en el entorno virtual.
   Tienes razón, olvidé incluir cómo desactivar el entorno virtual. Aquí está la instrucción que puedes agregar a tu archivo README:

7. **Desactivar el entorno virtual**:
  
   deactivate
   
   Este comando desactiva el entorno virtual. Una vez desactivado, volverás a usar la versión global de Python y sus paquetes en tu sistema. Es importante desactivar el entorno virtual cuando hayas terminado de usarlo para evitar instalar paquetes en el lugar equivocado.

Recordatorio deben tener Python y `pip` instalados en sus sistemas para poder ejecutar estos comandos e en un inicio crear el entorno  virtual si es que no se a creado entorno virtual de Python llamado `my_modulos`. Además, deben activar el entorno virtual con `source my_modulos/bin/activate` antes de instalar o usar cualquier paquete.