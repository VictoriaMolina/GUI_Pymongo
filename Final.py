from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from datetime import datetime
import pymongo

# Configuración de la GUI
root = Tk()
root.geometry('600x300+500+50')
root.resizable(10, 10)
root.title("ULSA")

#Para configurar el acceso a mi DB
user = StringVar(value="ulsa")
passw = StringVar(value="1234567890")
database = StringVar(value="Sensores")
cluster = StringVar(value="cluster0-e9jsl.mongodb.net")
coleccion = StringVar(value="movimiento")
SERVER = "mongodb+srv://"
OPCIONES = "?retryWrites=true&w=majority"
conexion = StringVar()
client = ""

# Donde voy a guardar los datos
proy = StringVar()
query = StringVar()
res = StringVar()
doc = StringVar(value="db.getCollection('movimiento').find({})")
col = StringVar()

menubar = Menu(root)
root.config(menu=menubar)

configmenu = Menu(menubar, tearoff=0)
configmenu.add_command(label="Atlas", command=lambda: frame_configura())
configmenu.add_command(label="Find", command=lambda: frame_find())
configmenu.add_command(label="FindOne", command=lambda: frame_find_one())
configmenu.add_command(label="Insert", command=lambda: frame_insert())
configmenu.add_command(label="InsertOne", command=lambda: frame_insert_one())
configmenu.add_command(label="InsertMany", command=lambda: frame_insert_many())
configmenu.add_command(label="Update", command=lambda: frame_insert())
configmenu.add_command(label="UpdateOne", command=lambda: frame_insert())
configmenu.add_command(label="UpdateMany", command=lambda: frame_insert())
configmenu.add_command(label="Remove", command=lambda: frame_insert())
configmenu.add_command(label="DeleteOne", command=lambda: frame_insert())
configmenu.add_command(label="DeleteMany", command=lambda: frame_insert())
configmenu.add_separator()
configmenu.add_command(label="Salir", command=root.quit)

menubar.add_cascade(label="Menú", menu=configmenu)


def frame_configura():
    clear()
    mi_Frame = Frame()  # Creacion del Frame
    mi_Frame.pack()  # Empaquetamiento del Frameo
    mi_Frame.config(width="400", height="200")  # cambiar tamaño
    mi_Frame.config(bd=5)  # cambiar el grosor del borde
    # flat, groove, raised, ridge, solid, or sunken
    mi_Frame.config(relief="flat")  # cambiar el tipo de borde
    mi_Frame.config(cursor="pirate")  # cambiar el tipo de cursor
    mi_Frame.pack(fill='both', expand=1)
    mi_Frame.columnconfigure(1, weight=1)

    lbluser = Label(mi_Frame, text="Usuario: ").grid(row=0, column=0, padx=5, pady=5)
    entuser = Entry(mi_Frame, text="Usuario", textvariable=user).grid(row=0, column=1, sticky="nsew", padx=5, pady=5)

    lblpass = Label(mi_Frame, text="Password:").grid(row=1, column=0, padx=5, pady=5)
    entpassw = Entry(mi_Frame, text="Password", textvariable=passw).grid(row=1, column=1, sticky="nsew", padx=5, pady=5)

    lblcol = Label(mi_Frame, text="Base de datos:").grid(row=2, column=0, padx=5, pady=5)
    entcol = Entry(mi_Frame, text="Base de datos", textvariable=database).grid(row=2, column=1, sticky="nsew", padx=5, pady=5)

    lblcol = Label(mi_Frame, text="Colección:").grid(row=3, column=0, padx=5, pady=5)
    entcol = Entry(mi_Frame, text="Colección", textvariable=coleccion).grid(row=3, column=1, sticky="nsew", padx=5, pady=5)

    lblclu = Label(mi_Frame, text="Cluster:").grid(row=4, column=0, padx=5, pady=5)
    entclu = Entry(mi_Frame, text="Cluster", textvariable=cluster).grid(row=4, column=1, sticky="nsew", padx=5, pady=5)

    btnGuardar = Button(mi_Frame, text="Guadar Conexión", command=lambda: setconexion()).grid(row=5, column=0, columnspan=2, sticky="nsew", padx=5, pady=5)


def frame_find():
    clear()
    mi_Frame = Frame()  # Creacion del Frame
    mi_Frame.pack()  # Empaquetamiento del Frameo
    mi_Frame.config(width="400", height="200")  # cambiar tamaño
    mi_Frame.config(bd=5)  # cambiar el grosor del borde
    # flat, groove, raised, ridge, solid, or sunken
    mi_Frame.config(relief="flat")  # cambiar el tipo de borde
    mi_Frame.pack(fill='both', expand=1)
    mi_Frame.columnconfigure(1, weight=1)

    title = Label(mi_Frame, text="Consulta con find() ").grid(row=0, column=0, padx=5, pady=5)
    

    lbl = Label(mi_Frame, textvariable=doc).grid(row=1, column=0, padx=5, pady=5)


    res2 = Label(mi_Frame, text="Resultado").grid(row=3, column=0, padx=5, pady=5)
    lblRes = Label(mi_Frame, textvariable=res).grid(row=3, column=1, sticky="nsew", padx=5, pady=5)

    btnConsulta = Button(mi_Frame, text="Consultar", command=find(lblRes)).grid(row=2, column=0, columnspan=2, sticky="nsew", padx=3, pady=3)


