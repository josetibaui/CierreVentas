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
    formasPagosLabel = tk.Label(resumenFrame, text='Total de Formas de Pago', bg=defaultColor)
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

    tituloLabel.grid(row=0, column=0, columnspan=2, sticky='WE')
    ventasLabel.grid(row=1, column=0, sticky='WE')
    gastosGeneralesLabel.grid(row=3, column=0, sticky='WE')
    gastosPersonalLabel.grid(row=5, column=0,sticky='WE')
    depositosLabel.grid(row=7, column=0, sticky='WE')
    diferenciaLabel.grid(row=9, column=0, sticky='WE')
    formasPagosLabel.grid(row=1, column=1, sticky='WE')
    anulacionesLabel.grid(row=3, column=1, sticky='WE')
    devolucionesLabel.grid(row=5, column=1, sticky='WE')
    cortesiasLabel.grid(row=7, column=1, sticky='WE')

    valorVentas.grid(row=2, column=0, sticky='WE')
    valorGastosGenerales.grid(row=4, column=0, sticky='WE')
    valorGastosPersonal.grid(row=6, column=0, sticky='WE')
    valorDepositos.grid(row=8, column=0, sticky='WE')
    valorDiferencia.grid(row=10, column=0, sticky='WE')
    valorFormasPagos.grid(row=2, column=1, sticky='WE')
    valorAnulaciones.grid(row=4, column=1, sticky='WE')
    valorDevoluciones.grid(row=6, column=1, sticky='WE')
    valorCortesias.grid(row=8, column=1, sticky='WE')

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


    tituloLabel.grid(row=0, column=0, columnspan=4, sticky='WE')
    ventasLabel.grid(row=1, column=0, sticky='WE')
    anulacionesLabel.grid(row=2, column=0, sticky='WE')
    devolucionesLabel.grid(row=3, column=0, sticky='WE')
    cortesiaTipoLabel.grid(row=4, column=1, sticky='WE')
    cortesiaValorLabel.grid(row=4, column=2, sticky='WE')
    cortesiaObservacionLabel.grid(row=4, column=3, sticky='WE')
    cortesiasLabel.grid(row=5, column=0, sticky='WE')

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

    cortesiasTree.grid(row=6, column=0, columnspan=4, sticky='nswe', pady=10)

def crearWidgetsFormasPago(formasPagoFrame):
    global defaultColor

    tituloLabel = tk.Label(formasPagoFrame, text='Detalle de Formas de Pago de Clientes', bg=defaultColor, font=('Helvetica bold', 16))
    tipoFormasPagoLabel = tk.Label(formasPagoFrame, text='Forma de Pago', bg=defaultColor)
    valorFormasPagoLabel =tk.Label(formasPagoFrame, text='Valor', bg=defaultColor)
    efectivoLabel = tk.Label(formasPagoFrame, text='Valor Recibido en Efectivo', bg=defaultColor)
    efectivoValor = tk.Label(formasPagoFrame, text='0', bg='#ffffff')

    tipoFormasPagoCombo = ttk.Combobox(formasPagoFrame)
    tipoFormasPagoCombo['values'] = ['Medianet', 'DataFast', 'Cheque', 'Transferencia', 'Retención IR']
    tipoFormasPagoCombo['state'] = 'readonly' 
    valorFormasPagoEntry = tk.Entry(formasPagoFrame)

    columnasFormasPago = ('tipoFormasPago', 'valor')
    formasPagoTree = ttk.Treeview(formasPagoFrame, columns=columnasFormasPago, show='headings')
    formasPagoTree.heading('tipoFormasPago', text='Formas de Pago')
    formasPagoTree.heading('valor', text='Valores')

    tituloLabel.grid(row=0, column=0, columnspan=2, sticky='WE')
    tipoFormasPagoLabel.grid(row=1, column=0, sticky='WE')
    valorFormasPagoLabel.grid(row=1, column=1, sticky='WE')
    efectivoLabel.grid(row=1, column=2, sticky='WE')
    efectivoValor.grid(row=2, column=3, sticky='WE')
    tipoFormasPagoCombo.grid(row=2, column=0, sticky='WE')
    valorFormasPagoEntry.grid(row=2, column=1, sticky='WE')

    formasPagoTree.grid(row=3, column=0, columnspan=3, sticky='nswe', pady=10)

