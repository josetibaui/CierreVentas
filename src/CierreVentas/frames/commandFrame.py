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
        self.botones = {
            'resumenButton': ttk.Button(self, text='Resumen', command=lambda:self.cambiarFrame('resumenFrame')),
            'ventasButton': ttk.Button(self, text='Ventas', command=lambda:self.cambiarFrame('ventasFrame')),
            'formasPagoButton': ttk.Button(self, text='Formas de Pago', command=lambda:self.cambiarFrame('formasPagosFrame')),
            'gastosGeneralesButton': ttk.Button(self, text='Gastos Generales', command=lambda:self.cambiarFrame('gastosGeneralesFrame')),
            'pagosPersonalButton': ttk.Button(self, text='Pagos al Personal', command=lambda:self.cambiarFrame('pagosPersonalFrame')),
            'depositosButton': ttk.Button(self, text='Depósitos', command=lambda:self.cambiarFrame('depositosFrame')),
            'salirButton': ttk.Button(self, text='Salir', command=lambda:self.rw.cerrarAplicacion()),
        }

        padOptions = {'pady': 5, 'padx': 10}
        for nombre, boton in self.botones.items():
            boton.pack(fill='x', **padOptions)

    def cambiarFrame(self, destino):
        self.rw.cambiarFrames(destino)
        