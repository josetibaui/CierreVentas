import tkinter as tk
from tkinter import ttk
from datetime import datetime

class HeaderFrame(ttk.Frame):
    def __init__(self, rootWindow):
        super().__init__(rootWindow)

        self.rw = rootWindow
        estilo = ttk.Style(self.rw)
        estilo.configure('TFrame', background=self.rw.defaultColor)
        estilo.configure('TLabel', background=self.rw.defaultColor)

        self.pack(fill='x')
        self.crearWidgets()

    def crearWidgets(self):
        self.rw.logo = tk.PhotoImage(file='./img/LasPalmerasLogotipo.png', height=100, width=174)
        logoLabel = ttk.Label(self, image=self.rw.logo)

        tituloLabel = ttk.Label(self, text='Cierre Diario de Ventas', justify='center', font=('Helvetica', 20))
        self.identFrame = ttk.Frame(self)

        logoLabel.pack(side='left', fill='both')
        self.identFrame.pack(side='right')
        tituloLabel.pack(expand=True)

    def crearIdentWidgets(self, esteLocal, usuario):
        localLabel = ttk.Label(self.identFrame, text=esteLocal[2])
        fechaLabel = ttk.Label(self.identFrame, text= datetime.now().strftime('%d-%m-%Y'))
        userLabel = ttk.Label(self.identFrame, text=usuario[1]+' '+usuario[2])

        localLabel.pack(fill='both', padx=5)
        fechaLabel.pack(fill='both', padx=5)
        userLabel.pack(fill='both', padx=5)