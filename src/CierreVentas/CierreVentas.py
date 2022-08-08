import tkinter as tk
from src.frames.headerFrame import HeaderFrame



class CierreVentas(tk.Tk):

    defaultColor =  '#FFF8EF'

    def __init__(self) -> None:
        super().__init__()

        

        self.protocol('WM_DELETE_WINDOW', self.cerrarVentana())
        self.geometry('960x600')
        self.config(bg=self.defaultColor)
        self.title('Sistema de registro de datos')

        self.crearFrames()

    def crearFrames(self):
        HeaderFrame(self)
        # dataFrame = DataFrame()
        # commanFrame = CommandFrame()

    def cerrarVentana(self):
        self.quit()

if __name__ == '__main__':
    cierreVentas = CierreVentas()
    cierreVentas.mainloop()
