import tkinter as tk
from tkinter import ttk
from modelo.locEgresos import Egresos as GastosGenerales
from modelo.igLocales import Locales as Locales

class GastosGeneralesFrame(ttk.Frame):
    def __init__(self, dataFrame):
        super().__init__(dataFrame)

        self.df = dataFrame
        
        self.grid(row=0, column=0, sticky='nsew')

        # dataFrame.gridConfigure(self)
        self.crearWidgets()

    def crearWidgets(self):

        estilo = ttk.Style(self)
        estilo.configure('TLabel', background=self.df.defaultColor)
        estilo.configure('Values.TLabel', relief='ridge')
        estilo.configure('TCombobox', background=self.df.defaultColor)
        estilo.configure('TEntry', width=10, borderwidth=1, background=self.df.defaultColor)
        labelsOptions = {'sticky': 'w', 'padx': 20, 'pady': 5}
        valuesOptions = {'sticky': 'e', 'padx': 20, 'pady': 5}
        labelsColumnsOptions = {'sticky': 'n', 'padx': 5, 'pady': 5}

        tituloLabel = ttk.Label(self, text='Detalle de Gastos', font=('Helvetica bold', 16))
        tituloLabel.grid(row=0, column=0, columnspan=4, pady=5, sticky='n')


        tipoGastoGeneralLabel = ttk.Label(self, text='Tipos de Gastos')
        tipoGastoGeneralLabel.grid(row=1,column=0, **labelsColumnsOptions)

        valorGastoGeneralLabel = ttk.Label(self, text='Valor del Gasto')
        valorGastoGeneralLabel.grid(row=1,column=1, **labelsColumnsOptions)
        
        localOrigenGastoGeneralLabel = ttk.Label(self, text='Local de Origen del Gasto')
        localOrigenGastoGeneralLabel.grid(row=1,column=2, **labelsColumnsOptions)

        obserbacionGastoGeneralLabel = ttk.Label(self, text='Observaciones')
        obserbacionGastoGeneralLabel.grid(row=1,column=3, **labelsColumnsOptions)

        gastosGenerales = GastosGenerales()
        listaGastosGenerales = gastosGenerales.queryAll()
        self.tipoGastoGeneralCombo = ttk.Combobox(self)
        self.tipoGastoGeneralCombo['values'] = [gasto[1] for gasto in listaGastosGenerales]
        self.tipoGastoGeneralCombo['state'] = 'readonly'
        self.tipoGastoGeneralCombo.grid(row=2, column=0)

        valorGastoGeneralEntry = ttk.Entry(self)
        valorGastoGeneralEntry.grid(row=2, column=1, **valuesOptions)
        
        locales = Locales()
        listaLocales = locales.queryAll()
        listaLocalesDisplay = [f'{local[1]} - {local[2]}' for local in listaLocales if local[0] != self.df.rw.esteLocal[0]]
        listaLocalesDisplay.insert(0,'')
        localOrigenGastoGeneralCombo = ttk.Combobox(self)
        localOrigenGastoGeneralCombo['values'] = listaLocalesDisplay
        localOrigenGastoGeneralCombo['state'] = 'readonly'
        localOrigenGastoGeneralCombo.grid(row=2, column=2)

        observacionGastoGeneralEntry = ttk.Entry(self) 
        observacionGastoGeneralEntry.grid(row=2, column=3, **valuesOptions)

        columnasGastosGenerales = ('tipoGastoGeneral', 'valorGastoGeneral', 'localOrigenGastoGeneral', 'observaciones')
        gastosGeneralesTree = ttk.Treeview(self, columns=columnasGastosGenerales, show='headings')
        gastosGeneralesTree.heading('tipoGastoGeneral', text='Tipo de Gasto')
        gastosGeneralesTree.heading('valorGastoGeneral', text='Valor del Gasto')
        gastosGeneralesTree.heading('localOrigenGastoGeneral', text='Local de Origen')
        gastosGeneralesTree.heading('observaciones', text='Observaciones')

        gastosGeneralesTree.grid(row=3, column=0, columnspan=4, sticky='nswe', pady=10)

