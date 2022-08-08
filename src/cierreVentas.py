import tkinter as tk
from datetime import datetime
from CierreVentas.frames import headerFrame as hf
from CierreVentas.frames import commandFrame as cf
from CierreVentas.frames import dataFrame as df
# import modelo.locCierreVentas


class App(tk.Tk):

    defaultColor =  '#FFF8EF'
    ident = None
    datosDia = None

    def __init__(self) -> None:
        super().__init__()

        self.protocol('WM_DELETE_WINDOW', self.cerrarAplicacion)

        self.geometry('960x800')
        self.config(bg=self.defaultColor)
        self.title('Aplicaciones para registros de datos')

        self.identGet()
        self.datosDiaGet()

    def identGet(self):
        if self.ident !=  None:
            return self.ident
        else:
            self.ident = self.Login()
            if self.ident !=  None:
                return self.ident
            else:
                self.cerrarAplicacion()

    def Login(self):
        usuario = {'id': 265, 'nombres': 'José', 'apellidos': 'Tibau Iturralde'}
        lugar = {'idLocal': 1,'codLocal': 0, 'nombreLocal': 'Las Plameras Planta'}
        fecha = datetime.now()
        return {'usuario': usuario, 'lugar': lugar, 'fecha': fecha }

    def cerrarAplicacion(self):
        # print('Save data')
        self.quit()

    def datosDiaGet(self):
        pass

    def crearFrames(self):

        self.dataFrames = {
            'headerFrame': hf.HeaderFrame(self),
            'commandFrame': cf.CommandFrame(self),
            'dataFrame': df.DataFrame(self)
        }

    def cambiarFrames(self, destino):
        self.dataFrames['dataFrame'].cambiarFrame(destino)


# class CrearFrames():
#     appWindow = None

#     def __init__(self, appWindow):

#         self.appWindow = appWindow

#         self.dataFrames = {
#             'headerFrame': hf.HeaderFrame(appWindow),
#             'commandFrame': cf.CommandFrame(appWindow),
#             'dataFrame': df.DataFrame(appWindow)
#         }


if __name__ == '__main__':
    app = App()
    app.crearFrames()
    app.mainloop()