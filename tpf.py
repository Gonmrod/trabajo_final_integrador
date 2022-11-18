from tkinter import * #--> Lo importé para realizar la gráfica
from tkinter import messagebox #--> Para mensajes emergentes.
import sqlite3 #--> Para conectar con base de datos.

#Alumno: Rodriguez, Gonzalo Martín -
#Profesor: Morales, Felipe -
#Com--06

#Índice
#0) Funciones 
#1) Menu superior
#--------1.a) Menú para Base de datos
#--------1.b) Menú para borrar campos
#--------1.c) CRUD
#--------1.d) Ayuda
#2)Cuadro intermedio con campos para carga de datos
#3) Creación de labels (Etiquetas)
#4) Creación de Botones
#5) Creación de Base de datos

#0) Funciones

def conexionBBDD():
    #Función para conectar con base de datos
    conn_bbdd=sqlite3.connect('Usuarios.db') 
    #El cursor, es un objeto que se utiliza para realizar la conexión para ejecutar consultas SQL. Actúa como middleware entre la conexión de la base de datos SQLite y la consulta SQL. Se crea después de dar conexión a la base de datos SQLite.
   #Acontinuación, creo la tabla y establezco instrucciones a cada casillero.
    mi_cursor=conn_bbdd.cursor() 
    try:
        mi_cursor.execute("""CREATE TABLE DATOS_USUARIOS (
            ID INTEGER PRIMARY KEY AUTOINCREMENT, 
            NOMBRE_USUARIO VARCHAR(30), 
            APELLIDO_USUARIO VARCHAR(30), 
            CUIT_USUARIO VARCHAR(15), 
            DOMPART_USUARIO VARCHAR(50), 
            DOMCOM_USUARIO VARCHAR(50), 
            EXPTE_USUARIO VARCHAR(40), 
            CUENTA_USUARIO VARCHAR(10), 
            TRAMITE_USUARIO VARCHAR(30), 
            RUBRO_USUARIO VARCHAR(50))
        """)
        messagebox.showinfo("BBDD", "BBDD creada con éxito.")
    except:
        messagebox.showwarning("¡Atención!", "La BBDD ya existe.")

#https://www.youtube.com/watch?v=5XPLCDp7nDk&t=275s

root=Tk()

#1) Menu superior

barra_menu=Menu(root) #-->Variable
root.config(menu=barra_menu, width= 300, height=300)

#1.a) Menú para Base de datos
bbdd_menu=Menu(barra_menu, tearoff=0) #tearoff=etiqueta para lineas
bbdd_menu.add_command(label="Conectar", command=conexionBBDD) #-->Instrucción para conectar a la bbdd
bbdd_menu.add_command(label="Salir")

#1.b) Menú para Borrar campos
borrar_menu=Menu(barra_menu, tearoff=0)
borrar_menu.add_command(label="Borrar campos")

#1.c) Creaciónd de CRUD (Creat, Read, Update, Delete), para operar sobre info. almacenada.
crud_menu=Menu(barra_menu, tearoff=0)
crud_menu.add_command(label="Crear")
crud_menu.add_command(label="Leer")
crud_menu.add_command(label="Actualizar")
crud_menu.add_command(label="Borrar")

#1.d) Ayuda
ayuda_menu=Menu(barra_menu, tearoff=0)
ayuda_menu.add_command(label="Contacto")
ayuda_menu.add_command(label="Acerca de...")

#Agregamos las opciones a la barra de menú, es decir especificamos que pertenece todo lo
#lo anterior a la barra de menú.
barra_menu.add_cascade(label="BBDD", menu=bbdd_menu)
barra_menu.add_cascade(label="Borrar", menu=borrar_menu)
barra_menu.add_cascade(label="CRUD", menu=crud_menu)
barra_menu.add_cascade(label="Ayuda", menu=ayuda_menu)

#-------------------------------------------------------#

#2)Cuadro intermedio con campos para carga de datos

frame_superior=Frame(root)
frame_superior.pack() #---> para empaquetar "es un tipo de posicionamiento para los widgets que ajusta todo los elementos acomodándolos entre sí, para luego hacer la ventana raíz tan grande para contener todos estos elementos"

#2.a) Creación de cuadros de textos (entry)
cuadro_id=Entry(frame_superior)
cuadro_id.grid(row=0, column=1, padx=10, pady=10) #Se establece la posición que ocuparán
cuadro_id.config(foreground="red", justify="left")

