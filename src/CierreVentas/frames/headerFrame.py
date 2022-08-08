import tkinter as tk
from tkinter import ttk

class HeaderFrame(ttk.Frame):
    def __init__(self, rootWindow):
        super().__init__(rootWindow)

        rw = rootWindow
        estilo = ttk.Style(rw)
        estilo.configure('TFrame', background=rw.defaultColor)
        estilo.configure('TLabel', background=rw.defaultColor)

        self.pack(fill='x')
        # identificacion = rw.identificacion
        self.usuario = rw.ident['usuario']
        self.lugar = rw.ident['lugar']
        self.fecha = rw.ident['fecha']
        self.crearWidgets(rw)

    def crearWidgets(self, rw):
        rw.logo = tk.PhotoImage(file='./img/LasPalmerasLogotipo.png', height=100, width=174)
        logoLabel = ttk.Label(self, image=rw.logo)

        tituloLabel = ttk.Label(self, text='Cierre Diario de Ventas', justify='center', font=('Helvetica', 20))
        identFrame = ttk.Frame(self)

        localLabel = ttk.Label(identFrame, text=self.lugar['nombreLocal'])
        fechaLabel = ttk.Label(identFrame, text=self.fecha.strftime('%d-%m-%Y'))
        userLabel = ttk.Label(identFrame, text=self.usuario['nombres']+' '+self.usuario['apellidos'])

        localLabel.pack(fill='both', padx=5)
        fechaLabel.pack(fill='both', padx=5)
        userLabel.pack(fill='both', padx=5)

        logoLabel.pack(side='left', fill='both')
        identFrame.pack(side='right')
        tituloLabel.pack(expand=True)
