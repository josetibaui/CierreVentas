import tkinter as tk
from tkinter import ttk
from CierreVentas.frames import dataFrame as df


class CommandFrame(ttk.Frame):
    def __init__(self, rootWindow):
        super().__init__(rootWindow)

        self.rw = rootWindow
        estilo = ttk.Style(self.rw)
        estilo.configure('TFrame', background=self.rw.defaultColor)
        estilo.configure('TLabel', background=self.rw.defaultColor)
        estilo.configure('TButton', background=self.rw.defaultColor)

        self.pack(side='left', fill='y')
        self.crearWidgets()

    def crearWidgets(self):
        resumenButton = ttk.Button(self, text='Resumen', command=lambda:self.cambiarFrame('resumenFrame'))
        ventasButton = ttk.Button(self, text='Ventas', command=lambda:self.cambiarFrame('ventasFrame'))
        formasPagoButton = ttk.Button(self, text='Formas de Pago', command=lambda:self.cambiarFrame('formasPagosFrame'))
        gastosGeneralesButton = ttk.Button(self, text='Gastos Generales', command=lambda:self.cambiarFrame('gastosGeneralesFrame'))
        gastosPersonalButton = ttk.Button(self, text='Gastos de Personal', command=lambda:self.cambiarFrame('gastosPersonalFrame'))
        depositosButton = ttk.Button(self, text='Depósitos', command=lambda:self.cambiarFrame('depositosFrame'))
        salirButton =ttk.Button(self, text='Salir', command=lambda:self.rw.cerrarAplicacion())

        # resumenButton.pack(fill='x', expand=True)
        # ventasButton.pack(fill='x', expand=True)
        # formasPagoButton.pack(fill='x', expand=True)
        # gastosGeneralesButton.pack(fill='x', expand=True)
        # gastosPersonalButton.pack(fill='x', expand=True)
        # depositosButton.pack(fill='x', expand=True)
        # salirButton.pack(fill='x', expand=True)

        padOptions = {'pady': 5, 'padx': 10}
        resumenButton.pack(fill='x', **padOptions)
        ventasButton.pack(fill='x', **padOptions)
        formasPagoButton.pack(fill='x', **padOptions)
        gastosGeneralesButton.pack(fill='x', **padOptions)
        gastosPersonalButton.pack(fill='x', **padOptions)
        depositosButton.pack(fill='x', **padOptions)
        salirButton.pack(fill='x', **padOptions)

    def cambiarFrame(self, destino):
        self.rw.cambiarFrames(destino)