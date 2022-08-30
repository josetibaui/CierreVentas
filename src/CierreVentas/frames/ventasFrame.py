# from curses.ascii import isdigit
from decimal import Decimal
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import *
from  modelo.locCortesias import Cortesias  as Cortesias
from decimal import *





class VentasFrame(ttk.Frame):

    def __init__(self, dataFrame):
        super().__init__(dataFrame)

        self.df = dataFrame
        self.grid(row=0, column=0, sticky='nsew')

        dataFrame.gridConfigure(self)
        self.crearWidgets()
        self.ventasEntry.focus()


#------------------- Ventas -------------------------------------------
    def validateVentas(self, entrada):
        getcontext().prec =  2
        if entrada == None or entrada == '':
            entrada = 0.00
        try:
            valor = Decimal(entrada)
            self.ventasEntryValue.set(valor)
            return True
        except InvalidOperation:
            self.ventasEntryValue.set('')
            return False
            
    def inValidateVentas(self):
        showerror(title='Error', message='Se debe ingresar un valor')
        self.ventasEntryValue.set('')
        self.ventasEntry.focus()

    def ventasEntryReturn(self, event):
        self.anulacionesEntry.focus()

# --------------------------Anulaciones----------------------------------------------------
    def validateAnulaciones(self, entrada):
        getcontext().prec =  2
        if entrada == None or entrada == '':
            entrada = 0.00
        try:
            valor = Decimal(entrada)
            self.anulacionesEntryValue.set(valor)
            return True
        except InvalidOperation:
            self.anulacionesEntryValue.set('')
            return False

    def inValidateAnulaciones(self):
        showerror(title='Error', message='Se debe ingresar un valor')
        self.anulacionesEntryValue.set('')
        self.anulacionesEntry.focus()

    def anulacionesEntryReturn(self, event):
        self.devolucionesEntry.focus()


#-----------------------------------Devoluciones -------------------------------------------------
    def validateDevoluciones(self, entrada):
        getcontext().prec =  2
        if entrada == None or entrada == '':
            entrada = 0.00
        try:
            valor = Decimal(entrada)
            self.devolucionesEntryValue.set(valor)
            return True
        except InvalidOperation:
            self.devolucionesEntryValue.set('')
            return False

    def inValidateDevoluciones(self):
        showerror(title='Error', message='Se debe ingresar un valor')
        self.devolucionesEntryValue.set('')
        self.devolucionesEntry.focus()

    def devolucionesEntryReturn(self, event):
        self.cortesiaTipoCombo.focus()

#--------------------------- Tipo de cortesia ----------------------------------------------
    def cortesiaTipoComboReturn(self, event):
        self.cortesiaValorEntry.focus()

#------------------------------Valor de la cortesia -------------------------------------------
    def cortesiaValorEntryReturn(self, event):
        self.cortesiaObservacionEntry.focus()

# --------------------------- Observaciones -------------------------------------------------
    def cortesiaObservacionEntryReturn(self, event):
        self.ventasEntry.focus()


# -----------------------------------------------------------------------------------------------
    def crearWidgets(self):

        estilo = ttk.Style(self)
        estilo.configure('TLabel', background=self.df.defaultColor)
        estilo.configure('TEntry', width=10, borderwidth=1, relief='solid', background=self.df.defaultColor)
        labelsOptions = {'sticky': 'we', 'padx': 20, 'pady': 2}
        labelColumnsOptions = {'sticky': 'N', 'padx': 5, 'pady': 10}

        tituloLabel = ttk.Label(self, text='Detalle de Ventas, anulaciones y Cortesías del Día', font=('Helvetica bold', 16))
        tituloLabel.grid(row=0, column=0, columnspan=4, pady=20, sticky='n')

        
#----------------------  Ventas Widgets ----------------------------------------------------
        self.ventasLabel = ttk.Label(self, text='Venta Total del día')
        self.ventasLabel.grid(row=1, column=0, **labelsOptions)
        # 
        self.ventasEntryValue = tk.StringVar()
        ventasEntryValid = (self.register(self.validateVentas), '%P')
        ventasEntryInvalid = (self.register(self.inValidateVentas), )
        self.ventasEntry = ttk.Entry(self, textvariable=self.ventasEntryValue, justify=tk.RIGHT)
        self.ventasEntry.grid(row=1, column=1)
        self.ventasEntry.config(validate='focusout', validatecommand=ventasEntryValid, invalidcommand=ventasEntryInvalid)
        self.ventasEntry.bind('<Return>', self.ventasEntryReturn)
        self.ventasEntry.bind('<KP_Enter>', self.ventasEntryReturn)