def crearWigetsgastosGenerales(gastosGeneralesFrame):
    global defaultColor

    tituloLabel = tk.Label(gastosGeneralesFrame, text='Detalle de Gastos', bg=defaultColor, font=('Helvetica bold', 16))
    tipoGastoGeneralLabel = tk.Label(gastosGeneralesFrame, text='Tipo de Gastos', bg=defaultColor)
    valorGastoGeneralLabel =tk.Label(gastosGeneralesFrame, text='Valor del Gasto', bg=defaultColor)
    localOrigenGastoGeneralLabel = tk.Label(gastosGeneralesFrame, text='Local de Origen del Gastos', bg=defaultColor)
    obserbacionGastoGeneralLabel =tk.Label(gastosGeneralesFrame, text='Observaciones', bg=defaultColor)

    tipoGastoGeneralCombo = ttk.Combobox(gastosGeneralesFrame)
    tipoGastoGeneralCombo['values'] = ['Pago de sueldos',
                                        'Pago a eventuales',
                                        'Pago días libres',
                                        'Transporte',
                                        'Mantenimientos',
                                        'Compras de insumos',
                                        'Cuenta auxiliar']
    tipoGastoGeneralCombo['state'] = 'readonly' 
    valorGastoGeneralEntry = tk.Entry(gastosGeneralesFrame)
    localOrigenGastoGeneralCombo = ttk.Combobox(gastosGeneralesFrame)
    localOrigenGastoGeneralCombo['values'] = [  ' 1 - La Carolina',
                                                ' 2 - Plaza de Toros',
                                                ' 3 - La Magdalena',
                                                ' 4 - San Rafael',
                                                ' 5 - Cotocollao',
                                                ' 6 - C.C. El Recreo',
                                                ' 7 - C.C. Quicentro Sur',
                                                ' 8 - C.C. San Luis',
                                                '10 - Mall de Los Andes',
                                                '11 - Mall El Jardín',
                                                '12 - C.C. El Paseo Shopping',
                                                '13 - C.C. Quincentro Norte'
                                                ]
    localOrigenGastoGeneralCombo['state'] = 'readonly'
    observacionGastoGeneralEntry = tk.Entry(gastosGeneralesFrame)

    columnasGastosGenerales = ('tipoGastoGeneral', 'valorGastoGeneral', 'localOrigenGastoGeneral', 'observaciones')
    gastosGeneralesTree = ttk.Treeview(gastosGeneralesFrame, columns=columnasGastosGenerales, show='headings')
    gastosGeneralesTree.heading('tipoGastoGeneral', text='Tipo de Gasto')
    gastosGeneralesTree.heading('valorGastoGeneral', text='Valor del Gasto')
    gastosGeneralesTree.heading('localOrigenGastoGeneral', text='Local de Origen')
    gastosGeneralesTree.heading('observaciones', text='Observaciones')

    tituloLabel.grid(row=0, column=0, columnspan=4, sticky='WE')
    tipoGastoGeneralLabel.grid(row=1, column=0, sticky='WE')
    valorGastoGeneralLabel.grid(row=1, column=1, sticky='WE')
    localOrigenGastoGeneralLabel.grid(row=1, column=2, sticky='WE')
    obserbacionGastoGeneralLabel.grid(row=1, column=3, sticky='WE')

    tipoGastoGeneralCombo.grid(row=2, column=0, sticky='WE')
    valorGastoGeneralEntry.grid(row=2, column=1, sticky='WE')
    localOrigenGastoGeneralCombo.grid(row=2, column=2, sticky='WE')
    observacionGastoGeneralEntry.grid(row=2, column=3, sticky='WE')

    gastosGeneralesTree.grid(row=3, column=0, columnspan=4, sticky='nswe', pady=10)

