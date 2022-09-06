# from curses.ascii import isdigit
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import *
from modelo.locCortesias import Cortesias  as Cortesias
from decimal import Decimal
from decimal import *





class VentasFrame(ttk.Frame):

    def __init__(self, dataFrame):
        super().__init__(dataFrame)

        self.df = dataFrame
        self.grid(row=0, column=0, sticky='nsew')

        dataFrame.gridConfigure(self)
        self.crearWidgets()
        self.ventasEntry.focus()

        self.bind('<Enter>', self.ventasFrameEnter)
        self.bind('<Leave>', self.ventasFrameExit)

#------------------------Entrada-------------------------
    def ventasFrameEnter(self, event):
        pass
        # showinfo('Salir', message=f'Entrando al frame {event.widget}')

#------------------------Salida-------------------------
    def ventasFrameExit(self, event):
        pass
        # showinfo('Salir', message=f'Saliendo del frame {event.widget}')

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
            self.ventasEntry.focus()
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
    # def cortesiaTipoCheck(self, event):
    #     valor = self.cortesiaTipoValue.get()
    #     if valor == None or valor == '':
    #         showwarning('Tipo de cortesía', message=f'Debe selecionar el tipo de cortesía.')
    #         self.cortesiaTipoCombo.focus()
    #         return False
    #     else:
    #         return True
   

    # def cortesiaTipoComboReturn(self, event):
    #     self.cortesiaValorEntry.focus()

#------------------------------Valor de la cortesia -------------------------------------------
    def validateCortesiaValor(self, entrada):
        getcontext().prec =  2
        if entrada == None or entrada == '':
            entrada = 0.00
        try:
            valor = Decimal(entrada)
            self.cortesiaValorEntryValue.set(entrada)
            return True
        except InvalidOperation:
            self.cortesiaValorEntryValue.set('')
            return False

    def inValidateCortesiaValor(self):
        showerror(title='Error', message='Se debe ingresar un valor')
        self.cortesiaValorEntryValue.set('')
        self.cortesiaValorEntry.focus()

    def cortesiaValorEntryReturn(self, event):
        self.cortesiaObservacionEntry.focus()

# --------------------------- Observaciones -------------------------------------------------
    def validateCortesiaObservacion(self):
        cortesiaTipo = self.cortesiaTipoValue.get()
        cortesiaObservacion = self.cortesiaObservacionValue.get()
        try:
            cortesiaValor = Decimal(self.cortesiaValorEntryValue.get())
        except InvalidOperation:
            cortesiaValor = 0

        if (cortesiaValor == None or cortesiaValor == '' or cortesiaValor == 0):
            self.cortesiaTipoValue.set('')
            self.cortesiaValorEntryValue.set('')
            self.cortesiaObservacionValue.set('')
            return Trgit branchue
        elif not(cortesiaTipo):
            return False
        else:
            self.cortesiasTree.insert('', tk.END,
                                values=(cortesiaTipo,
                                        cortesiaValor,
                                        cortesiaObservacion))
            self.cortesiaTipoValue.set('')
            self.cortesiaValorEntryValue.set('')
            self.cortesiaObservacionValue.set('')
        return True
    
    def invalidateCortesiaObservacion(self):
        showwarning('Tipo de cortesía', message=f'Debe selecionar el tipo de cortesía.')
        self.cortesiaTipoCombo.focus()
    
    def cortesiaObservacionEntryReturn(self, event):
        self.cortesiaTipoCombo.focus()

#-----------------------------TreeView--------------------------------------
    def cortesiasTreeItemSelected(self, event):
        for idItem in  self.cortesiasTree.selection():
            item = self.cortesiasTree.item(idItem)
            self.cortesiaTipoValue.set(item['values'][0])
            self.cortesiaValorEntryValue.set(item['values'][1])
            self.cortesiaObservacionValue.set(item['values'][2])
            self.cortesiasTree.delete(idItem)
            self.cortesiaTipoCombo.focus()
            break;


