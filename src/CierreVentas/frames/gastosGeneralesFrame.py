import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import *
from modelo.locGastosGenerales import GastosGenerales
from modelo.igLocales import Locales
from decimal import Decimal, InvalidOperation

class GastosGeneralesFrame(ttk.Frame):
    def __init__(self, dataFrame):
        super().__init__(dataFrame)

        self.df = dataFrame
        self.grid(row=0, column=0, sticky='nsew')

        dataFrame.gridConfigure(self)
        self.crearWidgets()
        self.gastoGeneralTipoCombo.focus()

        self.bind('<Enter>', self.gastosGeneralesFrameEnter)
        self.bind('<Leave>', self.gastosGeneralesFrameExit)

#-----------------------------Entrada-----------------------------------
    def gastosGeneralesFrameEnter(self, event):
        pass
#-----------------------------Salida------------------------------------
    def gastosGeneralesFrameExit(self, event):
        pass

#------------------------- Tipo de gasto ----------------------------

#--------------------------Valor del gastos --------------
    def validateGastoGeneralValor(self, entrada):
        if entrada == None or entrada == '':
            entrada = 0.00
        try:
            valor = Decimal(entrada)
            self.gastoGeneralValorValue.set(entrada)
            return True
        except InvalidOperation:
            self.gastoGeneralValorValue.set('')
            return False

    def inValidateGastoGeneralValor(self):
        showerror(title='Error', message='Se debe ingresar un valor')
        self.gastoGeneralValorValue.set('')
        self.gastoGeneralValorEntry.focus()

    def gastoGeneralValorEntryReturn(self, event):
        self.gastoGeneralObservacionEntry.focus()

#---------------------------Local de origen del gasto ------------------

#--------------------------Observaciones ------------------------
    def validateGastoGeneralObservacion(self):
        gastoGeneralTipo = self.gastoGeneralTipoValue.get()
        gastoGeneralLocalOrigen = self.gastoGeneralLocalOrigenValue.get()
        gastoGeneralObservacion = self.gastoGeneralObservacionValue.get()
        try:
            gastoGeneralValor = Decimal(self.gastoGeneralValorValue.get())
        except InvalidOperation:
            gastoGeneralValor = 0

        if(gastoGeneralValor == None or gastoGeneralValor == '' or gastoGeneralValor  == 0):
            self.gastoGeneralTipoValue.set('')
            self.gastoGeneralValorValue.set('')
            self.gastoGeneralLocalOrigenValue.set('')
            self.gastoGeneralObservacionValue.set('')
            return True
        elif not(gastoGeneralTipo):
            return False
        else:
            self.gastosGeneralesTree.insert('', tk.END, 
                            values=(gastoGeneralTipo,
                                    gastoGeneralValor,
                                    gastoGeneralLocalOrigen,
                                    gastoGeneralObservacion))
            self.gastoGeneralTipoValue.set('')
            self.gastoGeneralValorValue.set('')
            self.gastoGeneralLocalOrigenValue.set('')
            self.gastoGeneralObservacionValue.set('')
        return True

    def invalidateGastoGeneralObservacion(self):
        showwarning('Forma de Pago', message='Debe selecionar tipo de gasto.')
        self.gastoGeneralTipoCombo.focus()

    def gastoGeneralObservacionEntryReturn(self, event):
        self.gastoGeneralTipoCombo.focus()

#----------------------------  Tree View  ---------------------------------
    def gastosGeneralesTreeItemSelected(self, event):
        for idItem in self.gastosGeneralesTree.selection():
            item = self.gastosGeneralesTree.item(idItem)
            self.gastoGeneralTipoValue.set(item['values'][0])
            self.gastoGeneralValorValue.set(item['values'][1])
            self.gastoGeneralLocalOrigenValue.set(item['values'][2])
            self.gastoGeneralObservacionValue.set(item['values'][3])
            self.gastosGeneralesTree.delete(idItem)
            self.gastoGeneralTipoCombo.focus()
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

        tituloLabel = ttk.Label(self, text='Detalle de Gastos', font=('Helvetica bold', 16))
        tituloLabel.grid(row=0, column=0, columnspan=4, pady=6, sticky='n')


# =================================== Gastos Generales Widgets====================================

# --------------------------------------Tipo de gasto general widgets------------------------------------
        tipoGastoGeneralLabel = ttk.Label(self, text='Tipos de Gastos')
        tipoGastoGeneralLabel.grid(row=1,column=0, **labelsColumnsOptions)

        gastosGenerales = GastosGenerales()
        listaGastosGenerales = gastosGenerales.queryAll()
        self.gastoGeneralTipoValue = tk.StringVar()
        self.gastoGeneralTipoCombo = ttk.Combobox(self, textvariable=self.gastoGeneralTipoValue, justify='left')
        self.gastoGeneralTipoCombo['values'] = [gasto[1] for gasto in listaGastosGenerales]
        self.gastoGeneralTipoCombo['state'] = 'readonly'
        self.gastoGeneralTipoCombo.grid(row=2, column=0)

