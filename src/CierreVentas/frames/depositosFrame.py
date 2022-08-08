import tkinter as tk
from tkinter import ttk

class DepositosFrame(ttk.Frame):
    def __init__(self, dataFrame):
        super().__init__(dataFrame)

        self.df = dataFrame
        
        self.grid(row=0, column=0, sticky='nsew')

        dataFrame.gridConfigure(self)
        self.crearWidgets()

    def crearWidgets(self):
        pass


# tituloLabel = tk.Label(depositosFrame, text='Detalle de Formas de Pago de Clientes', bg=defaultColor, font=('Helvetica bold', 16))
#     bancoDepositosLabel = tk.Label(depositosFrame, text='Forma de Pago', bg=defaultColor)
#     valorDepositosLabel =tk.Label(depositosFrame, text='Valor', bg=defaultColor)
#     observacionDepositosLabel = tk.Label(depositosFrame, text='Valor Recibido en Efectivo', bg=defaultColor)

#     bancoDepositosCombo = ttk.Combobox(depositosFrame)
#     bancoDepositosCombo['values'] = ['Banco del Pichincha']
#     bancoDepositosCombo['state'] = 'readonly' 
#     valorDepositosEntry = tk.Entry(depositosFrame)
#     observacionDepositosEntry = tk.Entry(depositosFrame)

#     columnasDepositos = ('banco', 'valor', 'observacion')
#     depositosTree = ttk.Treeview(depositosFrame, columns=columnasDepositos, show='headings')
#     depositosTree.heading('banco', text='Banco')
#     depositosTree.heading('valor', text='Valores')
#     depositosTree.heading('observacion', text='Observaciones')

#     tituloLabel.grid(row=0, column=0, columnspan=3, sticky='WE')
 
#     bancoDepositosLabel.grid(row=1, column=0, sticky='WE')
#     valorDepositosLabel.grid(row=1, column=1, sticky='WE')
#     observacionDepositosLabel.grid(row=1, column=2, sticky='WE')
#     bancoDepositosCombo.grid(row=2, column=0, sticky='WE')
#     valorDepositosEntry.grid(row=2, column=1, sticky='WE')
#     observacionDepositosEntry.grid(row=2, column=2, sticky='WE')

#     depositosTree.grid(row=3, column=0, columnspan=3, sticky='nswe', pady=10)