# ============================== Crear Widgets=============================================
    def crearWidgets(self):

        estilo = ttk.Style(self)
        estilo.configure('TLabel', background=self.df.defaultColor)
        estilo.configure('TEntry', width=10, borderwidth=1, relief='solid', background=self.df.defaultColor)
        labelsOptions = {'sticky': 'we', 'padx': 20, 'pady': 2}
        valuesOptions = {'sticky': 'e', 'padx': 20, 'pady': 2}
        labelColumnsOptions = {'sticky': 'N', 'padx': 5, 'pady': 10}

        labelsEntryOptions = {'sticky': 'we', 'padx': 20, 'pady': 15}
        entryOptions = {'sticky': 'we', 'padx': 20, 'pady': 5}

        tituloLabel = ttk.Label(self, text='Detalle de Ventas, anulaciones y Cortesías del Día', font=('Helvetica bold', 16))
        tituloLabel.grid(row=0, column=0, columnspan=4, pady=20, sticky='n')

#----------------------  Ventas Widgets ----------------------------------------------------
        ventasLabel = ttk.Label(self, text='Venta Total del día')
        ventasLabel.grid(row=1, column=0, **labelsOptions)
         
        ventasEntryValid = (self.register(self.validateVentas), '%P')
        ventasEntryInvalid = (self.register(self.inValidateVentas), )
        self.ventasEntryValue = tk.StringVar()
        self.ventasEntry = ttk.Entry(self, textvariable=self.ventasEntryValue, justify=tk.RIGHT)
        self.ventasEntry.grid(row=1, column=1)
        self.ventasEntry.config(validate='focusout', validatecommand=ventasEntryValid, invalidcommand=ventasEntryInvalid)
        self.ventasEntry.bind('<Return>', self.ventasEntryReturn)
        self.ventasEntry.bind('<KP_Enter>', self.ventasEntryReturn)

#----------------------------Anulaciones widgets--------------------------------------------------------
        anulacionesLabel = ttk.Label(self, text='Anulaciones del día')
        anulacionesLabel.grid(row=2, column=0, **labelsOptions)
        
        anulacionesEntryValid = (self.register(self.validateAnulaciones), '%P')
        anulacionesEntryInvalid = (self.register(self.inValidateAnulaciones), )
        self.anulacionesEntryValue = tk.StringVar()
        self.anulacionesEntry = ttk.Entry(self, textvariable=self.anulacionesEntryValue, justify=tk.RIGHT)
        self.anulacionesEntry.grid(row=2, column=1)
        self.anulacionesEntry.config(validate='focusout', validatecommand=anulacionesEntryValid, invalidcommand=anulacionesEntryInvalid)
        self.anulacionesEntry.bind('<Return>', self.anulacionesEntryReturn)
        self.anulacionesEntry.bind('<KP_Enter>', self.anulacionesEntryReturn)

#----------------------------------Devoluciones Widgets----------------------------------------------------
        devolucionesLabel = ttk.Label(self, text='Devoluciones del día')
        devolucionesLabel.grid(row=3, column=0, **labelsOptions)

        devolucionesEntryValid = (self.register(self.validateDevoluciones), '%P')
        devolucionesEntryInvalid = (self.register(self.inValidateDevoluciones),)
        self.devolucionesEntryValue = tk.StringVar()
        self.devolucionesEntry = ttk.Entry(self,
                                            textvariable=self.devolucionesEntryValue,
                                            justify=tk.RIGHT)
        self.devolucionesEntry.grid(row=3, column=1)
        self.devolucionesEntry.config(validate='focusout',
                                    validatecommand=devolucionesEntryValid,
                                    invalidcommand=devolucionesEntryInvalid)
        self.devolucionesEntry.bind('<Return>', self.devolucionesEntryReturn)
        self.devolucionesEntry.bind('<KP_Enter>', self.devolucionesEntryReturn)