# -----------------------------------Valor del gastos generales widgets
        valorGastoGeneralLabel = ttk.Label(self, text='Valor del Gasto')
        valorGastoGeneralLabel.grid(row=1,column=1, **labelsColumnsOptions)

        gastoGeneralValorEntryValid = (self.register(self.validateGastoGeneralValor), '%P')
        gastoGeneralValorEntryInvalid = (self.register(self.inValidateGastoGeneralValor))
        self.gastoGeneralValorValue = tk.StringVar()
        self.gastoGeneralValorEntry = ttk.Entry(self,
                                        textvariable=self.gastoGeneralValorValue,
                                        justify=tk.RIGHT)
        self.gastoGeneralValorEntry.grid(row=2, column=1, **valuesOptions)
        self.gastoGeneralValorEntry.config(validate='focusout',
                                        validatecommand=gastoGeneralValorEntryValid,
                                        invalidcommand=gastoGeneralValorEntryInvalid)
        self.gastoGeneralValorEntry.bind('<Return>', self.gastoGeneralValorEntryReturn)
        self.gastoGeneralValorEntry.bind('<KP_Enter>', self.gastoGeneralValorEntryReturn)

        
# ---------------------------------Local de origen del gastos general -----------------------
        gastoGeneralLocalOrigenLabel = ttk.Label(self, text='Local de Origen del Gasto')
        gastoGeneralLocalOrigenLabel.grid(row=1,column=2, **labelsColumnsOptions)

        locales = Locales()
        listaLocales = locales.queryAll()
        listaLocalesDisplay = [f'{local[1]} - {local[2]}' for local in listaLocales if local[0] != self.df.rw.esteLocal[0]]
        listaLocalesDisplay.insert(0,'')
        self.gastoGeneralLocalOrigenValue = tk.StringVar()
        self.gastoGeneralLocalOrigenCombo = ttk.Combobox(self, textvariable=self.gastoGeneralLocalOrigenValue, justify='left')
        self.gastoGeneralLocalOrigenCombo['values'] = listaLocalesDisplay
        self.gastoGeneralLocalOrigenCombo['state'] = 'readonly'
        self.gastoGeneralLocalOrigenCombo.grid(row=2, column=2)

# ------------------------------------Observaciones del gastos genral ------------------------
        gastoGeneralObservacionLabel = ttk.Label(self, text='Observaciones')
        gastoGeneralObservacionLabel.grid(row=1,column=3, **labelsColumnsOptions)

        gastoGeneralObservacionValid = (self.register(self.validateGastoGeneralObservacion),)
        gastoGeneralObservacionInvalid = (self.register(self.invalidateGastoGeneralObservacion),)
        self.gastoGeneralObservacionValue = tk.StringVar()
        self.gastoGeneralObservacionEntry = ttk.Entry(self, textvariable = self.gastoGeneralObservacionValue, justify=tk.LEFT) 
        self.gastoGeneralObservacionEntry.grid(row=2, column=3, **valuesOptions)
        self.gastoGeneralObservacionEntry.config(validate='focusout', validatecommand=gastoGeneralObservacionValid, invalidcommand=gastoGeneralObservacionInvalid)
        self.gastoGeneralObservacionEntry.bind('<Return>', self.gastoGeneralObservacionEntryReturn)
        self.gastoGeneralObservacionEntry.bind('<KP_Enter>', self.gastoGeneralObservacionEntryReturn)


# ---------------------------------- Gastos Generales Tree view --------------
        columnasGastosGenerales = ('tipoGastoGeneral', 'valorGastoGeneral', 'gastoGeneralLocalOrigen', 'observaciones')
        self.gastosGeneralesTree = ttk.Treeview(self, columns=columnasGastosGenerales, show='headings', selectmode='browse')
        self.gastosGeneralesTree.heading('tipoGastoGeneral', text='Tipo de Gasto')
        self.gastosGeneralesTree.heading('valorGastoGeneral', text='Valor del Gasto')
        self.gastosGeneralesTree.heading('gastoGeneralLocalOrigen', text='Local de Origen')
        self.gastosGeneralesTree.heading('observaciones', text='Observaciones')
        self.gastosGeneralesTree.grid(row=3, column=0, columnspan=4, sticky='nswe', pady=10)
        self.gastosGeneralesTree.bind('<<TreeviewSelect>>', self.gastosGeneralesTreeItemSelected)