def crearWigetsGastosPersonal(gastosPersonalFrame):
    global defaultColor

    tituloLabel = tk.Label(gastosPersonalFrame, text='Detalle de Gastos de Personal', bg=defaultColor, font=('Helvetica bold', 16))

    empleadoLabel = tk.Label(gastosPersonalFrame, text='Empleado', bg=defaultColor)
    tipoGastosPersonalLabel = tk.Label(gastosPersonalFrame, text='Tipo de Gasto', bg=defaultColor)
    valorGastosPersonalLabel = tk.Label(gastosPersonalFrame, text='Valor', bg=defaultColor)
    observacionGastosPersonalLabel = tk.Label(gastosPersonalFrame, text='Observaciones', bg=defaultColor)

    empleadoCombo = ttk.Combobox(gastosPersonalFrame)
    empleadoCombo['values'] = [
                    'Avila Moreira Daisy Veronica ',
                    'Bedoya Chiluisa Juan Fidel ',
                    'Bone Mera Marcos Eduardo',
                    'Bone Mera Vanesa Anabela',
                    'Bonifaz Salazar Karlita Lucia',
                    'Borja Diaz Jessica Tatiana',
                    'Bravo Alcivar Leopoldina Maribel',
                    'Burgos Bustamante Jose Luis',
                    'Burgos Bustamante Segundo José ',
                    'Carpio Burgos Jose Agustin',
                    'Castro Seas Geomara Alexandra',
                    'Cedeño Gomez Wilson Onofre',
                    'Cedeño Zambrano Nancy Lilibeth',
                    'Cevallos Alvarado Pedro Pablo',
                    'Chimbolema Moposita Maria Mercedes',
                    'Chinche Analuisa Diana Carolina ',
                    'Chisag Chimbolema William Oswaldo ',
                    'Coronel Toledo Eduardo Enrique',
                    'Cortes Torres Flor Magaly',
                    'Cuasapud Yaguapaz Blanca Rubiela ',
                    'De Souza Mendoza Andrea Soraya',
                    'Delgado Ramirez Manuel Estalin ',
                    'Fajardo Peñafiel Richar Uber',
                    'Gaibor Cerruffo Erick Sebastian',
                    'Gordillo Cellan Victor Manuel',
                    'Gordillo Rosero Enma del Rocio',
                    'Gracia Velez Genesis Milady',
                    'Gualan Correa Jacqueline Sesibel',
                    'Gutierres Chacon Edison Fernando ',
                    'Jaya Quezada Rocio del Carmen',
                    'Loor Delgado Robert Rene',
                    'Loor Saltos Marcos Gregorio',
                    'Lopez Rubio Luis Alberto',
                    'Machado Galet Hilda ',
                    'Melendez Carvajal Arianne Elizabeth ',
                    'Mendez Ortiz Katherine Estefania ',
                    'Mendoza Fajardo Jessica Alexandra',
                    'Mera Quiroz Blanca Dolores',
                    'Moncerrate Guanipatin Alexi Mariano',
                    'Monserrate Vasquez Pedro Victor',
                    'Morales Perugachi Irene Alexandra',
                    'Moreno Guerrero Nagelly Lisseth',
                    'Padilla Mendez Magaly Beatriz',
                    'Parraga Baquerizo Jaime Antonio',
                    'Pelaes Cevallos Nancy del Rocio',
                    'Peñarrieta Velez Carlos Alfredo',
                    'Peñarrieta Velez Lenny del Rosario',
                    'Peñarrieta Velez Rosa Alexandra',
                    'Piedra Ruiz Rosa Margarita',
                    'Pilco Parco Lorena Patricia ',
                    'Piza Cela Vicente Orlando',
                    'Polo Carillo Julia Aracely',
                    'Ramos Acosta Rosmery Bellatriz',
                    'Reyes Medina Gladys Maria',
                    'Rivadeneira Muñoz Karina Lisbeth',
                    'Romero Hurtado Joselyn Gabriela',
                    'Rua Micolta Nancy Janeth',
                    'Sanchez Peñarrieta Francisco Roberto',
                    'Shiguango Mamallacta Jimmy Henry',
                    'Shiguango Mamallacta Maria Margarita',
                    'Silva Mera Jeniffer Angelica ',
                    'Silva Mera Roxana Lilibeth',
                    'Simba Freire Carlos Andres ',
                    'Solá Cheme Shirley Camila',
                    'Soto Malacatus Carmen Dolores',
                    'Soto Malacatus Vicente Felipe',
                    'Tandalla Guananga Diego Francisco ',
                    'Tapia Gomez Jesus Nazareno',
                    'Tiviano Punina Edison Mauricio ',
                    'Troya Morales Maria Salome ',
                    'Valdez Medina Leandro',
                    'Vegas Maldonado Fabiola Jhojanna',
                    'Velasco Quiñonez John Janner ',
                    'Velez Cedeño Gissela Janeth ',
                    'Velez Cedeño Shirley Rossibel',
                    'Velez Ganchozo Gissela Jazmin ',
                    'Vera Vasquez Jefferson Bernardino',
                    'Vidal Pazmiño Edison Leonardo',
                    'Vite Vaca Fannis',
                    'Zambrano Loor Mercy Magdalena',
                    'Zambrano Navarrete Gustavo Fabian'
    ]
    empleadoCombo['state'] = 'readonly'

    tipoGastosPersonalCombo = ttk.Combobox(gastosPersonalFrame)
    tipoGastosPersonalCombo['values'] = ['Préstamo', 'Anticipo']
    tipoGastosPersonalCombo['state'] = 'readonly'

    valorGastosPersonalEntry = tk.Entry(gastosPersonalFrame)
    observacionGastosPersonalEntry = tk.Entry(gastosPersonalFrame)

    columnasGastosPersonal = ('empleado', 'tipoGastosPersonal', 'valorGastosPersonal', 'observaciones')
    gastosPersonalTree = ttk.Treeview(gastosPersonalFrame, columns=columnasGastosPersonal, show='headings')
    gastosPersonalTree.heading('empleado', text='Empleado')
    gastosPersonalTree.heading('tipoGastosPersonal', text='Tipo de Gasto')
    gastosPersonalTree.heading('valorGastosPersonal', text='Valor')
    gastosPersonalTree.heading('observaciones', text='Observaciones')

    tituloLabel.grid(row=0, column=0, columnspan=4, sticky='WE')

    empleadoLabel.grid(row=1, column=0, sticky='WE')
    tipoGastosPersonalLabel.grid(row=1, column=1, sticky='WE')
    valorGastosPersonalLabel.grid(row=1, column=2, sticky='WE')
    observacionGastosPersonalLabel.grid(row=1, column=3, sticky='WE')

    empleadoCombo.grid(row=2, column=0, sticky='WE')
    tipoGastosPersonalCombo.grid(row=2, column=1, sticky='WE')
    valorGastosPersonalEntry.grid(row=2, column=2, sticky='WE')
    observacionGastosPersonalEntry.grid(row=2, column=3, sticky='WE')

    gastosPersonalTree.grid(row=3, column=0, columnspan=4, sticky='nswe', pady=10)

