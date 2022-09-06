import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import *
from modelo.locFormasPagos import FormasPagos as FormasPagos
from decimal import Decimal, InvalidOperation

class FormasPagosFrame(ttk.Frame):
    def __init__(self, dataFrame):
        super().__init__(dataFrame)

        self.df = dataFrame
        self.grid(row=0, column=0, sticky='nsew')

        dataFrame.gridConfigure(self)
        self.crearWidgets()
        self.formaPagoTipoCombo.focus()

        self.bind('<Enter>', self.formasPagosFrameEnter)
        self.bind('<Leave>', self.formasPagosFrameExit)

#-------------------Entrada-------------------------------------------
    def formasPagosFrameEnter(self,event):
        pass
     # showinfo('Salir', message=f'Entrando al frame {event.widget}')

#-------------------Salida-------------------------------------------
    def formasPagosFrameExit(self,event):
        pass
     # showinfo('Salir', message=f'Saliendo del frame {event.widget}')

#-------------------Efectivo------------------------------

#-------------------Tipo de forma de pago -----------------------
    # def formaPagoTipoCheck(self, event):
    #     valor = self.formaPagoTipoValue.get()
    #     if valor == None or valor == '':
    #         showwarning('Tipo de forma de pago', message='Debe selecionar el tipo de forma de pago')
    #         self.formaPagoTipoCombo.focus()
    #         return False
    #     else:
    #         return True

    # def formaPagoTipoReturn(self, event):
    #     self.formaPagoValorEntry.focus()

#----------------------------Forma Pagos valor ------------------
    def validateFormaPagoValor(self, entrada):
        if entrada == None or entrada == '':
            entrada = 0.00
        try:
            valor = Decimal(entrada)
            self.formaPagoValorValue.set(entrada)
            return True
        except InvalidOperation:
            self.formaPagoValorValue.set('')
            return False

    def inValidateFormaPagoValor(self):
        showerror(title='Error', message='Se debe ingresar un valor')
        self.formaPagoValorValue.set('')
        self.formaPagoValorEntry.focus()

    def formaPagoValorEntryReturn(self, event):
        self.formaPagoDescripcionEntry.focus()

# -------------------------- Forma pago descripción -------------
    def validateFormaPagoDescripcion(self):
        formaPagoTipo = self.formaPagoTipoValue.get()
        formaPagoDescripcion = self.formaPagoDescripcionValue.get()
        try:
            formaPagoValor = Decimal(self.formaPagoValorValue.get())
        except InvalidOperation:
            formaPagoValor = 0

        if(formaPagoValor == None or formaPagoValor == '' or formaPagoValor  == 0):
            self.formaPagoTipoValue.set('')
            self.formaPagoValorValue.set('')
            self.formaPagoDescripcionValue.set('')
            return True
        elif not(formaPagoTipo):
            return False
        else:
            self.formasPagosTree.insert('', tk.END, 
                            values=(formaPagoTipo,
                                    formaPagoValor,
                                    formaPagoDescripcion))
            self.formaPagoTipoValue.set('')
            self.formaPagoValorValue.set('')
            self.formaPagoDescripcionValue.set('')
        return True

    def invalidateFormaPagoDescripcion(self):
        showwarning('Forma de Pago', message='Debe selecionar el tipo de forma de pago.')
        self.formaPagoTipoCombo.focus()

    def formaPagoDescripcionEntryReturn(self, event):
        self.formaPagoTipoCombo.focus()

#------------------------------Tree view ------------------
    def formasPagosTreeItemSelected(self, event):
        for idItem in self.formasPagosTree.selection():
            item = self.formasPagosTree.item(idItem)
            self.formaPagoTipoValue.set(item['values'][0])
            self.formaPagoValorValue.set(item['values'][1])
            self.formaPagoDescripcionValue.set(item['values'][2])
            self.formasPagosTree.delete(idItem)
            self.formaPagoTipoCombo.focus()
            break;
#====================== Crear Widgets ============================
    def crearWidgets(self):

        estilo = ttk.Style(self)
        estilo.configure('TLabel', background=self.df.defaultColor)
        estilo.configure('Values.TLabel', relief='ridge')
        estilo.configure('TCombobox', background=self.df.defaultColor)
        estilo.configure('TEntry', width=10, borderwidth=1, background=self.df.defaultColor)
        labelsOptions = {'sticky': 'w', 'padx': 20, 'pady': 5}
        valuesOptions = {'sticky': 'e', 'padx': 20, 'pady': 5}
        labelsColumnsOptions = {'sticky': 'n', 'padx': 5, 'pady': 5}
        
        labelsEntryOptions = {'sticky': 'we', 'padx': 20, 'pady': 15}
        entryOptions = {'sticky': 'we', 'padx': 20, 'pady': 5}

        tituloLabel = ttk.Label(self, text='Detalle de Formas de Pago de Clientes', font=('Helvetica bold', 16))
        tituloLabel.grid(row=0, column=0, columnspan=4, pady=6, sticky='n')

# -----------------Efectivo---------------------------------------
        efectivoLabel = ttk.Label(self, text='Efectivo')
        efectivoLabel.grid(row=1,column=0, **labelsEntryOptions)

        self.efectivoEntry = ttk.Entry(self)
        self.efectivoEntry['takefocus'] = 0
        self.efectivoEntry['state'] = 'readonly'
        self.efectivoEntry.grid(row=1,column=1, **entryOptions)

