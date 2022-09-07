import tkinter as tk
import os
from datetime import datetime
from tkinter.messagebox import showerror
from CierreVentas.frames import headerFrame as hf
from CierreVentas.frames import commandFrame as cf
from CierreVentas.frames import dataFrame as df
from modelo.igLocales import Locales


class App(tk.Tk):

    defaultColor =  '#FFF8EF'
    esteLocal = None
    ident = None
    datosDia = None

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

    
    # def identGet(self):
    #     if self.ident !=  None:
    #         return self.ident
    #     else:
    #         self.ident = self.Login()
    #         if self.ident !=  None:
    #             return self.ident
    #         else:
    #             self.cerrarAplicacion()

    # def Login(self):

    #     # usuario = {'id': 265, 'nombres': 'José', 'apellidos': 'Tibau Iturralde'}
    #     # lugar = {'idLocal': 1,'codLocal': 0, 'nombreLocal': 'Las Plameras Planta'}
    #     # fecha = datetime.now()
    #     usuario = None
    #     lugar = None
    #     fecha = datetime.now()
    #     loginFrame = login.Login(self, self.esteLocal, self.defaultColor)
    #     if usuario == None or lugar == None:
    #         showerror(f'Hay una discrepancia entre el usuario, la contraseña y el local.')
    #     return {'usuario': usuario, 'lugar': lugar, 'fecha': fecha }

    def cerrarAplicacion(self):
        self.quit()

    def datosDiaGet(self):
        pass

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