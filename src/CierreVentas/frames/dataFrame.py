import tkinter as tk
from tkinter import ttk
from CierreVentas.frames import loginFrame
from CierreVentas.frames import resumenFrame
from CierreVentas.frames import ventasFrame
from CierreVentas.frames import formasPagosFrame
from CierreVentas.frames import gastosGeneralesFrame
from CierreVentas.frames import pagosPersonalFrame
from CierreVentas.frames import depositosFrame
from CierreVentas.frames import blankFrame

class DataFrame(ttk.Frame):
    def __init__(self, rootWindow, headerFrame, commandFrame):
        super().__init__(rootWindow)

        self.rw = rootWindow
        self.defaultColor = rootWindow.defaultColor
        estilo = ttk.Style(self.rw)
        estilo.configure('TFrame', background=self.defaultColor, highlightthickness=1)
        self['borderwidth'] = 1
        self['relief'] = 'solid'
        self.pack(side='left', fill='both', expand=True)

        self.crearDataFrames(headerFrame, commandFrame)

    def crearDataFrames(self, headerFrame, commandFrame):

        self.dataFrames = {
            'loginFrame': loginFrame.LoginFrame(self, headerFrame, commandFrame),
            'ventasFrame': ventasFrame.VentasFrame(self),
            'resumenFrame': resumenFrame.ResumenFrame(self),
            'formasPagosFrame': formasPagosFrame.FormasPagosFrame(self),
            'gastosGeneralesFrame': gastosGeneralesFrame.GastosGeneralesFrame(self),
            'pagosPersonalFrame': pagosPersonalFrame.PagosPersonalFrame(self),
            'depositosFrame': depositosFrame.DepositosFrame(self),
            'blankFrame': blankFrame.BlankFrame(self)
        }    

        self.cambiarFrame('loginFrame')
        # self.dataFrames['loginFrame'].usuarioEntry.focus()

    def gridConfigure(self, subFrame):
        subFrame.columnconfigure(0, weight=1)
        subFrame.columnconfigure(1, weight=3)
        subFrame.columnconfigure(2, weight=1)
        subFrame.columnconfigure(3, weight=3)

        subFrame.rowconfigure(0, weight=3)
        subFrame.rowconfigure(1, weight=1)
        subFrame.rowconfigure(2, weight=1)
        subFrame.rowconfigure(3, weight=1)
        subFrame.rowconfigure(4, weight=1)
        subFrame.rowconfigure(5, weight=1)
        subFrame.rowconfigure(6, weight=1)
        subFrame.rowconfigure(7, weight=1)
        subFrame.rowconfigure(8, weight=1)
        subFrame.rowconfigure(9, weight=1)
        subFrame.rowconfigure(10, weight=1)


    def cambiarFrame(self, destino):
        self.dataFrames[destino].tkraise()
        if destino == 'loginFrame':
            self.dataFrames['loginFrame'].usuarioEntry.focus()
        if destino == 'ventasFrame':
            self.dataFrames['ventasFrame'].ventasEntry.focus()
        elif destino == 'formasPagosFrame':
            self.dataFrames['formasPagosFrame'].formaPagoTipoCombo.focus()
        elif destino == 'gastosGeneralesFrame':
            self.dataFrames['gastosGeneralesFrame'].gastoGeneralTipoCombo.focus()
        elif destino == 'pagosPersonalFrame':
            self.dataFrames['pagosPersonalFrame'].empleadosCombo.focus()
        elif destino == 'depositosFrame':
             self.dataFrames['depositosFrame'].bancoDepositosCombo.focus()
