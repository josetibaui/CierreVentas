import tkinter as tk
from tkinter import ttk
from tkinter import font
from tkinter.messagebox import showwarning, showinfo, showerror
from datetime import datetime
from dataFrames import *


# Variables Globales

defaultColor =  ''
lugar = {}
usuario ={}
ahora = None


def cargarDatosGlobales():
    global resumenFrame
    global ventasFrame
    global formasPagoFrame
    global gastosGeneralesFrame
    global gastosPersonalFrame
    global depositosFrame

    global defaultColor
    global lugar
    global usuario
    global ahora

    defaultColor =  '#FFF8EF'
    ahora = datetime.now()
    lugar = {'codLocal': 1, 'nombreLocal': 'San Rafael'}
    usuario = {'idUsuario': '1234567890', 'nombre': 'Leonardo', 'apellido': 'Vidal'}

def cambiarFrame(frame):
    frame.tkraise()

def salir(root):
    root.quit()


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

    global resumenFrame
    global ventasFrame
    global formasPagoFrame
    global gastosGeneralesFrame
    global gastosPersonalFrame
    global depositosFrame


    resumenButton = tk.Button(commandFrame, text='Resumen', command=lambda:cambiarFrame(resumenFrame))
    ventasButton = tk.Button(commandFrame, text='Ventas', command=lambda:cambiarFrame(ventasFrame))
    formasPagoButton = tk.Button(commandFrame, text='Formas de Pago', command=lambda:cambiarFrame(formasPagoFrame))
    gastosGeneralesButton = tk.Button(commandFrame, text='Gastos Generales', command=lambda:cambiarFrame(gastosGeneralesFrame))
    gastosPersonalButton = tk.Button(commandFrame, text='Gastos de Personal', command=lambda:cambiarFrame(gastosPersonalFrame))
    depositosButton = tk.Button(commandFrame, text='Depósitos', command=lambda:cambiarFrame(depositosFrame))
    salirButton =tk.Button(commandFrame, text='Salir', command=lambda:salir(root))

    resumenButton.pack(fill='x', expand=True)
    ventasButton.pack(fill='x', expand=True)
    formasPagoButton.pack(fill='x', expand=True)
    gastosGeneralesButton.pack(fill='x', expand=True)
    gastosPersonalButton.pack(fill='x', expand=True)
    depositosButton.pack(fill='x', expand=True)
    salirButton.pack(fill='x', expand=True)

def crearWidgetsResumen(resumenFrame):

    global defaultColor

    resumenFrame.columnconfigure(0, weight=2)
    resumenFrame.columnconfigure(1, weight=1)

    resumenFrame.rowconfigure(0, weight=3)
    resumenFrame.rowconfigure(1, weight=1)
    resumenFrame.rowconfigure(3, weight=1)
    resumenFrame.rowconfigure(5, weight=1)
    resumenFrame.rowconfigure(7, weight=1)
    resumenFrame.rowconfigure(9, weight=1)
    resumenFrame.rowconfigure(2, weight=1)
    resumenFrame.rowconfigure(4, weight=1)
    resumenFrame.rowconfigure(6, weight=1)
    resumenFrame.rowconfigure(8, weight=1)
    resumenFrame.rowconfigure(10, weight=1)

    tituloLabel = tk.Label(resumenFrame, text='Resumen de Datos Registrados', bg=defaultColor, font=('Helvetica bold', 16))
    ventasLabel = tk.Label(resumenFrame, text='Venta Total del Día', bg=defaultColor)
    gastosGeneralesLabel = tk.Label(resumenFrame, text='Total Gastos Generales', bg=defaultColor)
    gastosPersonalLabel = tk.Label(resumenFrame, text='Total Gastos de Personal', bg=defaultColor)
    depositosLabel = tk.Label(resumenFrame, text='Total Depósitos', bg=defaultColor)
    formasPagosLabel = tk.Label(resumenFrame, text='Total recibido', bg=defaultColor)
    anulacionesLabel = tk.Label(resumenFrame, text='Anulaciones', bg=defaultColor)
    devolucionesLabel = tk.Label(resumenFrame, text='Devoluciones', bg=defaultColor)
    cortesiasLabel = tk.Label(resumenFrame, text='Total Cortesías', bg=defaultColor)
    diferenciaLabel = tk.Label(resumenFrame, text='Diferencia', bg=defaultColor)

    valorVentas = tk.Label(resumenFrame, text='10', bg='#ffffff')
    valorGastosGenerales = tk.Label(resumenFrame, text='30', bg='#ffffff')
    valorGastosPersonal = tk.Label(resumenFrame, text='50', bg='#ffffff')
    valorDepositos = tk.Label(resumenFrame, text='70', bg='#ffffff')
    valorDiferencia = tk.Label(resumenFrame, text='90', bg='#ffffff')
    valorFormasPagos = tk.Label(resumenFrame, text='11', bg='#ffffff')
    valorAnulaciones = tk.Label(resumenFrame, text='31', bg='#ffffff')
    valorDevoluciones = tk.Label(resumenFrame, text='51', bg='#ffffff')
    valorCortesias = tk.Label(resumenFrame, text='71', bg='#ffffff')

    tituloLabel.grid(row=0, column=0, columnspan=2, sticky='EW')
    ventasLabel.grid(row=1, column=0, sticky='EW')
    gastosGeneralesLabel.grid(row=3, column=0, sticky='EW')
    gastosPersonalLabel.grid(row=5, column=0,sticky='EW')
    depositosLabel.grid(row=7, column=0, sticky='EW')
    diferenciaLabel.grid(row=9, column=0, sticky='EW')
    formasPagosLabel.grid(row=1, column=1, sticky='EW')
    anulacionesLabel.grid(row=3, column=1, sticky='EW')
    devolucionesLabel.grid(row=5, column=1, sticky='EW')
    cortesiasLabel.grid(row=7, column=1, sticky='EW')

    valorVentas.grid(row=2, column=0, sticky='EW')
    valorGastosGenerales.grid(row=4, column=0, sticky='EW')
    valorGastosPersonal.grid(row=6, column=0, sticky='EW')
    valorDepositos.grid(row=8, column=0, sticky='EW')
    valorDiferencia.grid(row=10, column=0, sticky='EW')
    valorFormasPagos.grid(row=2, column=1, sticky='EW')
    valorAnulaciones.grid(row=4, column=1, sticky='EW')
    valorDevoluciones.grid(row=6, column=1, sticky='EW')
    valorCortesias.grid(row=8, column=1, sticky='EW')

