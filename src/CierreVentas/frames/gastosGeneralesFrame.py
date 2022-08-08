import tkinter as tk
from tkinter import ttk

class GastosGeneralesFrame(ttk.Frame):
    def __init__(self, dataFrame):
        super().__init__(dataFrame)

        self.df = dataFrame
        
        self.grid(row=0, column=0, sticky='nsew')

        dataFrame.gridConfigure(self)
        self.crearWidgets()

    def crearWidgets(self):

        estilo = ttk.Style(self)
        estilo.configure('TLabel', background=self.df.defaultColor)
        estilo.configure('TEntry', width=10, borderwidth=1, background=self.df.defaultColor)
        stickyLabelsOptions = {'sticky': 'we', 'padx': 20, 'pady': 5}
        stickyLabelsEntryOptions = {'sticky': 'we', 'padx': 20, 'pady': 15}
        stickyEntryOptions = {'sticky': 'we', 'padx': 20, 'pady': 5}

        tituloLabel = ttk.Label(self, text='Detalle de Gastos', font=('Helvetica bold', 16))
        tituloLabel.grid(row=0, column=0, columnspan=4, pady=20, sticky='n')



        tipoGastoGeneralLabel = ttk.Label(self, text='Tipos de Gastos')
        valorGastoGeneralLabel =tk.Label(self, text='Valor del Gasto')
        localOrigenGastoGeneralLabel = tk.Label(self, text='Local de Origen del Gasto')
        obserbacionGastoGeneralLabel =tk.Label(self, text='Observaciones')

        tipoGastoGeneralCombo = ttk.Combobox(self)
        tipoGastoGeneralCombo['values'] = ['Pago de sueldos',
                                        'Pago a eventuales',
                                        'Pago días libres',
                                        'Transporte',
                                        'Mantenimientos',
                                        'Compras de insumos',
                                        'Cuenta auxiliar']
        tipoGastoGeneralCombo['state'] = 'readonly' 
        valorGastoGeneralEntry = ttk.Entry(self)
        localOrigenGastoGeneralCombo = ttk.Combobox(self)
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
        observacionGastoGeneralEntry = ttk.Entry(self) 


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