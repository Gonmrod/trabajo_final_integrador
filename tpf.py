from tkinter import * #--> Lo importé para realizar la gráfica
from tkinter import messagebox #--> Para mensajes emergentes.
import sqlite3 #--> Para conectar con base de datos.
from pandas import *
import pandas as pd




#Alumno: Rodriguez, Gonzalo Martín -
#Profesor: Morales, Felipe -
#Com--06

#Índice
#0) Funciones --> Desde líneas 27 hasta 140.
#1) Menu superior --> Desde línea 144 hasta 180.
#--------1.a) Menú para Base de datos --> Desde línea 149.
#--------1.b) Menú para borrar campos --> Desde línea 154.
#--------1.c) CRUD --> Desde línea 158.
#--------1.e) Exportar a .xls --> Desde línea 165.
#--------1.d) Ayuda --> Desde línea 169.
#2) Cuadro intermedio con campos para carga de datos y Entry--> Desde línea 184 hasta 239.
#3) Creación de labels (Etiquetas) --> Desde línea 243 hasta 273.
#4) Creación de Botones --> Desde línea 277 hasta 292.


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

def salir_app():
    valor=messagebox.askquestion("Salir", "¿Deséas salir de la aplicación?")
    if valor=="yes":
        root.destroy()

def borrar_campos(): #Resetea los campos
    mi_id.set("")
    mi_nombre.set("")
    mi_apellido.set("")
    mi_cuit.set("")
    mi_dom_part.set("")
    mi_dom_com.set("")
    mi_expte.set("")
    mi_cuenta.set("")
    mi_tramite.set("")
    cuadro_rubro.delete(1.0, END) #El 1.0 cuenta como punto de partida, y el END, hasta el final.

def crear():
    mi_conexion=sqlite3.connect("Usuarios.db")
    mi_cursor=mi_conexion.cursor()
    mi_cursor.execute("INSERT INTO DATOS_USUARIOS VALUES(NULL,'" + mi_nombre.get() + 
        "','" + mi_apellido.get() +
        "','" + mi_cuit.get() +
        "','" + mi_dom_part.get() +
        "','" + mi_dom_com.get() +
        "','" + mi_expte.get() +
        "','" + mi_cuenta.get() +
        "','" + mi_tramite.get() +
        "','" + cuadro_rubro.get("1.0", END) + "')")
    mi_conexion.commit()
    messagebox.showinfo("BBDD", "Registro ingresado con éxito.")
def leer():
    mi_conexion=sqlite3.connect("Usuarios.db")
    mi_cursor=mi_conexion.cursor()
    id=0
    if mi_id.get() != "" and mi_id.get()!=None:
        id=mi_id.get()
    mi_cursor.execute("SELECT * FROM DATOS_USUARIOS WHERE ID=" + str(id) + " OR CUIT_USUARIO='" + mi_cuit.get() + "' OR EXPTE_USUARIO='" + mi_expte.get() + "' OR CUENTA_USUARIO='" + mi_cuenta.get()+ "'")
    los_usuarios=mi_cursor.fetchall()

    for usuario in los_usuarios:
        mi_id.set(usuario[0])
        mi_nombre.set(usuario[1])
        mi_apellido.set(usuario[2])
        mi_cuit.set(usuario[3])
        mi_dom_part.set(usuario[4])
        mi_dom_com.set(usuario[5])
        mi_expte.set(usuario[6])
        mi_cuenta.set(usuario[7])
        mi_tramite.set(usuario[8])
        cuadro_rubro.insert("1.0", usuario[9])
    
    mi_conexion.commit()

def actualizar():
    mi_conexion=sqlite3.connect("Usuarios.db")
    mi_cursor=mi_conexion.cursor()
    mi_cursor.execute("UPDATE DATOS_USUARIOS SET NOMBRE_USUARIO='" + mi_nombre.get() + 
    "', APELLIDO_USUARIO='" + mi_apellido.get()+
    "', CUIT_USUARIO='" + mi_cuit.get()+
    "', DOMPART_USUARIO='" + mi_dom_part.get()+
    "', DOMCOM_USUARIO='" + mi_dom_com.get()+
    "', EXPTE_USUARIO='" + mi_expte.get()+
    "', CUENTA_USUARIO='" + mi_cuenta.get()+
    "', TRAMITE_USUARIO='" + mi_tramite.get()+
    "', RUBRO_USUARIO='" + cuadro_rubro.get("1.0", END) +
    "' WHERE ID=" + mi_id.get())
    mi_conexion.commit()
    messagebox.showinfo("BBDD", "Registro actualizado con éxito.")

def borrar():
    mi_conexion=sqlite3.connect("Usuarios.db")
    mi_cursor=mi_conexion.cursor()
    mi_cursor.execute("DELETE FROM DATOS_USUARIOS WHERE ID=" + mi_id.get())
    mi_conexion.commit()
    messagebox.showinfo("BBDD", "Registro eliminado con éxito.")

def contacto():
    messagebox.showinfo("CONTACTO", "Por dudas o sugerencias escribir a gonzalo.marodriguez@gmail.com")

def acerca():
    messagebox.showinfo("Acerca de...", "Programa creado para TFI Prof. Felipe Morales - Com. 06 // Autor: Gonzalo Rodriguez")

