import tkinter as tk
import os
from datetime import datetime, date
from tkinter.messagebox import showerror
from CierreVentas.frames import headerFrame as hf
from CierreVentas.frames import commandFrame as cf
from CierreVentas.frames import dataFrame as df
from modelo.igLocales import Locales
from modelo.locCierreVentas import CierreVentas


class App(tk.Tk):

    defaultColor =  '#FFF8EF'
    esteLocal = None
    ident = None
    datosHoy = None

    def __init__(self) -> None:
        super().__init__()

        self.protocol('WM_DELETE_WINDOW', self.cerrarAplicacion)

        self.geometry('960x800')
        self.config(bg=self.defaultColor)
        self.title('Aplicaciones para registros de datos')

        self.esteLocal = self.esteLocalGet()
        
        if self.esteLocal:
            self.datosDiaGet()

    def esteLocalGet(self):
        with open('./EsteLocal') as f:
            codLocal = f.read()
        local = Locales()
        esteLocal = local.queryBycodLocal(codLocal)
        if esteLocal == None:
            showerror(title='Error en el local', message='No se puede determinar los datos de este local')
        return esteLocal

    def cerrarAplicacion(self):
        self.mainFrames['dataFrame'].saveData()
        self.quit()

    def datosDiaGet(self):
        hoy = date.today()
        self.cierreVentas = CierreVentas()
        self.cierreVentas.queryByLocalFecha(self.esteLocal[0], hoy)
        self.datosHoy = self.cierreVentas.data

    def crearFrames(self):

        headerFrame = hf.HeaderFrame(self)
        commandFrame = cf.CommandFrame(self)
        dataFrame = df.DataFrame(self, headerFrame, commandFrame)
        self.mainFrames = {
            'headerFrame': headerFrame,
            'commandFrame': commandFrame,
            'dataFrame': dataFrame
        }

    def cambiarFrames(self, destino):
        self.mainFrames['dataFrame'].cambiarFrame(destino)

if __name__ == '__main__':
    app = App()
    if app.esteLocal:
        app.crearFrames()
        app.mainloop()