def frame_find_one():
    clear()
    mi_Frame = Frame()  # Creacion del Frame
    mi_Frame.pack()  # Empaquetamiento del Frameo
    mi_Frame.config(width="400", height="200")  # cambiar tamaño
    mi_Frame.config(bd=5)  # cambiar el grosor del borde
    # flat, groove, raised, ridge, solid, or sunken
    mi_Frame.config(relief="flat")  # cambiar el tipo de borde
    mi_Frame.pack(fill='both', expand=1)
    mi_Frame.columnconfigure(1, weight=1)

    title2 = Label(mi_Frame, text="Consulta con find_one() ").grid(row=0, column=0, padx=5, pady=5)

    lblQuery = Label(mi_Frame, text="Query: ").grid(row=1, column=0, padx=5, pady=5)
    entQuery = Entry(mi_Frame , textvariable=query).grid(row=1, column=1, sticky="nsew", padx=5, pady=5)

    lblProy = Label(mi_Frame, text="Proyección:").grid(row=2, column=0, padx=5, pady=5)
    entProy = Entry(mi_Frame, textvariable=proy).grid(row=2, column=1, sticky="nsew", padx=5, pady=5)

    lblRes = Label(mi_Frame, text="Resultado:").grid(row=3, column=0, padx=5, pady=5)
    entRes = Entry(mi_Frame, textvariable=res).grid(row=3, column=1, sticky="nsew", padx=5, pady=5)

    btnFindOne = Button(mi_Frame, text="Consultar", command=lambda: find_one()).grid(row=4, column=0, columnspan=2, padx=3, pady=3)


def frame_insert():
    clear()
    mi_Frame = Frame()  # Creacion del Frame
    mi_Frame.pack()  # Empaquetamiento del Frameo
    mi_Frame.config(width="400", height="200")  # cambiar tamaño
    mi_Frame.config(bd=5)  # cambiar el grosor del borde
    # flat, groove, raised, ridge, solid, or sunken
    mi_Frame.config(relief="flat")  # cambiar el tipo de borde
    mi_Frame.pack(fill='both', expand=1)
    mi_Frame.columnconfigure(1, weight=1)

    title = Label(mi_Frame, text="Consulta con insert() ").grid(row=0, column=0, padx=5, pady=5)

    lblQuery = Label(mi_Frame, text="Query: ").grid(row=4, column=0, padx=5, pady=5)
    entQuery = Entry(mi_Frame , textvariable=query).grid(row=4, column=1, sticky="nsew", padx=5, pady=5)

    lblProy = Label(mi_Frame, text="Proyección:").grid(row=5, column=0, padx=5, pady=5)
    entProy = Entry(mi_Frame, textvariable=proy).grid(row=5, column=1, sticky="nsew", padx=5, pady=5)

    lblcol = Label(mi_Frame, text="Colección:").grid(row=6, column=0, padx=5, pady=5)
    entcol = Entry(mi_Frame, textvariable=col).grid(row=6, column=1, sticky="nsew", padx=5, pady=5)

    lblRes = Label(mi_Frame, text="Resultado:").grid(row=7, column=0, padx=5, pady=5)
    entRes = Entry(mi_Frame, textvariable=res).grid(row=7, column=1, sticky="nsew", padx=5, pady=5)

    btnInsert = Button(mi_Frame, text="Consultar", command=lambda: insert_one()).grid(row=8, column=0, columnspan=2, padx=3, pady=3)


