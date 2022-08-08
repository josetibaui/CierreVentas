import tkinter as tk
from tkinter import ttk
from CierreVentas.frames import resumenFrame
from CierreVentas.frames import ventasFrame
from CierreVentas.frames import formasPagosFrame
from CierreVentas.frames import gastosGeneralesFrame
from CierreVentas.frames import gastosPersonalFrame
from CierreVentas.frames import depositosFrame

class DataFrame(ttk.Frame):
    def __init__(self, rootWindow):
        super().__init__(rootWindow)

        self.rw = rootWindow
        self.defaultColor = rootWindow.defaultColor
        estilo = ttk.Style(self.rw)
        estilo.configure('TFrame', background=self.rw.defaultColor)

        self.pack(side='left', fill='both', expand=True)

        self.crearDataFrames()

    def crearDataFrames(self):

        self.frames = {
            'resumenFrame': resumenFrame.ResumenFrame(self),
            'ventasFrame': ventasFrame.VentasFrame(self),
            'formasPagosFrame': formasPagosFrame.FormasPagosFrame(self),
            'gastosGeneralesFrame': gastosGeneralesFrame.GastosGeneralesFrame(self),
            'gastosPersonalFrame': gastosPersonalFrame.GastosPersonalFrame(self),
            'depositosFrame': depositosFrame.DepositosFrame(self)
        }

        self.cambiarFrame('resumenFrame')

    def gridConfigure(self, subFrame):
        subFrame.columnconfigure(0, weight=1)
        subFrame.columnconfigure(1, weight=1)
        subFrame.columnconfigure(2, weight=1)
        subFrame.columnconfigure(3, weight=1)

        subFrame.rowconfigure(0, weight=3)
        subFrame.rowconfigure(1, weight=1)
        subFrame.rowconfigure(3, weight=1)
        subFrame.rowconfigure(5, weight=1)
        subFrame.rowconfigure(7, weight=1)
        subFrame.rowconfigure(9, weight=1)
        subFrame.rowconfigure(2, weight=1)
        subFrame.rowconfigure(4, weight=1)
        subFrame.rowconfigure(6, weight=1)
        subFrame.rowconfigure(8, weight=1)
        subFrame.rowconfigure(10, weight=1)

        # resumenFrame = ttk.Frame(dataFrame, bg=defaultColor, highlightthickness=1)
        # resumenFrame.grid(row=0, column=0, sticky='nsew')
        # crearWidgetsResumen(resumenFrame)

        # ventasFrame = tk.Frame(dataFrame, bg=defaultColor, highlightthickness=1)
        # ventasFrame.grid(row=0, column=0, sticky='nsew')
        # crearWidgetsVentas(ventasFrame)

        # formasPagoFrame = tk.Frame(dataFrame, bg=defaultColor, highlightthickness=1)
        # formasPagoFrame.grid(row=0, column=0, sticky='nsew')
        # crearWidgetsFormasPago(formasPagoFrame)

        # gastosGeneralesFrame = tk.Frame(dataFrame, bg=defaultColor, highlightthickness=1)
        # gastosGeneralesFrame.grid(row=0, column=0, sticky='nsew')
        # crearWigetsgastosGenerales(gastosGeneralesFrame)

        # gastosPersonalFrame = tk.Frame(dataFrame, bg=defaultColor, highlightthickness=1)
        # gastosPersonalFrame.grid(row=0, column=0, sticky='nsew')
        # crearWigetsGastosPersonal(gastosPersonalFrame)

        # depositosFrame = tk.Frame(dataFrame, bg=defaultColor, highlightthickness=1)
        # depositosFrame.grid(row=0, column=0, sticky='nsew')
        # crearWigetsDepositos(depositosFrame)

        # resumenFrame.tkraise()


    def cambiarFrame(self, destino):
        self.frames[destino].tkraise()