def crearWidgetsVentas(ventasFrame):

    global defaultColor

    ventasFrame.columnconfigure(0, weight=1)
    ventasFrame.columnconfigure(1, weight=1)
    ventasFrame.columnconfigure(2, weight=1)
    ventasFrame.columnconfigure(3, weight=1)

    ventasFrame.rowconfigure(0, weight=3)
    ventasFrame.rowconfigure(1, weight=1)
    ventasFrame.rowconfigure(2, weight=1)
    ventasFrame.rowconfigure(3, weight=1)
    ventasFrame.rowconfigure(4, weight=1)
    ventasFrame.rowconfigure(5, weight=1)
    ventasFrame.rowconfigure(6, weight=10)

    tituloLabel = tk.Label(ventasFrame, text='Detalle de Ventas, anulaciones y Cortesías del Día', bg=defaultColor, font=('Helvetica bold', 16))
    ventasLabel = tk.Label(ventasFrame, text='Venta Total del día', bg=defaultColor)
    anulacionesLabel = tk.Label(ventasFrame, text='Anulaciones del día', bg=defaultColor)
    devolucionesLabel = tk.Label(ventasFrame, text='Devoluciones del día', bg=defaultColor)
    cortesiasLabel = tk.Label(ventasFrame, text='Cortesías de día', bg=defaultColor)
    cortesiaTipoLabel = tk.Label(ventasFrame, text='Tipo de Cortesía', bg=defaultColor)
    cortesiaValorLabel = tk.Label(ventasFrame, text='Valor de la Cortesía', bg=defaultColor)
    cortesiaObservacionLabel = tk.Label(ventasFrame, text='Observaciones', bg=defaultColor)

    ventasEntry = tk.Entry(ventasFrame)
    anulacionesEntry= tk.Entry(ventasFrame)
    devolucionesEntry= tk.Entry(ventasFrame)
    cortesiaTipoCombo = ttk.Combobox(ventasFrame)
    cortesiaTipoCombo['values'] = ['Cumpleañero', 'Cortesía del Local', 'Cortesías a empleados', 'Cortesías de Gerencia']
    cortesiaTipoCombo['state'] = 'readonly'
    cortesiaValorEntry= tk.Entry(ventasFrame)
    cortesiaObservacionEntry= tk.Entry(ventasFrame)


    tituloLabel.grid(row=0, column=0, columnspan=2, sticky='EW')
    ventasLabel.grid(row=1, column=0, stick='EW')
    anulacionesLabel.grid(row=2, column=0, stick='EW')
    devolucionesLabel.grid(row=3, column=0, stick='EW')
    cortesiaTipoLabel.grid(row=4, column=1, stick='EW')
    cortesiaValorLabel.grid(row=4, column=2, stick='EW')
    cortesiaObservacionLabel.grid(row=4, column=3, stick='EW')
    cortesiasLabel.grid(row=5, column=0, stick='EW')

    ventasEntry.grid(row=1, column=1)
    anulacionesEntry.grid(row=2, column=1, sticky='WE')
    devolucionesEntry.grid(row=3, column=1, sticky='WE')
    cortesiaTipoCombo.grid(row=5, column=1, sticky='WE')
    cortesiaValorEntry.grid(row=5, column=2)
    cortesiaObservacionEntry.grid(row=5, column=3)

    columnasCortesias =('tipo', 'valor', 'observacion')
    cortesiasTree = ttk.Treeview(ventasFrame, columns=columnasCortesias, show='headings')
    cortesiasTree.heading('tipo', text='Tipo de Cortesía')
    cortesiasTree.heading('valor', text='Valor de Cortesía')
    cortesiasTree.heading('observacion', text='Observaciones')

    cortesiasTree.grid(row=6, column=0, columnspan=4, sticky='nswe')

