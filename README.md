# proyecto-coder-negocio

Aplicacion web desarrollada para gestion de productos(colchones y almohadas) y clientes para una colchoneria
Con respecto a los modelos:
Desde la página inicio se puede acceder a las diferentes funcionalidades. En la parte superior derecha se encuentra una barra de navegación la cual ofrece los siguientes accesos:

Colchones: Lista de colchones registrados.

Almohadas: Lista de almohadas registradas.

Clientes: Lista de clientes registrados.

Blog (Pages): Sección de artículos sobre productos y descanso con texto enriquecido e imágenes.

Mensajes: Sistema para enviarse mensajes entre usuarios registrados.

About: Una sección con información sobre el dueño de la página y los objetivos del proyecto.

Seguridad y Usuarios
Para este proyecto implementé un sistema de usuarios avanzados. Para acceder a la lista de clientes, colchones, almohadas o al blog, el usuario sí o sí tiene que estar logueado. Si un usuario intenta entrar a estas secciones sin haber iniciado sesión, la aplicación lo lleva directamente a la pantalla de Login o le da la opción de Registrarse.

Cada usuario tiene su propio Perfil, donde puede cargar su nombre, apellido, biografía y un Avatar (foto de perfil). También agregué la opción de cambiar la contraseña y editar los datos del perfil desde ahí.

Orden para probar la aplicación:
1. Acceder a la página de inicio.

2. Ir a Registrarse para crear un usuario nuevo.

3. Iniciar sesión con los datos creados.

4. Una vez logueado, ir hacia Agregar Colchón y registrar uno. Ahora, al terminar, el sistema te lleva directo a la lista de colchones.

5. Repetir el paso con almohadas y clientes.

6. Entrar al Blog (Pages) para ver los artículos o crear uno nuevo con imagen.

7. Probar la Mensajería enviando un mensaje a otro usuario.

8. Entrar al Perfil para subir un Avatar o editar la biografía.

9. Verificar la búsqueda de cliente por DNI.