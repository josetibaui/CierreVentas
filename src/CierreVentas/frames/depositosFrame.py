import tkinter as tk
from tkinter import ttk
from modelo.baBancos import Bancos

class DepositosFrame(ttk.Frame):
    def __init__(self, dataFrame):
        super().__init__(dataFrame)

        self.df = dataFrame
        
        self.grid(row=0, column=0, sticky='nsew')

        # dataFrame.gridConfigure(self)
        self.crearWidgets()

    def crearWidgets(self):
        estilo = ttk.Style(self)
        estilo.configure('TLabel', background=self.df.defaultColor)
        estilo.configure('TFrame', background=self.df.defaultColor)
        estilo.configure('Values.TLabel', relief='ridge')
        estilo.configure('TCombobox', background=self.df.defaultColor)
        estilo.configure('TEntry', width=10, borderwidth=1, background=self.df.defaultColor)
        labelsOptions = {'sticky': 'w', 'padx': 20, 'pady': 5}
        valuesOptions = {'sticky': 'e', 'padx': 20, 'pady': 5}
        labelsColumnsOptions = {'sticky': 'n', 'padx': 10, 'pady': 5}

        tituloLabel = ttk.Label(self, text='Detalle de Valores a Depositar', font=('Helvetica bold', 16))
        tituloLabel.grid(row=0, column=0, columnspan=4, pady=5, sticky='n')

        bancoDepositosLabel = ttk.Label(self, text='Forma de Pago')
        bancoDepositosLabel.grid(row=1, column=0, **labelsColumnsOptions)

        valorDepositosLabel =ttk.Label(self, text='Valor')
        valorDepositosLabel.grid(row=1, column=1, **labelsColumnsOptions)

        observacionDepositosLabel = ttk.Label(self, text='Valor Recibido en Efectivo')
        observacionDepositosLabel.grid(row=1, column=2, **labelsColumnsOptions)

        bancos = Bancos()
        listaBancos = bancos.queryAll()
        self.bancoDepositosCombo = ttk.Combobox(self)
        self.bancoDepositosCombo['values'] = [banco[1] for banco in listaBancos]
        self.bancoDepositosCombo['state'] = 'readonly' 
        self.bancoDepositosCombo.grid(row=2, column=0)
        
        valorDepositosEntry = tk.Entry(self)
        valorDepositosEntry.grid(row=2, column=1, **valuesOptions)

        observacionDepositosEntry = tk.Entry(self)
        observacionDepositosEntry.grid(row=2, column=2, **valuesOptions)

        columnasDepositos = ('banco', 'valor', 'observacion')
        depositosTree = ttk.Treeview(self, columns=columnasDepositos, show='headings')
        depositosTree.heading('banco', text='Banco')
        depositosTree.heading('valor', text='Valores')
        depositosTree.heading('observacion', text='Observaciones')
        depositosTree.grid(row=3, column=0, columnspan=3, sticky='nswe', pady=10)

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