def crearWigetsDepositos(depositosFrame):
    global defaultColor
    
    tituloLabel = tk.Label(depositosFrame, text='Detalle de Depósitos', bg=defaultColor, font=('Helvetica bold', 16))
    bancoDepositosLabel = tk.Label(depositosFrame, text='Banco', bg=defaultColor)
    valorDepositosLabel =tk.Label(depositosFrame, text='Valor', bg=defaultColor)
    observacionDepositosLabel = tk.Label(depositosFrame, text='Observaciones', bg=defaultColor)
    valorADepositarLabel = tk.Label(depositosFrame, text='Valor a Depositar', bg=defaultColor)

    bancoDepositosCombo = ttk.Combobox(depositosFrame)
    bancoDepositosCombo['values'] = ['Banco del Pichincha']
    bancoDepositosCombo['state'] = 'readonly' 
    valorDepositosEntry = tk.Entry(depositosFrame)
    observacionDepositosEntry = tk.Entry(depositosFrame)
    valorSugeridoLabel = tk.Label(depositosFrame, text='', bg='#ffffff')

    columnasDepositos = ('banco', 'valor', 'observacion')
    depositosTree = ttk.Treeview(depositosFrame, columns=columnasDepositos, show='headings')
    depositosTree.heading('banco', text='Banco')
    depositosTree.heading('valor', text='Valores')
    depositosTree.heading('observacion', text='Observaciones')

    tituloLabel.grid(row=0, column=0, columnspan=3, sticky='WE')
 
    bancoDepositosLabel.grid(row=1, column=0, sticky='WE')
    valorDepositosLabel.grid(row=1, column=1, sticky='WE')
    observacionDepositosLabel.grid(row=1, column=2, sticky='WE')
    valorADepositarLabel.grid(row=1, column=3, sticky='WE')
    bancoDepositosCombo.grid(row=2, column=0, sticky='WE')
    valorDepositosEntry.grid(row=2, column=1, sticky='WE')
    observacionDepositosEntry.grid(row=2, column=2, sticky='WE')
    valorSugeridoLabel.grid(row=2, column=3, sticky='WE')

    depositosTree.grid(row=3, column=0, columnspan=3, sticky='nswe', pady=10)

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
    crearWigetsGastosPersonal(gastosPersonalFrame)

    depositosFrame = tk.Frame(dataFrame, bg=defaultColor, highlightthickness=1)
    depositosFrame.grid(row=0, column=0, sticky='nsew')
    crearWigetsDepositos(depositosFrame)

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

    root.geometry('960x600')
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
