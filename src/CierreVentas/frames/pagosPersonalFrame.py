import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import *
from modelo.locPagosPersonal import PagosPersonal
from modelo.igPersonas import Personas
from decimal import Decimal, InvalidOperation


class PagosPersonalFrame(ttk.Frame):
    def __init__(self, dataFrame):
        super().__init__(dataFrame)

        self.df = dataFrame
        self.grid(row=0, column=0, sticky='nsew')

    
        self.datosHoy = dataFrame.datosHoy
        dataFrame.gridConfigure(self)
        self.crearWidgets()
        self.pagoPersonalEmpleadosCombo.focus()

        self.bind('<Enter>', self.pagosPersonalFrameEnter)
        self.bind('<Leave>', self.pagosPersonalFrameExit)

#-----------------------------Entrada-----------------------------------
    def pagosPersonalFrameEnter(self, event):
        self.pagosPersonalFrameSetValues()

    def pagosPersonalFrameSetValues(self):
        for idItem in self.pagosPersonalTree.get_children():
            self.pagosPersonalTree.delete(idItem)

        for pagoPersonal in self.df.datosHoy['PagosPersonal']:
            self.pagosPersonalTree.insert('', tk.END, 
                            values=(pagoPersonal[0],
                                    pagoPersonal[1],
                                    pagoPersonal[2],
                                    pagoPersonal[3]))
#-----------------------------Salida------------------------------------
    def pagosPersonalFrameExit(self, event):
       listaPagosPersonal = []
       for idItem in self.pagosPersonalTree.get_children():
            pagoPersonal = self.pagosPersonalTree.item(idItem)['values']
            if float(pagoPersonal[2]) != 0:
                listaPagosPersonal.append(pagoPersonal)

       self.datosHoy['PagosPersonal'] = listaPagosPersonal

# --------------------------------Lista de empleados -------------------------

# --------------------------- Tipo de Pago ----------------------------------------
    def validatePagoPersonalValor(self, entrada):
        if entrada == None or entrada == '':
            entrada = 0.00
        try:
            valor = float(entrada)
            self.pagoPersonalValorValue.set(entrada)
            return True
        except InvalidOperation:
            self.pagoPersonalValorValue.set('')
            return False

    def inValidatePagoPersonalValor(self):
        showerror(title='Error', message='Se debe ingresar un valor')
        self.pagoPersonalValorValue.set('')
        self.pagoPersonalValorEntry.focus()

    def pagoPersonalValorEntryReturn(self, event):
        self.pagoPersonalObservacionEntry.focus()
# ---------------------------------Valor del pago -------------------------------

# --------------------------------Observaciones-------------------------------
    def validatePagoPersonalObservacion(self):
        pagoPersonalEmpleado = self.pagoPersonalEmpleadoValue.get()
        pagoPersonalTipo = self.pagoPersonalTipoValue.get()
        pagoPersonalObservacion = self.pagoPersonalObservacionValue.get()
        try:
            pagoPersonalValor = float(self.pagoPersonalValorValue.get())
        except InvalidOperation:
            pagoPersonalValor = 0

        if(pagoPersonalValor == None or pagoPersonalValor == '' or pagoPersonalValor  == 0):
            self.pagoPersonalEmpleadoValue.set('')
            self.pagoPersonalTipoValue.set('')
            self.pagoPersonalValorValue.set('')
            self.pagoPersonalObservacionValue.set('')
            return True
        elif not(pagoPersonalTipo or pagoPersonalEmpleado):
            return False
        else:
            self.pagosPersonalTree.insert('', tk.END, 
                            values=(pagoPersonalEmpleado,
                                    pagoPersonalTipo,
                                    pagoPersonalValor,
                                    pagoPersonalObservacion))
            self.pagoPersonalEmpleadoValue.set('')
            self.pagoPersonalTipoValue.set('')
            self.pagoPersonalValorValue.set('')
            self.pagoPersonalObservacionValue.set('')
        return True

    def invalidatePagoPersonalObservacion(self):
        showwarning('Forma de Pago', message='Debe selecionar al empleado y el tipo de pago.')
        self.pagoPersonalEmpleadosCombo.focus()

    def pagoPersonalObservacionEntryReturn(self, event):
        self.pagoPersonalEmpleadosCombo.focus()

#--------------------------------Treee view --------------------------------------
    def pagosPersonalTreeItemSelected(self, event):
        for idItem in self.pagosPersonalTree.selection():
            item = self.pagosPersonalTree.item(idItem)
            self.pagoPersonalEmpleadoValue.set(item['values'][0])
            self.pagoPersonalTipoValue.set(item['values'][1])
            self.pagoPersonalValorValue.set(item['values'][2])
            self.pagoPersonalObservacionValue.set(item['values'][3])
            self.pagosPersonalTree.delete(idItem)
            self.pagoPersonalEmpleadosCombo.focus()
            break

#============================== Crear Widgets =====================================       

    def crearWidgets(self):
        estilo = ttk.Style(self)
        estilo.configure('TLabel', background=self.df.defaultColor)
        estilo.configure('TFrame', background=self.df.defaultColor)
        estilo.configure('TRadiobutton', background=self.df.defaultColor)
        estilo.configure('Values.TLabel', relief='ridge')
        estilo.configure('TCombobox', background=self.df.defaultColor)
        estilo.configure('TEntry', width=10, borderwidth=1, background=self.df.defaultColor)
        valuesOptions = {'sticky': 'e', 'padx': 20, 'pady': 5}
        labelsColumnsOptions = {'sticky': 'n', 'padx': 10, 'pady': 5}

        tituloLabel = ttk.Label(self, text='Detalle de Gastos de Personal', font=('Helvetica bold', 16))
        tituloLabel.grid(row=0, column=0, columnspan=4, pady=5, sticky='n')