#----------------------------Anulaciones widgets--------------------------------------------------------
        self.anulacionesLabel = ttk.Label(self, text='Anulaciones del día')
        self.anulacionesLabel.grid(row=2, column=0, **labelsOptions)
        
        self.anulacionesEntryValue = tk.StringVar()
        anulacionesEntryValid = (self.register(self.validateAnulaciones), '%P')
        anulacionesEntryInvalid = (self.register(self.inValidateAnulaciones), )
        self.anulacionesEntry = ttk.Entry(self, textvariable=self.anulacionesEntryValue, justify=tk.RIGHT)
        self.anulacionesEntry.grid(row=2, column=1)
        self.anulacionesEntry.config(validate='focusout', validatecommand=anulacionesEntryValid, invalidcommand=anulacionesEntryInvalid)
        self.anulacionesEntry.bind('<Return>', self.anulacionesEntryReturn)
        self.anulacionesEntry.bind('<KP_Enter>', self.anulacionesEntryReturn)


#----------------------------------Devoluciones Widgets----------------------------------------------------
        self.devolucionesLabel = ttk.Label(self, text='Devoluciones del día')
        self.devolucionesLabel.grid(row=3, column=0, **labelsOptions)

        self.devolucionesEntryValue = tk.StringVar()
        devolucionesEntryValid = (self.register(self.validateDevoluciones), '%P')
        devolucionesEntryInvalid = (self.register(self.inValidateDevoluciones),)
        self.devolucionesEntry = ttk.Entry(self, textvariable=self.devolucionesEntryValue, justify=tk.RIGHT)
        self.devolucionesEntry.grid(row=3, column=1)
        self.devolucionesEntry.config(validate='focusout', validatecommand=devolucionesEntryValid, invalidcommand=devolucionesEntryInvalid)
        self.devolucionesEntry.bind('<Return>', self.devolucionesEntryReturn)
        self.devolucionesEntry.bind('<KP_Enter>', self.devolucionesEntryReturn)


        # Cortesías Widgets

        cortesiasLabel = ttk.Label(self, text='Cortesías de día')
        cortesiasLabel.grid(row=5, column=0, **labelsOptions)


        # Cortesias Tipo Widgets

        self.cortesiaTipoLabel = ttk.Label(self, text='Tipo de Cortesía')
        self.cortesiaTipoLabel.grid(row=4, column=1, **labelColumnsOptions)
        
        cortesias = Cortesias()
        listaCortesias = cortesias.queryAll()
        self.cortesiaTipoCombo = ttk.Combobox(self)
        self.cortesiaTipoCombo['values'] = [cortesia[1] for cortesia in listaCortesias]
        self.cortesiaTipoCombo['state'] = 'readonly'
        self.cortesiaTipoCombo.grid(row=5, column=1)
        self.cortesiaTipoCombo.bind('<Return>', self.cortesiaTipoComboReturn)
        self.cortesiaTipoCombo.bind('<KP_Enter>', self.cortesiaTipoComboReturn)
        

        # Cortesia Valor Widgets

        self.cortesiaValorLabel = ttk.Label(self, text='Valor de la Cortesía')
        self.cortesiaValorLabel.grid(row=4, column=2, **labelColumnsOptions)
        
        self.cortesiaValorEntry = ttk.Entry(self)
        self.cortesiaValorEntry.grid(row=5, column=2)
        self.cortesiaValorEntry.bind('<Return>', self.cortesiaValorEntryReturn)
        self.cortesiaValorEntry.bind('<KP_Enter>', self.cortesiaValorEntryReturn)


        # Cortesias ObservacionesWidgets

        self.cortesiaObservacionLabel = ttk.Label(self, text='Observaciones')
        self.cortesiaObservacionLabel.grid(row=4, column=3, **labelColumnsOptions)

        self.cortesiaObservacionEntry = ttk.Entry(self)
        self.cortesiaObservacionEntry.grid(row=5, column=3)
        self.cortesiaObservacionEntry.bind('<Return>', self.cortesiaObservacionEntryReturn)
        self.cortesiaObservacionEntry.bind('<KP_Enter>', self.cortesiaObservacionEntryReturn)


        # Tabla Cortesias

        columnasCortesias =('tipo', 'valor', 'observacion')
        cortesiasTree = ttk.Treeview(self, columns=columnasCortesias, show='headings')
        cortesiasTree.heading('tipo', text='Tipo de Cortesía')
        cortesiasTree.heading('valor', text='Valor de las Cortesías')
        cortesiasTree.heading('observacion', text='Observaciones')

        cortesiasTree.grid(row=7, column=1, columnspan=3, pady=10,sticky='nswe')


    # def nextField(self, actualField):
        # if actualField == 'ventasEntry':
            # self.anulacionesEntry.focus()