def crearWidgetsFormasPago(formasPagoFrame):
   global defaultColor

   

def crearWigetsgastosGenerales(gastosGeneralesFrame):
    global defaultColor

def crearWigetsgastosPersonal(gastosPersonalFrame):
    global defaultColor

def crearWigetsgastosPersonal(gastosPersonalFrame):
    global defaultColor

def crearDataFrames(dataFrame, root):

    global resumenFrame
    global ventasFrame
    global formasPagoFrame
    global gastosGeneralesFrame
    global gastosPersonalFrame
    global depositosFrame

    resumenFrame = tk.Frame(dataFrame, bg=defaultColor, highlightthickness=1)
    resumenFrame.grid(row=0, column=0, sticky='nsew')
    crearWidgetsResumen(resumenFrame)

    ventasFrame = tk.Frame(dataFrame, bg=defaultColor, highlightthickness=1)
    ventasFrame.grid(row=0, column=0, sticky='nsew')
    crearWidgetsVentas(ventasFrame)

    formasPagoFrame = tk.Frame(dataFrame, bg=defaultColor, highlightthickness=1)
    formasPagoFrame.grid(row=0, column=0, sticky='nsew')
    crearWidgetsFormasPago(formasPagoFrame)

    gastosGeneralesFrame = tk.Frame(dataFrame, bg=defaultColor, highlightthickness=1)
    gastosGeneralesFrame.grid(row=0, column=0, sticky='nsew')
    crearWigetsgastosGenerales(gastosGeneralesFrame)

    gastosPersonalFrame = tk.Frame(dataFrame, bg=defaultColor, highlightthickness=1)
    gastosPersonalFrame.grid(row=0, column=0, sticky='nsew')
    crearWigetsgastosPersonal(gastosPersonalFrame)

    depositosFrame = tk.Frame(dataFrame, bg=defaultColor, highlightthickness=1)
    depositosFrame.grid(row=0, column=0, sticky='nsew')
    crearWigetsgastosPersonal(gastosPersonalFrame)

    resumenFrame.tkraise()
    

def crearFrames(root):

    global defaultColor

    headerFrame = tk.Frame(root, bg=defaultColor)
    headerFrame.pack(fill='x')
    crearWidgetsHeader(headerFrame, root)

    commandFrame = tk.Frame(root, bg=defaultColor, highlightthickness=1)
    commandFrame.pack(side='left', fill='y')
    crearWidgetsCommand(commandFrame, root)

    dataFrame = tk.Frame(root, bg=defaultColor, highlightthickness=1)
    dataFrame.pack(side='left', fill='both', expand=True)
    crearDataFrames(dataFrame, root)


def cerrarVentana(root):
    salir(root)

def main():

    global defaultColor
    root = tk.Tk()

    root.protocol('WM_DELETE_WINDOW', cerrarVentana(root))

    root.geometry('800x600')
    root.config(bg=defaultColor)
    root.title('Sistema de registro de datos')

    # rootStyle = ttk.Style(root)

    # rootStyle.configure('TLabel', bg=defaultColor)
    # rootStyle.configure('TFrame', bg=defaultColor)
   
    cargarDatosGlobales()
    crearFrames(root)

    root.mainloop()


if __name__ == '__main__':
    main()