# tituloLabel = tk.Label(gastosGeneralesFrame, text='Detalle de Gastos', bg=defaultColor, font=('Helvetica bold', 16))
#     tipoGastoGeneralLabel = tk.Label(gastosGeneralesFrame, text='Tipo de Gastos', bg=defaultColor)
#     valorGastoGeneralLabel =tk.Label(gastosGeneralesFrame, text='Valor del Gasto', bg=defaultColor)
#     localOrigenGastoGeneralLabel = tk.Label(gastosGeneralesFrame, text='Local de Origen del Gastos', bg=defaultColor)
#     obserbacionGastoGeneralLabel =tk.Label(gastosGeneralesFrame, text='Observaciones', bg=defaultColor)

#     tipoGastoGeneralCombo = ttk.Combobox(gastosGeneralesFrame)
#     tipoGastoGeneralCombo['values'] = ['Pago de sueldos',
#                                         'Pago a eventuales',
#                                         'Pago días libres',
#                                         'Transporte',
#                                         'Mantenimientos',
#                                         'Compras de insumos',
#                                         'Cuenta auxiliar']
#     tipoGastoGeneralCombo['state'] = 'readonly' 
#     valorGastoGeneralEntry = tk.Entry(gastosGeneralesFrame)
#     localOrigenGastoGeneralCombo = ttk.Combobox(gastosGeneralesFrame)
#     localOrigenGastoGeneralCombo['values'] = [  ' 1 - La Carolina',
#                                                 ' 2 - Plaza de Toros',
#                                                 ' 3 - La Magdalena',
#                                                 ' 4 - San Rafael',
#                                                 ' 5 - Cotocollao',
#                                                 ' 6 - C.C. El Recreo',
#                                                 ' 7 - C.C. Quicentro Sur',
#                                                 ' 8 - C.C. San Luis',
#                                                 '10 - Mall de Los Andes',
#                                                 '11 - Mall El Jardín',
#                                                 '12 - C.C. El Paseo Shopping',
#                                                 '13 - C.C. Quincentro Norte'
#                                                 ]
#     localOrigenGastoGeneralCombo['state'] = 'readonly'
#     observacionGastoGeneralEntry = tk.Entry(gastosGeneralesFrame)

#     columnasGastosGenerales = ('tipoGastoGeneral', 'valorGastoGeneral', 'localOrigenGastoGeneral', 'observaciones')
#     gastosGeneralesTree = ttk.Treeview(gastosGeneralesFrame, columns=columnasGastosGenerales, show='headings')
#     gastosGeneralesTree.heading('tipoGastoGeneral', text='Tipo de Gasto')
#     gastosGeneralesTree.heading('valorGastoGeneral', text='Valor del Gasto')
#     gastosGeneralesTree.heading('localOrigenGastoGeneral', text='Local de Origen')
#     gastosGeneralesTree.heading('observaciones', text='Observaciones')

#     tituloLabel.grid(row=0, column=0, columnspan=4, sticky='WE')
#     tipoGastoGeneralLabel.grid(row=1, column=0, sticky='WE')
#     valorGastoGeneralLabel.grid(row=1, column=1, sticky='WE')
#     localOrigenGastoGeneralLabel.grid(row=1, column=2, sticky='WE')
#     obserbacionGastoGeneralLabel.grid(row=1, column=3, sticky='WE')

#     tipoGastoGeneralCombo.grid(row=2, column=0, sticky='WE')
#     valorGastoGeneralEntry.grid(row=2, column=1, sticky='WE')
#     localOrigenGastoGeneralCombo.grid(row=2, column=2, sticky='WE')
#     observacionGastoGeneralEntry.grid(row=2, column=3, sticky='WE')

#     gastosGeneralesTree.grid(row=3, column=0, columnspan=4, sticky='nswe', pady=10)