import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import *
from modelo.baBancos import Bancos
from decimal import Decimal, InvalidOperation

class DepositosFrame(ttk.Frame):
    def __init__(self, dataFrame):
        super().__init__(dataFrame)

        self.df = dataFrame
        self.grid(row=0, column=0, sticky='nsew')
        dataFrame.gridConfigure(self)
        self.crearWidgets()
        self.depositoBancosCombo.focus()

        self.bind('<Enter>', self.depositosFrameEnter)
        self.bind('<Leave>', self.depositosFrameExit)

#------------------------Entrada------------------------------
    def depositosFrameEnter(self, event):
        pass

#-------------------------Salida------------------------------
    def depositosFrameExit(self, event):
        pass

#-------------------------Lista de bancos-------------------------

#--------------------------- Valor del depósito---------------------------------
    def validateDepositoValor(self, entrada):
        if entrada == None or entrada == '':
            entrada = 0.00
        try:
            valor = Decimal(entrada)
            self.depositoValorValue.set(entrada)
            return True
        except InvalidOperation:
            self.depositoValorValue.set('')
            return False

    def invalidateDepositoValor(self):
        showerror(title='Error', message='Se debe ingresar un valor')
        self.depositoValorValue.set('')
        self.depositoValorEntry.focus()

    def depositoValorEntryReturn(self, event):
        self.depositoObservacionEntry.focus()

#----------------------------Observaciones ------------------------------
    def validateDepositoObservacion(self):
        depositoBanco = self.depositoBancoValue.get()
        depositoObservacion = self.depositoObservacionValue.get()
        try:
            depositoValor = Decimal(self.depositoValorValue.get())
        except InvalidOperation:
            depositoValor = 0

        if(depositoValor == None or depositoValor == '' or depositoValor  == 0):
            self.depositoBancoValue.set('')
            self.depositoValorValue.set('')
            self.depositoObservacionValue.set('')
            return True
        elif not(depositoBanco):
            return False
        else:
            self.depositosTree.insert('', tk.END, 
                            values=(depositoBanco,
                                    depositoValor,
                                    depositoObservacion))
            self.depositoBancoValue.set('')
            self.depositoValorValue.set('')
            self.depositoObservacionValue.set('')
        return True

    def invalidateDepositoObservacion(self):
        showwarning('Depósitos', message='Debe selecionar el banco en que se hace el depósito')
        self.depositoBancosCombo.focus()

    def depositosBancoEntryReturn(self, event):
        self.depositoBancosCombo.focus()

#-----------------------------Tree view--------------------------
    def depositosTreeItemSelected(self, event):
        for idItem in self.depositosTree.selection():
            item = self.depositosTree.item(idItem)
            self.depositoBancoValue.set(item['values'][0])
            self.depositoValorValue.set(item['values'][1])
            self.depositoObservacionValue.set(item['values'][2])
            self.depositosTree.delete(idItem)
            self.depositoBancosCombo.focus()
            break

# ========================================== Crear depositos Widgets ============================
    def crearWidgets(self):
        estilo = ttk.Style(self)
        estilo.configure('TLabel', background=self.df.defaultColor)
        # estilo.configure('TFrame', background=self.df.defaultColor)
        estilo.configure('Values.TLabel', relief='ridge')
        estilo.configure('TCombobox', background=self.df.defaultColor)
        estilo.configure('TEntry', width=10, borderwidth=1, background=self.df.defaultColor)
        labelsOptions = {'sticky': 'w', 'padx': 20, 'pady': 5}
        valuesOptions = {'sticky': 'e', 'padx': 20, 'pady': 5}
        labelsColumnsOptions = {'sticky': 'n', 'padx': 10, 'pady': 5}
        
        labelsEntryOptions = {'sticky': 'we', 'padx': 20, 'pady': 15}
        entryOptions = {'sticky': 'we', 'padx': 20, 'pady': 5}

        tituloLabel = ttk.Label(self, text='Detalle de Valores a Depositar', font=('Helvetica bold', 16))
        tituloLabel.grid(row=0, column=0, columnspan=4, pady=5, sticky='n')

#---------------------------------Banco---------------------------------------
        depositosBancoLabel = ttk.Label(self, text='Banco')
        depositosBancoLabel.grid(row=1, column=0, **labelsColumnsOptions)

        bancos = Bancos()
        listaBancos = bancos.queryAll()
        self.depositoBancoValue = tk.StringVar()
        self.depositoBancosCombo = ttk.Combobox(self, textvariable=self.depositoBancoValue, justify='left')
        self.depositoBancosCombo['values'] = [banco[1] for banco in listaBancos]
        self.depositoBancosCombo['state'] = 'readonly' 
        self.depositoBancosCombo.grid(row=2, column=0)

#---------------------------------Depósito Valor-----------------------------
        depositoValorLabel =ttk.Label(self, text='Valor del depósito')
        depositoValorLabel.grid(row=1, column=1, **labelsColumnsOptions)

        depositoValorEntryValid = (self.register(self.validateDepositoValor), '%P')
        depositoValorEntryInvalid = (self.register(self.invalidateDepositoValor),)
        self.depositoValorValue = tk.StringVar()
        self.depositoValorEntry = ttk.Entry(self, textvariable=self.depositoValorValue,justify='left')
        self.depositoValorEntry.grid(row=2, column=1, **valuesOptions)
        self.depositoValorEntry.config(validate='focusout',
                                        validatecommand=depositoValorEntryValid,
                                        invalidcommand=depositoValorEntryInvalid)
        self.depositoValorEntry.bind('<Return>', self.depositoValorEntryReturn)
        self.depositoValorEntry.bind('<KP_Enter>', self.depositoValorEntryReturn)

#-------------------------------Depósito Observacion-----------------------
        depositoObservacionLabel = ttk.Label(self, text='Observaciones')
        depositoObservacionLabel.grid(row=1, column=2, **labelsColumnsOptions)

        depositoObservacionValid = (self.register(self.validateDepositoObservacion),)
        depositoObservacionInvalid = (self.register(self.invalidateDepositoObservacion),)
        self.depositoObservacionValue = tk.StringVar()
        self.depositoObservacionEntry = ttk.Entry(self, textvariable=self.depositoObservacionValue,justify='left')
        self.depositoObservacionEntry.grid(row=2, column=2, **valuesOptions)
        self.depositoObservacionEntry.config(validate='focusout',
                                            validatecommand=depositoObservacionValid,
                                            invalidcommand=depositoObservacionInvalid)
        self.depositoObservacionEntry.bind('<Return>', self.depositosBancoEntryReturn)
        self.depositoObservacionEntry.bind('<KP_Enter>', self.depositosBancoEntryReturn)

# --------------------------------Depósitos Tree View-----------------------------
        columnasDepositos = ('banco', 'valor', 'observacion')
        self.depositosTree = ttk.Treeview(self, columns=columnasDepositos, show='headings')
        self.depositosTree.heading('banco', text='Banco')
        self.depositosTree.heading('valor', text='Valores')
        self.depositosTree.heading('observacion', text='Observaciones')
        self.depositosTree.grid(row=3, column=0, columnspan=3, sticky='nswe', pady=10)
        self.depositosTree.bind('<<TreeviewSelect>>', self.depositosTreeItemSelected)

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