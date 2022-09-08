import tkinter as tk
from tkinter import ANCHOR, ttk



class ResumenFrame(ttk.Frame):
    def __init__(self, dataFrame):
        super().__init__(dataFrame)

        self.df = dataFrame
        self.grid(row=0, column=0, sticky='nsew')

        dataFrame.gridConfigure(self)
        self.crearWidgets()


    def crearWidgets(self):

        estilo = ttk.Style(self)
        estilo.configure('TLabel', background=self.df.defaultColor, anchor='e')
        estilo.configure('Values.TLabel', relief='ridge')
        labelsOptions = {'sticky': 'w', 'padx': 20, 'pady': 5}
        valuesOptions = {'sticky': 'e', 'padx': 20, 'pady': 5}


        tituloLabel = ttk.Label(self, text='Resumen de Datos Registrados', font=('Helvetica bold', 16))
        tituloLabel.grid(row=0, column=0, columnspan=4, pady=20)


        '''
            Label Name, Label Text, Value Label Name, row, column label, column value
        '''
        widgets = [
            ('ventasLabel', 'Venta Total del Día', 'valorVentas', 1, 0, 1),
            ('gastosGeneralesLabel', 'Total Gastos Generales', 'valorGastosGenerales', 2, 0, 1),
            ('gastosPersonalLabel', 'Total Gastos de Personal', 'valorGastosPersonal', 3, 0, 1),
            ('depositosLabel', 'Total Depósitos', 'valorDepositos', 4, 0, 1),
            ('difrenciaLabel', 'Diferencia', 'valorDiferencia', 5, 0, 1),
            ('formasPagosLabel', 'Total de Formas de Pago', 'valorformasPagos', 1, 2, 3),
            ('anulacionesLabel', 'Total Anulaciones', 'valorAnulaciones', 2, 2, 3),
            ('devolucionesLabel', 'Total Devoluciones', 'valorDevoluciones', 3, 2, 3),
            ('cortesiasLabel', 'Total Cortesías', 'valorCortesias', 4, 2, 3),
            ('dummy6', None, 'vdummy6', 6, 0, 1),
            ('dummy7', None, 'vdummy7', 7, 0, 1),
            ('dummy8', None, 'vdummy8', 8, 0, 1),
            ('dummy9', None, 'vdummy9', 9, 0, 1),
            ('dummy10', None, 'vdummy10', 10, 0, 1),
        ]
        for widget in widgets:
            nameLabel = widget[0]
            textLabel = widget[1]
            valueLabel = widget[2]
            rowLabel = widget[3]
            columnNameLabel = widget[4]
            columnValueLabel = widget[5]

            nameLabel = ttk.Label(self, text=textLabel)
            nameLabel.grid(row=rowLabel, column=columnNameLabel, **labelsOptions)

            if textLabel != None:
                valueLabel = ttk.Label(self, text='0.00', style='Values.TLabel')
                valueLabel.grid(row=rowLabel, column=columnValueLabel, **valuesOptions)
