# trabajo_final_integrador
Trabajo final integrador UNAJ Com. 06

Prof. Felipe Morales.
Alumno: Gonzalo Rodriguez
DNI: 35.401.481.

Estimado profesor, como le había comentado, el programa goza de varias caracterísiticas adicionales. 
0°) El objetivo del programa tiene la finalidad de suplir una necesidad imperiosa de crear una base de datos para sistema de expedientes.
En este, se cargan no solo datos del expediente, como cuentas, actividades y domicilios comerciales, sino también datos personales de los solicitantes.
La interfáz cuenta con un menú superior, unos botones (CRUD) para la gestión de los datos. Asimismo, es dable destacar que al programa
le dejé una suerte de índice para que pueda desplazarse con mayor facilidad y está comentado para explicar por qué uso cada cosa.
1°) Se utilizó la siguiente librería: tkinter, sqlite3, pandas y openpyxl. Tkinter, para crear una interfaz gráfica
para que sea amigable para el usuario. Sqlite3, lo utilicé para crear base de datos con extensión .db para almacenar información de forma sencilla.
Pandas y Openpyxl para poder trabajar con hojas de cálculo con extensión xls. Esto me permitió poder exportar un arhivo de estas características.
Seguramente, si desea ejecucarlo desde un editor de código como VSCODE, deberá instalar librería, para pandas y openpyxl. 
pandas -datareader y openpyxl (por medio del sistema de gestión de paquetes (pip). En caso de que no reconzca pip, habrá que editar
las variables de enterno del sistema y modificar el instalador de python.
2°) Por otra parte, y a modo de plus, utilicé un módulo pyinstaller (pip install pyinstaller) para poder compilar el arhico .py y generar un ejecutable. 
Para ello, ubiqué en una carpeta en el escritorio el archivo .py y además me tomé la molestia de agregar una foto mía como ícono para el ejecutable, utilicé mi consola 
cmd, y por medio de la instrucción: pyinstaller --windowed --onefile --icon=./logo.ico (nombre del archivo y su extensión .py) Creó el archivo .exe. --windowed para que 
mostrara la interfaz al ejecutarlo, --onfile para que lo metiera todo en un .exe y --icon=./logo.ico para que agregara mi imagen al archivo.

Espero sea de su agrado.
