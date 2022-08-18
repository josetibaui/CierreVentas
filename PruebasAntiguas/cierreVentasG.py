import tkinter as tk

defaultColor =  '#FFF8EF'

def logoCreate(rootWindow):

    global defaultColor
    rootWindow.logoImg = tk.PhotoImage(file='./img/LasPalmerasLogotipo.png', height=100, width=174)
    logoLabel = tk.Label(rootWindow, image=rootWindow.logoImg, bg=defaultColor)
    return logoLabel


class RootWindow(tk.Tk):

    global defaultColor

    def __init__(self):
        super().__init__()


        self.geometry('800x600')
        # self.config(bg=defaultColor)
        self.title('Sistema de registro de datos')

        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=10)
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=10)


        # self.logoImg = tk.PhotoImage(file='/home/USERS/jtibau/Desarrollo/Palmeras/CierreVentas/img/LasPalmerasLogotipo.png', height=100, width=174)
        # logoLabel = tk.Label(self, image=logoImg).grid(row=0,column=0,sticky=tk.W+tk.E+tk.N+tk.S)
        # logoLabel = tk.Label(self, image=self.logoImg).grid(row=0,column=0,sticky=tk.W+tk.E+tk.N+tk.S)
    #     logoLabel.grid(row=0,column=0,sticky=tk.NW)

        logo = logoCreate(self)
        logo.grid(row=0,column=0,sticky=tk.NW)

    #     logoImg = tk.PhotoImage(file='/home/users/jtibau/Desarrollo/Palmeras/CierreVentas/img/LasPalmerasLogotipo.png', height=100, width=174)
    # # logoLabel = tk.Label(rootWindow, image=logo, text="Las Palmeras Logo", bg=rootWindow.defaultColor, font=('Helvetica', 14), compound='right')
    #     logoLabel = tk.Label(self, image=logoImg, bg=defaultColor)
    #     # logoLabel.grid(row=0,column=0,sticky=tk.W+tk.E+tk.N+tk.S)
    #     logoLabel.grid(row=0,column=0,sticky=tk.NW)

        # prueba00 = tk.Label(text="logo", bg='red').grid(row=0,column=0,sticky=tk.W+tk.E+tk.N+tk.S)
        prueba01 = tk.Label(text="titulo, id", bg='blue').grid(row=0,column=1,sticky=tk.W+tk.E+tk.N+tk.S)
        prueba10 = tk.Label(text="Command", bg='green').grid(row=1,column=0,sticky=tk.W+tk.E+tk.N+tk.S)
        prueba11 = tk.Label(text="DATA", bg='yellow').grid(row=1,column=1,sticky=tk.W+tk.E+tk.N+tk.S)


    

def main():
    rootWindow = RootWindow()
    rootWindow.mainloop()

if __name__ == '__main__':
    main()