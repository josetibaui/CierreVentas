
import tkinter as tk
from tkinter import ttk




class ControlFrame(tk.Frame):

    def __init__(self, rootWindow, defaultColor):
        super().__init__(rootWindow)

        self.defaultcolor = defaultColor

        self.config(bg=defaultColor)
        self.config( highlightthickness=1)

        resumenFrame = self.crearResumenFrame()

        self.pack(expand=True, fill='both')

        

    def crearResumenFrame(self):
        resumenFrame = tk.Frame(self, bg=self.defaultcolor)

        titulo = tk.Label(resumenFrame, text='RESUMEN DE DATOS')

        return resumenFrame
        

    
class DataFrame():
    pass