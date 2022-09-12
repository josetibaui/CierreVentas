from decimal import Decimal, InvalidOperation, getcontext
import tkinter as tk
from tkinter import ANCHOR, ttk



class ResumenFrame(ttk.Frame):
    def __init__(self, dataFrame):
        super().__init__(dataFrame)

        self.df = dataFrame
        self.grid(row=0, column=0, sticky='nsew')

        self.datosHoy = dataFrame.datosHoy
        dataFrame.gridConfigure(self)
        self.crearWidgets()

        self.bind('<Enter>', self.resumenFrameEnter)
        self.bind('<Leave>', self.resumenFrameExit)

    def resumenFrameEnter(self, event):
        self.resumenFrameSetValues()

    def resumenFrameSetValues(self):
        getcontext().prec = 4

#-------------Ventas-----------------------
        ventas = self.datosHoy['Ventas']
        ventaTotal = float(ventas['VentaTotal'])
        devoluciones = ventas['Devoluciones']
        anulaciones = ventas['Anulaciones']
        totalCortesias = 0.0
        listaCortesias = ventas['Cortesias']
        for cortesia in listaCortesias:
            totalCortesias+= cortesia[1]

        self.valores['ventas'].set(ventaTotal)
        self.valores['anulaciones'].set(anulaciones)
        self.valores['devoluciones'].set(devoluciones)
        self.valores['cortesias'].set(totalCortesias)

        # self.valores['ventas'].set('{:-.2f}'.format(ventaTotal))
        # self.valores['anulaciones'].set('{:-.2f}'.format(anulaciones))
        # self.valores['devoluciones'].set('{:-.2f}'.format(devoluciones))
        # self.valores['cortesias'].set('{:-.2f}'.format(totalCortesias))

# ----------------------------Formas de Pago ----------------------------------------
        # try:
        #     efectivo = float(self.datosHoy['FormasPagos']['Efectivo'])
        # except InvalidOperation:
        #     efectivo = 0

        valor = self.datosHoy['FormasPagos']['Efectivo']
        if valor == None or valor == '':
            valor = 0.0
        efectivo = float(valor)

        self.valores['efectivo'].set('{:-.2f}'.format(efectivo))
        totalFormasPagos = 0
        for formaPago in self.datosHoy['FormasPagos']['FormasPagos']:
            totalFormasPagos += float(formaPago[1])

        self.valores['formasPagos'].set('{:-.2f}'.format(totalFormasPagos))

# -----------------------------Gastos Generales --------------------------------------
        totalGastosGenerales = 0
        for gastoGeneral in self.datosHoy['GastosGenerales']:
            totalGastosGenerales += float(gastoGeneral[1])
        self.valores['gastosGenerales'].set('{:-.2f}'.format(totalGastosGenerales))

#--------------------------------Pagos Personal -----------------------------------------
        totalPagosPersonal = 0
        for pagoPersonal in self.datosHoy['PagosPersonal']:
            totalPagosPersonal += float(pagoPersonal[2])
        self.valores['pagosPersonal'].set('{:-.2f}'.format(totalPagosPersonal))

#---------------------------------Depósitos---------------------------------------------
        totalDepositos = 0
        for deposito in self.datosHoy['Depositos']:
            totalDepositos += float(deposito[1])
        self.valores['depositos'].set('{:-.2f}'.format(totalDepositos))

#---------------------------------Diferencia --------------------------------------------
        # print(f'-------------------Tipo venta total: {type(ventaTotal)}--------------------------------')
        diferenciaValor = ventaTotal - totalFormasPagos - totalGastosGenerales - totalPagosPersonal - totalDepositos
        self.valores['diferencia'].set('{:-.2f}'.format(diferenciaValor))

#---------------------------------Salida delFrame --------------------------------------
    def resumenFrameExit(self, event):
        pass

#=======================================Crear Widgets =========================
    def crearWidgets(self):

        estilo = ttk.Style(self)
        estilo.configure('TLabel', background=self.df.defaultColor, anchor='e')
        estilo.configure('TEntry', background=self.df.defaultColor, anchor='e')
        estilo.configure('Values.TLabel', relief='ridge')
        labelsOptions = {'sticky': 'w', 'padx': 20, 'pady': 5}
        valuesOptions = {'sticky': 'e', 'padx': 20, 'pady': 5}


        tituloLabel = ttk.Label(self, text='Resumen de Datos Registrados', font=('Helvetica bold', 16))
        tituloLabel.grid(row=0, column=0, columnspan=4, pady=20)

        '''
            Base Name, Label Text, row, column label, column value
        '''
        widgets = [
            ('ventas', 'Venta Total del Día', 2, 0, 1),
            ('gastosGenerales', 'Total Gastos Generales', 3, 0, 1),
            ('pagosPersonal', 'Total Gastos de Personal', 4, 0, 1),
            ('depositos', 'Total Depósitos', 5, 0, 1),
            ('diferencia', 'Diferencia', 6, 0, 1),
            ('efectivo', 'Pagos en efectivo', 1, 2, 3),
            ('formasPagos', 'Total de Formas de Pago', 2, 2, 3),
            ('anulaciones', 'Total Anulaciones', 3, 2, 3),
            ('devoluciones', 'Total Devoluciones', 4, 2, 3),
            ('cortesias', 'Total Cortesías', 5, 2, 3),
            ('dummy7', None, 7, 0, 1),
            ('dummy8', None, 8, 0, 1),
            ('dummy9', None, 9, 0, 1),
            ('dummy10', None, 10, 0, 1),
        ]

        self.valores = {}
        for widget in widgets:
            if widget[1] != None:
                widgetLabel = widget[0] + 'Label'
                widgetText = widget[1]
                widgetEntry = widget[0] + 'Entry'
                widgetRow = widget[2]
                widgetLabelColumn = widget[3]
                widgetEntryColumn = widget[4]


                widgetLabel = ttk.Label(self, text=widgetText)
                widgetLabel.grid(row=widgetRow, column=widgetLabelColumn, **labelsOptions)

                self.valores[widget[0]] = tk.StringVar()
                widgetEntry = ttk.Entry(self, textvariable=self.valores[widget[0]], takefocus=0, state='readonly', justify=tk.RIGHT)
                widgetEntry.grid(row=widgetRow, column=widgetEntryColumn, **labelsOptions)
