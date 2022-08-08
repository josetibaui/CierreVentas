import tkinter as tk
from tkinter import ttk

class FormasPagosFrame(ttk.Frame):
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

        tituloLabel = ttk.Label(self, text='Detalle de Formas de Pago de Clientes', font=('Helvetica bold', 16))
        tituloLabel.grid(row=0, column=0, columnspan=4, pady=20, sticky='n')

        tipoFormasPagoLabel = ttk.Label(self, text='Forma de Pago')
        valorFormasPagoLabel =ttk.Label(self, text='Valor')
        efectivoLabel = ttk.Label(self, text='Valor Recibido en Efectivo')
        efectivoValor = ttk.Label(self, text='0.00')

        tipoFormasPagoCombo = ttk.Combobox(self)
        tipoFormasPagoCombo['values'] = ['Medianet', 'DataFast', 'Cheque', 'Transferencia', 'Retención IR']
        tipoFormasPagoCombo['state'] = 'readonly' 
        valorFormasPagoEntry = tk.Entry(self)

        columnasFormasPago = ('tipoFormasPago', 'valor')
        formasPagoTree = ttk.Treeview(self, columns=columnasFormasPago, show='headings')
        formasPagoTree.heading('tipoFormasPago', text='Formas de Pago')
        formasPagoTree.heading('valor', text='Valores')

        tituloLabel.grid(row=0, column=0, columnspan=2, sticky='WE')
        tipoFormasPagoLabel.grid(row=1, column=0, sticky='WE')
        valorFormasPagoLabel.grid(row=1, column=1, sticky='WE')
        efectivoLabel.grid(row=1, column=2, sticky='WE')
        efectivoValor.grid(row=2, column=3, sticky='WE')
        tipoFormasPagoCombo.grid(row=2, column=0, sticky='WE')
        valorFormasPagoEntry.grid(row=2, column=1, sticky='WE')




    # tituloLabel = tk.Label(formasPagoFrame, text='Detalle de Formas de Pago de Clientes', bg=defaultColor, font=('Helvetica bold', 16))
    # tipoFormasPagoLabel = tk.Label(formasPagoFrame, text='Forma de Pago', bg=defaultColor)
    # valorFormasPagoLabel =tk.Label(formasPagoFrame, text='Valor', bg=defaultColor)
    # efectivoLabel = tk.Label(formasPagoFrame, text='Valor Recibido en Efectivo', bg=defaultColor)
    # efectivoValor = tk.Label(formasPagoFrame, text='0', bg='#ffffff')
# 
    # tipoFormasPagoCombo = ttk.Combobox(formasPagoFrame)
    # tipoFormasPagoCombo['values'] = ['Medianet', 'DataFast', 'Cheque', 'Transferencia', 'Retención IR']
    # tipoFormasPagoCombo['state'] = 'readonly' 
    # valorFormasPagoEntry = tk.Entry(formasPagoFrame)
# 
    # columnasFormasPago = ('tipoFormasPago', 'valor')
    # formasPagoTree = ttk.Treeview(formasPagoFrame, columns=columnasFormasPago, show='headings')
    # formasPagoTree.heading('tipoFormasPago', text='Formas de Pago')
    # formasPagoTree.heading('valor', text='Valores')
# 
    # tituloLabel.grid(row=0, column=0, columnspan=2, sticky='WE')
    # tipoFormasPagoLabel.grid(row=1, column=0, sticky='WE')
    # valorFormasPagoLabel.grid(row=1, column=1, sticky='WE')
    # efectivoLabel.grid(row=1, column=2, sticky='WE')
    # efectivoValor.grid(row=2, column=3, sticky='WE')
    # tipoFormasPagoCombo.grid(row=2, column=0, sticky='WE')
    # valorFormasPagoEntry.grid(row=2, column=1, sticky='WE')
# 
    # formasPagoTree.grid(row=3, column=0, columnspan=3, sticky='nswe', pady=10)