# ========================   Cortesías Widgets ======================================
        cortesiasLabel = ttk.Label(self, text='Cortesías de día')
        cortesiasLabel.grid(row=5, column=0, **labelsOptions)

#-------------------- Cortesias Tipo Widgets ------------------------------------------
        self.cortesiaTipoLabel = ttk.Label(self, text='Tipo de Cortesía')
        self.cortesiaTipoLabel.grid(row=4, column=1, **labelColumnsOptions)
        
        cortesias = Cortesias()
        listaCortesias = cortesias.queryAll()
        self.cortesiaTipoValue = tk.StringVar()
        self.cortesiaTipoCombo = ttk.Combobox(self, textvariable=self.cortesiaTipoValue, justify='left')
        self.cortesiaTipoCombo['values'] = [cortesia[1] for cortesia in listaCortesias]
        self.cortesiaTipoCombo['state'] = 'readonly'
        self.cortesiaTipoCombo.grid(row=5, column=1)

#------------------------------------------Cortesia Valor Widgets --------------------------------
        cortesiaValorLabel = ttk.Label(self, text='Valor de la Cortesía')
        cortesiaValorLabel.grid(row=4, column=2, **labelColumnsOptions)
        
        cortesiaValorEntryValid = (self.register(self.validateCortesiaValor), '%P')
        cortesiaValorEntryInvalid = (self.register(self.inValidateCortesiaValor),)
        self.cortesiaValorEntryValue = tk.StringVar()
        self.cortesiaValorEntry = ttk.Entry(self,
                                            textvariable=self.cortesiaValorEntryValue,
                                            justify=tk.RIGHT)
        self.cortesiaValorEntry.grid(row=5, column=2)
        self.cortesiaValorEntry.config(validate='focusout',
                                        validatecommand=cortesiaValorEntryValid,
                                        invalidcommand=cortesiaValorEntryInvalid)
        self.cortesiaValorEntry.bind('<Return>', self.cortesiaValorEntryReturn)
        self.cortesiaValorEntry.bind('<KP_Enter>', self.cortesiaValorEntryReturn)


        # Cortesias ObservacionesWidgets

        cortesiaObservacionLabel = ttk.Label(self, text='Observaciones')
        cortesiaObservacionLabel.grid(row=4, column=3, **labelColumnsOptions)
        
        cortesiaObservacionValid = (self.register(self.validateCortesiaObservacion),)
        cortesiaObservacionInvalid = (self.register(self.invalidateCortesiaObservacion),)
        self.cortesiaObservacionValue = tk.StringVar()
        self.cortesiaObservacionEntry = ttk.Entry(self, textvariable=self.cortesiaObservacionValue, justify=tk.LEFT)
        self.cortesiaObservacionEntry.grid(row=5, column=3, **valuesOptions)
        self.cortesiaObservacionEntry.config(validate='focusout', validatecommand=cortesiaObservacionValid, invalidcommand=cortesiaObservacionInvalid)
        self.cortesiaObservacionEntry.bind('<Return>', self.cortesiaObservacionEntryReturn)
        self.cortesiaObservacionEntry.bind('<KP_Enter>', self.cortesiaObservacionEntryReturn)


        # Tabla Cortesias

        columnasCortesias =('tipo', 'valor', 'observacion')
        self.cortesiasTree = ttk.Treeview(self, columns=columnasCortesias, show='headings', selectmode='browse')
        self.cortesiasTree.heading('tipo', text='Tipo de Cortesía')
        self.cortesiasTree.heading('valor', text='Valor de las Cortesías')
        self.cortesiasTree.heading('observacion', text='Observaciones')
        self.cortesiasTree.grid(row=7, column=1, columnspan=3, pady=10,sticky='nswe')
        self.cortesiasTree.bind('<<TreeviewSelect>>', self.cortesiasTreeItemSelected)
