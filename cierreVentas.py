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

    # logo = tk.PhotoImage(file='/home/users/jtibau/Desarrollo/Palmeras/CierreVentas/img/LasPalmerasLogotipo.png')
    logo = tk.PhotoImage(file='./img/LasPalmerasLogotipo.png', height=100, width=174)

    logoLabel = tk.Label(headerFrame, image=logo, text="Las Palmeras Logo", bg=defaultColor, font=('Helvetica', 14), compound='right')
    tituloLabel = tk.Label(headerFrame, text='Cierre Diario de Ventas', justify='center', font=('Helvetica', 20), bg=defaultColor)
    identFrame = tk.Frame(headerFrame, bg=defaultColor)

    localLabel = tk.Label(identFrame, text=lugar['nombreLocal'], bg=defaultColor)
    fechaLabel = tk.Label(identFrame, text=ahora.strftime('%d-%m-%Y'), bg=defaultColor)
    userLabel = tk.Label(identFrame, text=usuario['nombre']+' '+usuario['apellido'], bg=defaultColor)

    localLabel.pack(fill='both')
    fechaLabel.pack(fill='both')
    userLabel.pack(fill='both')

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

    dataFrame  = tk.Frame(root, bg=defaultColor)
    dataFrame.pack(side='left', fill='y')

def cerrarVentana():
    print("Ventana cerrada")

def salir():
    pass

def main():

    global defaultColor
    root = tk.Tk()

    root.protocol('WM_DELETE_WINDOW', cerrarVentana)

    root.title ='Administración de Locales.'
    root.geometry('800x600')
    root.config(bg=defaultColor)

    rootStyle = ttk.Style(root)

    rootStyle.configure('TLabel', bg=defaultColor)
   
    cargarDatosGlobales()
    crearFrames(root)

    root.mainloop()


if __name__ == '__main__':
    main()



# class IdentFrame(tk.Frame):
#     def __init__(self, container):
#         super().__init__(self)

#         self.__createWidgets()

#     def __createWidgets(self):
#         localLabel = tk.Label(text='Nombre del Local')
#         fechaLabel = tk.Label(text='Fecha y hora')
#         userLabel = tk.Label(text='Nombre del usuario')

#         localLabel.pack(ipadx=5, ipady=5, fill='x')
#         fechaLabel.pack(ipadx=5, ipady=5, fill='x')
#         userLabel.pack(ipadx=5, ipady=5, fill='x')

# class HeaderFrame(tk.Frame):
#     def __init__(self, app):
#         super().__init__()

#         self.config(fg='red')

#         self.__createWidgets()

#     def __createWidgets(self):
#         logoLabel = tk.Label()
#         tituloLabel = tk.Label(text='Cierre Diario de Ventas')
#         idFrame = IdentFrame(self)

#         logoLabel.pack(side='left')
#         tituloLabel.pack(side='left')
#         idFrame.pack(side='right')
        

# class CommandFrame(tk.Frame):
#     def __init__(self, app):
#         pass

# class BottomFrame(tk.Frame):
#     def __init__(self, app):
#         pass

# class DataFrames(tk.Frame):
#     def __init__(self, app):
#         pass


# class App(tk.Tk):
#     def __init__(self):
#         super().__init__()

#         defaultColor = '#FFF8EF'

#         self.title('')
#         self.geometry('800x600')
#         self.config(bg=defaultColor)  
        
#     def __createFrames(self):
#         headerFrame = HeaderFrame(self)
#         commandFrame = CommandFrame(self)
#         dataFrames = DataFrames(self)

#         headerFrame.pack(self, fill='x')


# if __name__ == '__main__':
#     app = App()
#     app.mainloop()