def frame_insert_one():
    clear()
    mi_Frame = Frame()  # Creacion del Frame
    mi_Frame.pack()  # Empaquetamiento del Frameo
    mi_Frame.config(width="400", height="200")  # cambiar tamaño
    mi_Frame.config(bd=5)  # cambiar el grosor del borde
    # flat, groove, raised, ridge, solid, or sunken
    mi_Frame.config(relief="flat")  # cambiar el tipo de borde
    mi_Frame.pack(fill='both', expand=1)
    mi_Frame.columnconfigure(1, weight=1)

    title2 = Label(mi_Frame, text="Consulta con insert_one() ").grid(row=0, column=0, padx=5, pady=5)

    lblQuery = Label(mi_Frame, text="Query: ").grid(row=1, column=0, padx=5, pady=5)
    entQuery = Entry(mi_Frame , textvariable=query).grid(row=1, column=1, sticky="nsew", padx=5, pady=5)

    lblProy = Label(mi_Frame, text="Proyección:").grid(row=2, column=0, padx=5, pady=5)
    entProy = Entry(mi_Frame, textvariable=proy).grid(row=2, column=1, sticky="nsew", padx=5, pady=5)

    lblcol = Label(mi_Frame, text="Colección:").grid(row=3, column=0, padx=5, pady=5)
    entcol = Entry(mi_Frame, textvariable=col).grid(row=3, column=1, sticky="nsew", padx=5, pady=5)

    lblRes = Label(mi_Frame, text="Resultado:").grid(row=4, column=0, padx=5, pady=5)
    entRes = Entry(mi_Frame, textvariable=res).grid(row=4, column=1, sticky="nsew", padx=5, pady=5)

    btnInsertOne = Button(mi_Frame, text="Consultar", command=lambda: insert_one()).grid(row=5, column=0, columnspan=2, padx=3, pady=3)

def frame_insert_many():
    clear()
    mi_Frame = Frame()  # Creacion del Frame
    mi_Frame.pack()  # Empaquetamiento del Frameo
    mi_Frame.config(width="400", height="200")  # cambiar tamaño
    mi_Frame.config(bd=5)  # cambiar el grosor del borde
    # flat, groove, raised, ridge, solid, or sunken
    mi_Frame.config(relief="flat")  # cambiar el tipo de borde
    mi_Frame.pack(fill='both', expand=1)
    mi_Frame.columnconfigure(1, weight=1)

    title = Label(mi_Frame, text="Consulta con insert_one() ").grid(row=0, column=0, padx=5, pady=5)

    lblQuery = Label(mi_Frame, text="Query: ").grid(row=1, column=0, padx=5, pady=5)
    entQuery = Entry(mi_Frame , textvariable=query).grid(row=1, column=1, sticky="nsew", padx=5, pady=5)

    lblProy = Label(mi_Frame, text="Proyección:").grid(row=2, column=0, padx=5, pady=5)
    entProy = Entry(mi_Frame, textvariable=proy).grid(row=2, column=1, sticky="nsew", padx=5, pady=5)

    lblcol = Label(mi_Frame, text="Colección:").grid(row=3, column=0, padx=5, pady=5)
    entcol = Entry(mi_Frame, textvariable=col).grid(row=3, column=1, sticky="nsew", padx=5, pady=5)

    lblRes = Label(mi_Frame, text="Resultado:").grid(row=4, column=0, padx=5, pady=5)
    entRes = Entry(mi_Frame, textvariable=res).grid(row=4, column=1, sticky="nsew", padx=5, pady=5)

    btnFindOne = Button(mi_Frame, text="Consultar", command=lambda: find_one()).grid(row=5, column=0, columnspan=2, padx=3, pady=3)

def clear():
    list = root.pack_slaves()
    for l in list:
        l.pack_forget()


def setconexion():
    strtemp = ""

    strtemp = SERVER + user.get() + ":" + passw.get() + "@" + cluster.get() + "/" + database.get() + OPCIONES
    conexion.set(strtemp)

    messagebox.showinfo("Conexión", "Conexión guardada")


def save():
    #el valor que guardo en la DB
    document = {"place": snsrLoc.get(),
                "datetime": snsrDate.get(),
                "value": snsrValue.get()}
    #Nos conectamos al servidor
    client = pymongo.MongoClient(conexion.get())
    #Que DB voy a utilizar
    db = client[database.get()]
    #Que colección voy a utilizar
    colection = db[coleccion.get()]
    #Voy a guardar los datos
    data = colection.insert_one(document)
    print(data.inserted_id)
    messagebox.showinfo("Guardar", "Documento guardado con id:" + str(data.inserted_id))

def find(lblRes):
    print(lblRes)
    #Nos conectamos al servidor
    client = pymongo.MongoClient(conexion.get())
    #Que DB voy a utilizar
    db = client[database.get()]
    #Que colección voy a utilizar
    colection = db[coleccion.get()]
    #Voy a guardar los datos
    data = colection.find()
    for dat in data:
        lblRes.config(text=dat)
        print(dat)
    messagebox.showinfo("Consultar", "Documento encontrado:" )

def find_one():
    doc = {query.get(), proy.get()}
    #Nos conectamos al servidor
    client = pymongo.MongoClient(conexion.get())
    #Que DB voy a utilizar
    db = client[database.get()]
    #Que colección voy a utilizar
    colection = db[coleccion.get()]
    #Voy a guardar los datos
    data = colection.find_one(doc)
    for dat in data:
        print(dat)
    messagebox.showinfo("Consultar", "Documento encontrado:" + dat)

# Finalmente bucle de la aplicación
root.mainloop()