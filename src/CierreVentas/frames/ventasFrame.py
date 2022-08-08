import tkinter as tk
from tkinter import ttk

class VentasFrame(ttk.Frame):
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


        tituloLabel = ttk.Label(self, text='Detalle de Ventas, anulaciones y Cortesías del Día', font=('Helvetica bold', 16))
        tituloLabel.grid(row=0, column=0, columnspan=4, pady=20, sticky='n')

        '''
            Label Name, Label Text, Value Label Name, row, column label, column value or entry 
        '''

        widgets = [
            ('ventasLabel', 'Venta Total del día', 'ventasEntry', 1, 0, 1),
            ('anulacionesLabel', 'Venta Total del día', 'anulacionesEntry', 2, 0, 1),
            ('devolucionesLabel', 'Devoluciones del día', 'devolucionesEntry', 3, 0, 1),
            ('cortesiasLabel', 'Cortesías de día', None, 5, 0, None),
            ('cortesiaTipoLabel,', 'Tipo de Cortesía', 'cortesiaTipoEntry', 4, 1, 5),
            ('cortesiaValorLabel', 'Valor de la Cortesía', 'cortesiaValorEntry', 4, 2, 5),
            ('cortesiaObservacionLabel', 'Observaciones', 'cortesiasObservacionEntry', 4, 3, 5)
        ]

        for widget in widgets:
            nameLabel = widget[0]
            textLabel = widget[1]
            valueLabel = widget[2]
            rowLabel = widget[3]
            columnNameLabel = widget[4]
            columnValueLabel = widget[5]

            nameLabel = ttk.Label(self, text=textLabel)
            nameLabel.grid(row=rowLabel, column=columnNameLabel, **stickyLabelsOptions)

            # if rowLabel != None:
            #     valueLabel = ttk.Label(self, text='0.00', style='Values.TLabel')
            #     valueLabel.grid(row=rowLabel, column=columnValueLabel, **stickyValuesOptions)

        # ventasLabel = ttk.Label(self, text='Venta Total del día')
        # ventasLabel.grid(row=1, column=0, **stickyLabelsOptions)
        # ventasEntry = ttk.Entry(self)
        # ventasEntry.grid(row=1, column=1, **stickyEntryOptions)
        
        # anulacionesLabel = ttk.Label(self, text='Anulaciones del día')
        # anulacionesLabel.grid(row=2, column=0, **stickyLabelsOptions)
        # anulacionesEntry = ttk.Entry(self)
        # anulacionesEntry.grid(row=2, column=1, **stickyEntryOptions)

        # devolucionesLabel = ttk.Label(self, text='Devoluciones del día')
        # devolucionesLabel.grid(row=3, column=0, **stickyLabelsOptions)
        # devolucionesEntry = ttk.Entry(self)
        # devolucionesEntry.grid(row=3, column=1, **stickyEntryOptions)

        # cortesiasLabel = ttk.Label(self, text='Cortesías de día')
        # cortesiasLabel.grid(row=5, column=0, **stickyLabelsOptions)

        # cortesiaTipoLabel = ttk.Label(self, text='Tipo de Cortesía')
        # cortesiaTipoLabel.grid(row=4, column=1, **stickyLabelsEntryOptions)
        # cortesiaTipoEntry = ttk.Entry(self)
        # cortesiaTipoEntry.grid(row=5, column=1, **stickyEntryOptions)

        # cortesiaValorLabel = ttk.Label(self, text='Valor de la Cortesía')
        # cortesiaValorLabel.grid(row=4, column=2, **stickyLabelsEntryOptions)
        # cortesiaValorEntry = ttk.Entry(self)
        # cortesiaValorEntry.grid(row=5, column=2, **stickyEntryOptions)

        # cortesiaObservacionLabel = ttk.Label(self, text='Observaciones')
        # cortesiaObservacionLabel.grid(row=4, column=3, **stickyLabelsEntryOptions)
        # cortesiasObservacionEntry = ttk.Entry(self)
        # cortesiasObservacionEntry.grid(row=5, column=3,**stickyEntryOptions)


        columnasCortesias =('tipo', 'valor', 'observacion')
        cortesiasTree = ttk.Treeview(self, columns=columnasCortesias, show='headings')
        cortesiasTree.heading('tipo', text='Tipo de Cortesía')
        cortesiasTree.heading('valor', text='Valor de Cortesía')
        cortesiasTree.heading('observacion', text='Observaciones')

        cortesiasTree.grid(row=6, column=1, columnspan=3, pady=10)
