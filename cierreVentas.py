import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showwarning, showinfo, showerror
from datetime import datetime


# Variables Globales

defaultColor =  ''
lugar = {}
usuario ={}
ahora = None


def cargarDatosGlobales():
    global defaultColor
    global lugar
    global usuario
    global ahora

    defaultColor =  '#FFF8EF'
    ahora = datetime.now()
    lugar = {'codLocal': 1, 'nombreLocal': 'San Rafael'}
    usuario = {'idUsuario': '1234567890', 'nombre': 'Leonardo', 'apellido': 'Vidal'}

def crearWidgetsHeader(headerFrame, root):

    global defaultColor
    global lugar
    global usuario
    global ahora

    root.logo = tk.PhotoImage(file='./img/LasPalmerasLogotipo.png', height=100, width=174)
    logoLabel = tk.Label(headerFrame, image=root.logo, bg=defaultColor)

    tituloLabel = tk.Label(headerFrame, text='Cierre Diario de Ventas', justify='center', font=('Helvetica', 20), bg=defaultColor)
    identFrame = tk.Frame(headerFrame, bg=defaultColor)

    localLabel = tk.Label(identFrame, text=lugar['nombreLocal'], bg=defaultColor)
    fechaLabel = tk.Label(identFrame, text=ahora.strftime('%d-%m-%Y'), bg=defaultColor)
    userLabel = tk.Label(identFrame, text=usuario['nombre']+' '+usuario['apellido'], bg=defaultColor)

    localLabel.pack(fill='both', padx=5)
    fechaLabel.pack(fill='both', padx=5)
    userLabel.pack(fill='both', padx=5)

    logoLabel.pack(side='left', fill='both')
    identFrame.pack(side='right')
    tituloLabel.pack(expand=True)

def crearWidgetsCommand(commandFrame, root):

    resumenButton = tk.Button(commandFrame, text='Resumen')
    ventasButton = tk.Button(commandFrame, text='Ventas')
    formasPagoButton = tk.Button(commandFrame, text='Formas de Pago')
    gastosGeneralesButton = tk.Button(commandFrame, text='Gastos Generales')
    gastosPersonalButton = tk.Button(commandFrame, text='Gastos de Personal')
    depositosButton = tk.Button(commandFrame, text='Depósitos')
    salirButton =tk.Button(commandFrame, text='Salir', command=lambda: root.quit())

    resumenButton.pack(fill='x', expand=True)
    ventasButton.pack(fill='x', expand=True)
    formasPagoButton.pack(fill='x', expand=True)
    gastosGeneralesButton.pack(fill='x', expand=True)
    gastosPersonalButton.pack(fill='x', expand=True)
    depositosButton.pack(fill='x', expand=True)
    salirButton.pack(fill='x', expand=True)

def crearFrames(root):

    headerFrame = tk.Frame(root, bg=defaultColor)
    headerFrame.pack(fill='x')
    crearWidgetsHeader(headerFrame, root)

    commandFrame = tk.Frame(root, bg=defaultColor)
    commandFrame.pack(side='left', fill='y')
    crearWidgetsCommand(commandFrame, root)

    # dataFrame  = tk.Frame(root, bg=defaultColor)
    # dataFrame.pack(side='left', fill='y')

def cerrarVentana():
    pass

def salir(root):
    root.quit()

def main():

    global defaultColor
    root = tk.Tk()

    root.protocol('WM_DELETE_WINDOW', cerrarVentana)

    root.geometry('800x600')
    root.config(bg=defaultColor)
    root.title('Sistema de registro de datos')

    rootStyle = ttk.Style(root)

    rootStyle.configure('TLabel', bg=defaultColor)
    rootStyle.configure('TFrame', bg=defaultColor)
   
    cargarDatosGlobales()
    crearFrames(root)

    root.mainloop()


if __name__ == '__main__':
    main()