cuadro_nombre=Entry(frame_superior)
cuadro_nombre.grid(row=1, column=1, padx=10, pady=10)
cuadro_nombre.config(foreground="red", justify="left")

cuadro_apellido=Entry(frame_superior)
cuadro_apellido.grid(row=2, column=1, padx=10, pady=10)
cuadro_apellido.config(foreground="red", justify="left")

cuadro_cuit=Entry(frame_superior)
cuadro_cuit.grid(row=3, column=1, padx=10, pady=10)
cuadro_cuit.config(foreground="red", justify="left")

cuadro_dom_part=Entry(frame_superior)
cuadro_dom_part.grid(row=4, column=1, padx=10, pady=10)
cuadro_dom_part.config(justify="left")

cuadro_dom_com=Entry(frame_superior)
cuadro_dom_com.grid(row=5, column=1, padx=10, pady=10)
cuadro_dom_com.config(justify="left")

cuadro_expte=Entry(frame_superior)
cuadro_expte.grid(row=6, column=1, padx=10, pady=10)
cuadro_expte.config( justify="left")

cuadro_cuenta=Entry(frame_superior)
cuadro_cuenta.grid(row=7, column=1, padx=10, pady=10)
cuadro_cuenta.config(justify="left")

cuadro_tipo_tramite=Entry(frame_superior)
cuadro_tipo_tramite.grid(row=8, column=1, padx=10, pady=10)
cuadro_tipo_tramite.config(justify="left")

cuadro_rubro=Text(frame_superior, width=16, height=5)
cuadro_rubro.grid(row=9, column=1, padx=10, pady=10)
scroll_bar=Scrollbar(frame_superior, command=cuadro_rubro.yview) #Para poder ver si el rubro es amplio
scroll_bar.grid(row=9, column=2, sticky="nsew")
cuadro_rubro.config(yscrollcommand=scroll_bar.set) #Esto sirve para saber donde deternerse. 

#----------------------------------------------------------------#

#3) Creación de labels (Etiquetas)

id_label=Label(frame_superior, text="Id:")
id_label.grid(row=0, column=0, sticky="e", padx=10, pady=10)

nombre_label=Label(frame_superior, text="Nombre:")
nombre_label.grid(row=1, column=0, sticky="e", padx=10, pady=10)

apellido_label=Label(frame_superior, text="Apellido:")
apellido_label.grid(row=2, column=0, sticky="e", padx=10, pady=10)

cuit_label=Label(frame_superior, text="CUIL/CUIT:")
cuit_label.grid(row=3, column=0, sticky="e", padx=10, pady=10)

dom_part_label=Label(frame_superior, text="Domicilio Particular:")
dom_part_label.grid(row=4, column=0, sticky="e", padx=10, pady=10)

dom_com_label=Label(frame_superior, text="Domicilio Comercial:")
dom_com_label.grid(row=5, column=0, sticky="e", padx=10, pady=10)

expte_label=Label(frame_superior, text="N° de Expediente:")
expte_label.grid(row=6, column=0, sticky="e", padx=10, pady=10)

cuenta_label=Label(frame_superior, text="N° de Cuenta:")
cuenta_label.grid(row=7, column=0, sticky="e", padx=10, pady=10)

tipo_tramite_label=Label(frame_superior, text="Tipo de Trámite:")
tipo_tramite_label.grid(row=8, column=0, sticky="e", padx=10, pady=10)

rubro_label=Label(frame_superior, text="Rubro:")
rubro_label.grid(row=9, column=0, sticky="e", padx=10, pady=10)

#--------------------------------------------------------------#

#4) Creación de Botones

frame_inferior=Frame(root)
frame_inferior.pack()

boton_crear=Button(frame_inferior, text="Crear")
boton_crear.grid(row=1, column=0, sticky="e", padx=10, pady=10)

boton_leer=Button(frame_inferior, text="Leer")
boton_leer.grid(row=1, column=1, sticky="e", padx=10, pady=10)

boton_actualizar=Button(frame_inferior, text="Actualizar")
boton_actualizar.grid(row=1, column=2, sticky="e", padx=10, pady=10)

boton_borrar=Button(frame_inferior, text="Borrar")
boton_borrar.grid(row=1, column=3, sticky="e", padx=10, pady=10)

#----------------------------------------------------------------#

#5) Creación de Base de datos

root.mainloop()