def exportar():
    mi_conexion=sqlite3.connect("Usuarios.db")
    datos = pd.read_sql("SELECT * FROM DATOS_USUARIOS", mi_conexion)
    df= pd.DataFrame(datos)
    df.to_excel((f'Datos.xlsx'))
    messagebox.showinfo('Información', 'Datos exportados con éxito.') 
    
root=Tk()

#1) Menu superior

barra_menu=Menu(root) #-->Variable
root.config(menu=barra_menu, width= 300, height=300)

#1.a) Menú para Base de datos
bbdd_menu=Menu(barra_menu, tearoff=0) #tearoff=etiqueta para lineas
bbdd_menu.add_command(label="Conectar", command=conexionBBDD) #-->Instrucción para conectar a la bbdd
bbdd_menu.add_command(label="Salir", command=salir_app)

#1.b) Menú para Borrar campos
borrar_menu=Menu(barra_menu, tearoff=0)
borrar_menu.add_command(label="Borrar campos", command=borrar_campos)

#1.c) Creaciónd de CRUD (Creat, Read, Update, Delete), para operar sobre info. almacenada.
crud_menu=Menu(barra_menu, tearoff=0)
crud_menu.add_command(label="Crear", command=crear)
crud_menu.add_command(label="Leer", command=leer)
crud_menu.add_command(label="Actualizar", command=actualizar)
crud_menu.add_command(label="Borrar", command=borrar)

#1.d) Exportar a xls
exportar_menu=Menu(barra_menu, tearoff=0)
exportar_menu.add_command(label="Exportar BBDD a .xls", command=exportar)

#1.e) Ayuda
ayuda_menu=Menu(barra_menu, tearoff=0)
ayuda_menu.add_command(label="Contacto", command=contacto)
ayuda_menu.add_command(label="Acerca de...", command=acerca)

#Agregamos las opciones a la barra de menú, es decir especificamos que pertenece todo lo
#lo anterior a la barra de menú.
barra_menu.add_cascade(label="BBDD", menu=bbdd_menu)
barra_menu.add_cascade(label="Borrar", menu=borrar_menu)
barra_menu.add_cascade(label="CRUD", menu=crud_menu)
barra_menu.add_cascade(label="Exportar", menu=exportar_menu)
barra_menu.add_cascade(label="Ayuda", menu=ayuda_menu)

#-------------------------------------------------------#

#2)Cuadro intermedio con campos para carga de datos

frame_superior=Frame(root)
frame_superior.pack() #---> para empaquetar "es un tipo de posicionamiento para los widgets que ajusta todo los elementos acomodándolos entre sí, para luego hacer la ventana raíz tan grande para contener todos estos elementos"
mi_id=StringVar()
mi_nombre=StringVar()
mi_apellido=StringVar()
mi_cuit=StringVar()
mi_dom_part=StringVar()
mi_dom_com=StringVar()
mi_expte=StringVar()
mi_cuenta=StringVar()
mi_tramite=StringVar()

#2.a) Creación de cuadros de textos (entry)
cuadro_id=Entry(frame_superior, textvariable=mi_id)
cuadro_id.grid(row=0, column=1, padx=10, pady=10) #Se establece la posición que ocuparán
cuadro_id.config(foreground="red", justify="left")

cuadro_nombre=Entry(frame_superior, textvariable=mi_nombre)
cuadro_nombre.grid(row=1, column=1, padx=10, pady=10)
cuadro_nombre.config(foreground="red", justify="left")

cuadro_apellido=Entry(frame_superior, textvariable=mi_apellido)
cuadro_apellido.grid(row=2, column=1, padx=10, pady=10)
cuadro_apellido.config(foreground="red", justify="left")

cuadro_cuit=Entry(frame_superior, textvariable=mi_cuit)
cuadro_cuit.grid(row=3, column=1, padx=10, pady=10)
cuadro_cuit.config(foreground="red", justify="left")

cuadro_dom_part=Entry(frame_superior, textvariable=mi_dom_part)
cuadro_dom_part.grid(row=4, column=1, padx=10, pady=10)
cuadro_dom_part.config(justify="left")

cuadro_dom_com=Entry(frame_superior, textvariable=mi_dom_com)
cuadro_dom_com.grid(row=5, column=1, padx=10, pady=10)
cuadro_dom_com.config(justify="left")

cuadro_expte=Entry(frame_superior, textvariable=mi_expte)
cuadro_expte.grid(row=6, column=1, padx=10, pady=10)
cuadro_expte.config( justify="left")

cuadro_cuenta=Entry(frame_superior, textvariable=mi_cuenta)
cuadro_cuenta.grid(row=7, column=1, padx=10, pady=10)
cuadro_cuenta.config(justify="left")

cuadro_tipo_tramite=Entry(frame_superior, textvariable=mi_tramite)
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

boton_crear=Button(frame_inferior, text="Crear", command=crear)
boton_crear.grid(row=1, column=0, sticky="e", padx=10, pady=10)

boton_leer=Button(frame_inferior, text="Leer", command=leer)
boton_leer.grid(row=1, column=1, sticky="e", padx=10, pady=10)

boton_actualizar=Button(frame_inferior, text="Actualizar", command=actualizar)
boton_actualizar.grid(row=1, column=2, sticky="e", padx=10, pady=10)

boton_borrar=Button(frame_inferior, text="Borrar", command=borrar)
boton_borrar.grid(row=1, column=3, sticky="e", padx=10, pady=10)

#----------------------------------------------------------------#


root.resizable(False, False)
root.mainloop()