# --------------------------  Selecciona el contenido de la lista de empleados
        selectListaPersonasFrame = ttk.Frame(self)
        selectListaPersonasFrame.grid(row=1, column=0, sticky='we')

# ------------------------------- Lista de empleados wodget -------------------
        pagoPersonalEmpleadoLabel = ttk.Label(self, text='Empleado')
        pagoPersonalEmpleadoLabel.grid(row=2,column=0, **labelsColumnsOptions)

        personas = Personas()
        listaPersonasLocal = personas.queryByIdLocal(self.df.rw.esteLocal[0])
        listaPersonasEmpresa = personas.queryAll()
        
        listaSeleccionada = tk.StringVar()
        self.pagoPersonalEmpleadoValue = tk.StringVar()
        self.pagoPersonalEmpleadosCombo = ttk.Combobox(self, textvariable=self.pagoPersonalEmpleadoValue, justify='left', state='readonly')
        listaSeleccionada.set('L')
        def setListaPersonas():
            if listaSeleccionada.get() == 'L':
                self.pagoPersonalEmpleadosCombo['values'] = [f'{empleado[2]} {empleado[1]}' for empleado in listaPersonasLocal]
            else:
                self.pagoPersonalEmpleadosCombo['values'] = [f'{empleado[2]} {empleado[1]}' for empleado in listaPersonasEmpresa]
        setListaPersonas()
        self.pagoPersonalEmpleadosCombo.grid(row=3, column=0)

        

        opcionesListas =  [('Este Local', 'L'), ('Todos los Locales', 'T')]
        for lista, valor in opcionesListas:
            ttk.Radiobutton(selectListaPersonasFrame, text=lista, variable=listaSeleccionada, command=setListaPersonas, value=valor).pack(side='left')

# ------------------------------------Tipo de pago widget-----------------------------
        pagoPersonalTipoLabel = ttk.Label(self, text='Tipo de Pago')
        pagoPersonalTipoLabel.grid(row=2,column=1, **labelsColumnsOptions)

        pagosPersonal = PagosPersonal()
        listaPagosPersonal= pagosPersonal.queryAll()
        
        self.pagoPersonalTipoValue = tk.StringVar()
        self.pagoPersonalTipoCombo =ttk.Combobox(self, textvariable=self.pagoPersonalTipoValue, justify='left', state='readonly')
        self.pagoPersonalTipoCombo['values'] = [pagoPersonal[1] for pagoPersonal in listaPagosPersonal]
        self.pagoPersonalTipoCombo.grid(row=3, column=1)

# -------------------------------------Valor del pago Widget ---------------------------
        pagoPersonalValorLabel = ttk.Label(self, text='Valor del Pago')
        pagoPersonalValorLabel.grid(row=2,column=2, **labelsColumnsOptions)

        pagoPersonalValorEntryValid = (self.register(self.validatePagoPersonalValor), '%P')
        pagoPersonalValorEntryInvalid = (self.register(self.inValidatePagoPersonalValor),)
        self.pagoPersonalValorValue=tk.StringVar()
        self.pagoPersonalValorEntry = ttk.Entry(self, textvariable=self.pagoPersonalValorValue, justify=tk.RIGHT)
        self.pagoPersonalValorEntry.grid(row=3, column=2, **valuesOptions)
        self.pagoPersonalValorEntry.config(validate='focusout',
                                        validatecommand=pagoPersonalValorEntryValid,
                                        invalidcommand=pagoPersonalValorEntryInvalid)
        self.pagoPersonalValorEntry.bind('<Return>', self.pagoPersonalValorEntryReturn)
        self.pagoPersonalValorEntry.bind('<KP_Enter>', self.pagoPersonalValorEntryReturn)

# ---------------------------------------Observacion widget ---------------------------
        pagoPersonalObservacionLabel = ttk.Label(self, text='Observaciones')
        pagoPersonalObservacionLabel.grid(row=2,column=3, **labelsColumnsOptions)

        pagoPersonalObservacionValid = (self.register(self.validatePagoPersonalObservacion),)
        pagoPersonalObservacionInvalid = (self.register(self.invalidatePagoPersonalObservacion),)
        self.pagoPersonalObservacionValue = tk.StringVar()
        self.pagoPersonalObservacionEntry = ttk.Entry(self, textvariable=self.pagoPersonalObservacionValue, justify='left') 
        self.pagoPersonalObservacionEntry.grid(row=3, column=3, **valuesOptions)
        self.pagoPersonalObservacionEntry.config(validate='focusout',
                                                validatecommand=pagoPersonalObservacionValid,
                                                invalidcommand=pagoPersonalObservacionInvalid)
        self.pagoPersonalObservacionEntry.bind('<Return>', self.pagoPersonalObservacionEntryReturn)
        self.pagoPersonalObservacionEntry.bind('<KP_Enter>', self.pagoPersonalObservacionEntryReturn)

# --------------------------------- Pagos Personal Tree View ---------------
        columnasPagosPersonal = ('empleado', 'tipoGastosPersonal', 'valorGastosPersonal', 'observaciones')
        self.pagosPersonalTree = ttk.Treeview(self, columns=columnasPagosPersonal, show='headings', selectmode='browse')
        self.pagosPersonalTree.heading('empleado', text='Empleado')
        self.pagosPersonalTree.heading('tipoGastosPersonal', text='Tipo de Pago')
        self.pagosPersonalTree.heading('valorGastosPersonal', text='Valor')
        self.pagosPersonalTree.heading('observaciones', text='Observaciones')
        self.pagosPersonalTree.grid(row=4, column=0, columnspan=4, sticky='nswe', pady=10)
        self.pagosPersonalTree.bind('<<TreeviewSelect>>', self.pagosPersonalTreeItemSelected)