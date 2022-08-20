import tkinter as tk
from tkinter import ttk
from modelo.locPagosPersonal import PagosPersonal
from modelo.igPersonas import Personas

class PagosPersonalFrame(ttk.Frame):
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
        estilo.configure('TRadiobutton', background=self.df.defaultColor)
        estilo.configure('Values.TLabel', relief='ridge')
        estilo.configure('TCombobox', background=self.df.defaultColor)
        estilo.configure('TEntry', width=10, borderwidth=1, background=self.df.defaultColor)
        valuesOptions = {'sticky': 'e', 'padx': 20, 'pady': 5}
        labelsColumnsOptions = {'sticky': 'n', 'padx': 10, 'pady': 5}

        selectListaPersonasFrame = ttk.Frame(self)
        selectListaPersonasFrame.grid(row=1, column=0, sticky='we')

        tituloLabel = ttk.Label(self, text='Detalle de Gastos de Personal', font=('Helvetica bold', 16))
        tituloLabel.grid(row=0, column=0, columnspan=4, pady=5, sticky='n')

        empleadoLabel = ttk.Label(self, text='Empleado')
        empleadoLabel.grid(row=2,column=0, **labelsColumnsOptions)

        localOrigenPagoPersonalLabel = ttk.Label(self, text='Tipo de Gastos')
        localOrigenPagoPersonalLabel.grid(row=2,column=1, **labelsColumnsOptions)

        valorGastoPersonalLabel = ttk.Label(self, text='Valor del Gasto')
        valorGastoPersonalLabel.grid(row=2,column=2, **labelsColumnsOptions)
        
        observacionPagoPersonalLabel = ttk.Label(self, text='Observaciones')
        observacionPagoPersonalLabel.grid(row=2,column=3, **labelsColumnsOptions)

        personas = Personas()
        listaPersonasLocal = personas.queryByIdLocal(self.df.rw.esteLocal[0])
        listaPersonasEmpresa = personas.queryAll()
        empleadoCombo = ttk.Combobox(self)
        # empleadoCombo['values'] = [f'{empleado[2]} {empleado[1]}' for empleado in listaPersonasLocal] 
        

        listaSeleccionada = tk.StringVar()
        listaSeleccionada.set('L')
        def setListaPersonas():
            if listaSeleccionada.get() == 'L':
                empleadoCombo['values'] = [f'{empleado[2]} {empleado[1]}' for empleado in listaPersonasLocal]
            else:
                empleadoCombo['values'] = [f'{empleado[2]} {empleado[1]}' for empleado in listaPersonasEmpresa]
        setListaPersonas()
        empleadoCombo['state'] = 'readonly'
        empleadoCombo.grid(row=3, column=0)

        pagosPersonal = PagosPersonal()
        listaPagosPersonal= pagosPersonal.queryAll()
        pagosPersonalCombo =ttk.Combobox(self)
        pagosPersonalCombo['values'] = [pagoPersonal[1] for pagoPersonal in listaPagosPersonal]
        pagosPersonalCombo['state'] ='readonly'
        pagosPersonalCombo.grid(row=3, column=1)

        valorPagoPersonalEntry = ttk.Entry(self)
        valorPagoPersonalEntry.grid(row=3, column=2, **valuesOptions)

        observacionPagoPersonalEntry = ttk.Entry(self) 
        observacionPagoPersonalEntry.grid(row=3, column=3, **valuesOptions)


        columnasPagosPersonal = ('empleado', 'tipoGastosPersonal', 'valorGastosPersonal', 'observaciones')
        pagosPersonalTree = ttk.Treeview(self, columns=columnasPagosPersonal, show='headings')
        pagosPersonalTree.heading('empleado', text='Empleado')
        pagosPersonalTree.heading('tipoGastosPersonal', text='Tipo de Pago')
        pagosPersonalTree.heading('valorGastosPersonal', text='Valor')
        pagosPersonalTree.heading('observaciones', text='Observaciones')
        pagosPersonalTree.grid(row=4, column=0, columnspan=4, sticky='nswe', pady=10)

        
        opcionesListas =  [('Este Local', 'L'), ('Todos los Locales', 'T')]
        for lista, valor in opcionesListas:
            ttk.Radiobutton(selectListaPersonasFrame, text=lista, variable=listaSeleccionada, command=setListaPersonas, value=valor).pack(side='left')
