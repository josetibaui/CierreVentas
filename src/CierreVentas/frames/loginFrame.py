import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showerror, showinfo, showwarning
from CierreVentas.frames import commandFrame
from modelo.igPersonas import Personas
from passlib.hash import sha512_crypt as sha512


class LoginFrame(ttk.Frame):
    def __init__(self, dataFrame, headerFrame, commandFrame) -> None:
        super().__init__(dataFrame)


        self.df = dataFrame
        self.cf = commandFrame
        self.hf = headerFrame
        self.grid(row=0, column=0, sticky='n')

        # Desactivar los botones del frame command
        for nombre, boton in commandFrame.botones.items():
            if nombre != 'salirButton':
                boton.state(['disabled'])
        
        self.crearWidgets()
        self.initFocus()

    def usuarioEntryReturn(self, event):
        self.contrasenaEntry.focus()

    def contrasenaEntryReturn(self, event):
        self.loginButton.focus()

    def loginButtonReturn(self, event):
        self.checkUser()

    def crearWidgets(self):

        estilo = ttk.Style(self.df)
        estilo.configure('TFrame', background=self.df.defaultColor)
        estilo.configure('TLabel', background=self.df.defaultColor)
        estilo.configure('TButton', background=self.df.defaultColor)


        self.usuario = tk.StringVar()
        self.contrasena = tk.StringVar()
        
        usuarioLabel = ttk.Label(self, text='Usuario ')
        contasenaLabel = ttk.Label(self, text='Contraseña ')

        self.usuarioEntry = ttk.Entry(self, textvariable=self.usuario)
        self.usuarioEntry.bind('<Return>', self.usuarioEntryReturn)
        self.usuarioEntry.bind('<KP_Enter>', self.usuarioEntryReturn)

        self.contrasenaEntry = ttk.Entry(self, show='-', textvariable=self.contrasena)
        self.contrasenaEntry.bind('<Return>', self.contrasenaEntryReturn)
        self.contrasenaEntry.bind('<KP_Enter>', self.contrasenaEntryReturn)

        self.loginButton=ttk.Button(self, text='Ingresar', command=self.checkUser)
        self.loginButton.bind('<Return>', self.loginButtonReturn)
        self.loginButton.bind('<KP_Enter>', self.loginButtonReturn)

        padOptions ={'pady': 5}
        
        usuarioLabel.grid(row=0, column=0, sticky=tk.W, **padOptions)
        contasenaLabel.grid(row=1, column=0, sticky=tk.W, **padOptions)
        
        self.usuarioEntry.grid(row=0, column=1, sticky=tk.E, **padOptions)
        
        self.contrasenaEntry.grid(row=1, column=1, sticky=tk.E, **padOptions)
        self.loginButton.grid(row=2, column=1)
        
    def checkUser(self):
        persona = Personas()
        user = persona.checkAuth(self.usuario.get(), self.contrasena.get(), self.df.rw.esteLocal[0])
        if user == None:
            showwarning(title='Usuario incorrecto', message='Hay una discrepancia entre el usuario, la contraseña y el local')
            self.usuario.set('')
            self.contrasena.set('')
            self.usuarioEntry.focus()
        else:
            self.df.rw.ident = user
            for nombre, boton in self.cf.botones.items():
                if nombre != 'salirButton':
                    boton.state(['!disabled'])
            self.hf.crearIdentWidgets(self.df.rw.esteLocal, user)
            self.df.cambiarFrame('ventasFrame')
            self.destroy()

    def initFocus(self):
        self.usuarioEntry.focus()