# ====================== Formas de Pago Widgets =============================
        formasPagosLabel = ttk.Label(self, text='Pagos')
        formasPagosLabel.grid(row=3, column=0, **labelsOptions)

# ------------------------- Tipo de forma de pago Widget ---------------------
        formaPagoTipoLabel = ttk.Label(self, text='Forma de Pago')
        formaPagoTipoLabel.grid(row=2, column=1, **labelsColumnsOptions)

        formasPagos = FormasPagos()
        listaFormasPagos = formasPagos.queryAll()
        self.formaPagoTipoValue = tk.StringVar()
        self.formaPagoTipoCombo = ttk.Combobox(self, textvariable=self.formaPagoTipoValue, justify='left')
        self.formaPagoTipoCombo['values'] = [formaPago[1] for formaPago in listaFormasPagos]
        self.formaPagoTipoCombo['state'] = 'readonly'
        self.formaPagoTipoCombo.grid(row=3, column=1)

# ------------------------- Valor de la forma de pago widget-----------------
        formaPagoValorLabel = ttk.Label(self, text='Valor')
        formaPagoValorLabel.grid(row=2,column=2, **labelsColumnsOptions)

        formaPagoValorEntryValid = (self.register(self.validateFormaPagoValor), '%P')
        formaPagoValorEntryInvalid = (self.register(self.inValidateFormaPagoValor))
        self.formaPagoValorValue = tk.StringVar()
        self.formaPagoValorEntry = ttk.Entry(self,
                                        textvariable=self.formaPagoValorValue,
                                        justify=tk.RIGHT)               
        self.formaPagoValorEntry.grid(row=3, column=2, **valuesOptions)
        self.formaPagoValorEntry.config(validate='focusout',
                                        validatecommand=formaPagoValorEntryValid,
                                        invalidcommand=formaPagoValorEntryInvalid)
        self.formaPagoValorEntry.bind('<Return>', self.formaPagoValorEntryReturn)
        self.formaPagoValorEntry.bind('<KP_Enter>', self.formaPagoValorEntryReturn)


# -------------------------- Descripción de la froma de pago widget-------------------- 
        formaPagoDescripcionLabel = ttk.Label(self, text='Obervaciones')
        formaPagoDescripcionLabel.grid(row=2, column=3, **labelsColumnsOptions)

        formaPagoDescripcionValid = (self.register(self.validateFormaPagoDescripcion),)
        formaPagoDescripcionInvalid = (self.register(self.invalidateFormaPagoDescripcion),)
        self.formaPagoDescripcionValue = tk.StringVar()
        self.formaPagoDescripcionEntry = ttk.Entry(self, textvariable=self.formaPagoDescripcionValue, justify=tk.LEFT)
        self.formaPagoDescripcionEntry.grid(row=3, column=3, **valuesOptions)
        self.formaPagoDescripcionEntry.config(validate='focusout', validatecommand=formaPagoDescripcionValid, invalidcommand=formaPagoDescripcionInvalid)
        self.formaPagoDescripcionEntry.bind('<Return>', self.formaPagoDescripcionEntryReturn)
        self.formaPagoDescripcionEntry.bind('<KP_Enter>', self.formaPagoDescripcionEntryReturn)

# --------------------------- Formas de pago tree widget
        columnasFormasPago = ('tipoFormasPago', 'valor', 'observacion')
        self.formasPagosTree = ttk.Treeview(self, columns=columnasFormasPago, show='headings', selectmode='browse')
        self.formasPagosTree.heading('tipoFormasPago', text='Formas de Pago')
        self.formasPagosTree.heading('valor', text='Valores')
        self.formasPagosTree.heading('observacion', text='Observaciones')
        self.formasPagosTree.grid(row=4, column=1, columnspan=3, sticky='nswe', pady=10)
        self.formasPagosTree.bind('<<TreeviewSelect>>', self.formasPagosTreeItemSelected)

        # tipoFormasPagoLabel = ttk.Label(self, text='Forma de Pago')
        # valorFormasPagoLabel =ttk.Label(self, text='Valor')
        # efectivoLabel = ttk.Label(self, text='Valor Recibido en Efectivo')
        # efectivoValor = ttk.Label(self, text='0.00')

        # self.tipoFormasPagoCombo = ttk.Combobox(self)
        # self.tipoFormasPagoCombo['values'] = ['Medianet', 'DataFast', 'Cheque', 'Transferencia', 'Retención IR']
        # self.tipoFormasPagoCombo['state'] = 'readonly' 
        # valorFormasPagoEntry = tk.Entry(self)

        # columnasFormasPago = ('tipoFormasPago', 'valor')
        # formasPagoTree = ttk.Treeview(self, columns=columnasFormasPago, show='headings')
        # formasPagoTree.heading('tipoFormasPago', text='Formas de Pago')
        # formasPagoTree.heading('valor', text='Valores')

        # tituloLabel.grid(row=0, column=0, columnspan=2, sticky='WE')
        # tipoFormasPagoLabel.grid(row=1, column=0, sticky='WE')
        # valorFormasPagoLabel.grid(row=1, column=1, sticky='WE')
        # efectivoLabel.grid(row=1, column=2, sticky='WE')
        # efectivoValor.grid(row=2, column=3, sticky='WE')
        # self.tipoFormasPagoCombo.grid(row=2, column=0, sticky='WE')
        # valorFormasPagoEntry.grid(row=2, column=1, sticky='WE')

    # def initFocus(self):
    #     self.tipoFormasPagoCombo.focus()


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