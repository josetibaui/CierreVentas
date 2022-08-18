import tkinter as tk
from tkinter import ttk

class GastosPersonalFrame(ttk.Frame):
    def __init__(self, dataFrame):
        super().__init__(dataFrame)

        self.df = dataFrame
        
        self.grid(row=0, column=0, sticky='nsew')

        # dataFrame.gridConfigure(self)
        self.crearWidgets()

    def crearWidgets(self):
        estilo = ttk.Style(self)
        estilo.configure('TLabel', background=self.df.defaultColor)
        estilo.configure('Values.TLabel', relief='ridge')
        estilo.configure('TCombobox', background=self.df.defaultColor)
        estilo.configure('TEntry', width=10, borderwidth=1, background=self.df.defaultColor)
        labelsOptions = {'sticky': 'w', 'padx': 20, 'pady': 5}
        valuesOptions = {'sticky': 'e', 'padx': 20, 'pady': 5}
        labelsColumnsOptions = {'sticky': 'n', 'padx': 5, 'pady': 5}

        tituloLabel = ttk.Label(self, text='Detalle de Gastos de Personal', font=('Helvetica bold', 16))
        tituloLabel.grid(row=0, column=0, columnspan=4, pady=5, sticky='n')

        empleadoLabel = ttk.Label(self, text='Empleado')
        empleadoLabel.grid(row=1,column=0, **labelsColumnsOptions)

        localOrigenGastoGeneralLabel = ttk.Label(self, text='Tipo de Gastos')
        localOrigenGastoGeneralLabel.grid(row=1,column=1, **labelsColumnsOptions)

        valorGastoPersonalLabel = ttk.Label(self, text='Valor del Gasto')
        valorGastoPersonalLabel.grid(row=1,column=2, **labelsColumnsOptions)
        

        obserbacionGastoGeneralLabel = ttk.Label(self, text='Observaciones')
        obserbacionGastoGeneralLabel.grid(row=1,column=3, **labelsColumnsOptions)



#  tituloLabel = tk.Label(gastosPersonalFrame, text='Detalle de Gastos de Personal', bg=defaultColor, font=('Helvetica bold', 16))

#     empleadoLabel = tk.Label(gastosPersonalFrame, text='Empleado', bg=defaultColor)
#     tipoGastosPersonalLabel = tk.Label(gastosPersonalFrame, text='Tipo de Gasto', bg=defaultColor)
#     valorGastosPersonalLabel = tk.Label(gastosPersonalFrame, text='Valor', bg=defaultColor)
#     observacionGastosPersonalLabel = tk.Label(gastosPersonalFrame, text='Observaciones', bg=defaultColor)

#     empleadoCombo = ttk.Combobox(gastosPersonalFrame)
#     empleadoCombo['values'] = [
#                     'Avila Moreira Daisy Veronica ',
#                     'Bedoya Chiluisa Juan Fidel ',
#                     'Bone Mera Marcos Eduardo',
#                     'Bone Mera Vanesa Anabela',
#                     'Bonifaz Salazar Karlita Lucia',
#                     'Borja Diaz Jessica Tatiana',
#                     'Bravo Alcivar Leopoldina Maribel',
#                     'Burgos Bustamante Jose Luis',
#                     'Burgos Bustamante Segundo José ',
#                     'Carpio Burgos Jose Agustin',
#                     'Castro Seas Geomara Alexandra',
#                     'Cedeño Gomez Wilson Onofre',
#                     'Cedeño Zambrano Nancy Lilibeth',
#                     'Cevallos Alvarado Pedro Pablo',
#                     'Chimbolema Moposita Maria Mercedes',
#                     'Chinche Analuisa Diana Carolina ',
#                     'Chisag Chimbolema William Oswaldo ',
#                     'Coronel Toledo Eduardo Enrique',
#                     'Cortes Torres Flor Magaly',
#                     'Cuasapud Yaguapaz Blanca Rubiela ',
#                     'De Souza Mendoza Andrea Soraya',
#                     'Delgado Ramirez Manuel Estalin ',
#                     'Fajardo Peñafiel Richar Uber',
#                     'Gaibor Cerruffo Erick Sebastian',
#                     'Gordillo Cellan Victor Manuel',
#                     'Gordillo Rosero Enma del Rocio',
#                     'Gracia Velez Genesis Milady',
#                     'Gualan Correa Jacqueline Sesibel',
#                     'Gutierres Chacon Edison Fernando ',
#                     'Jaya Quezada Rocio del Carmen',
#                     'Loor Delgado Robert Rene',
#                     'Loor Saltos Marcos Gregorio',
#                     'Lopez Rubio Luis Alberto',
#                     'Machado Galet Hilda ',
#                     'Melendez Carvajal Arianne Elizabeth ',
#                     'Mendez Ortiz Katherine Estefania ',
#                     'Mendoza Fajardo Jessica Alexandra',
#                     'Mera Quiroz Blanca Dolores',
#                     'Moncerrate Guanipatin Alexi Mariano',
#                     'Monserrate Vasquez Pedro Victor',
#                     'Morales Perugachi Irene Alexandra',
#                     'Moreno Guerrero Nagelly Lisseth',
#                     'Padilla Mendez Magaly Beatriz',
#                     'Parraga Baquerizo Jaime Antonio',
#                     'Pelaes Cevallos Nancy del Rocio',
#                     'Peñarrieta Velez Carlos Alfredo',
#                     'Peñarrieta Velez Lenny del Rosario',
#                     'Peñarrieta Velez Rosa Alexandra',
#                     'Piedra Ruiz Rosa Margarita',
#                     'Pilco Parco Lorena Patricia ',
#                     'Piza Cela Vicente Orlando',
#                     'Polo Carillo Julia Aracely',
#                     'Ramos Acosta Rosmery Bellatriz',
#                     'Reyes Medina Gladys Maria',
#                     'Rivadeneira Muñoz Karina Lisbeth',
#                     'Romero Hurtado Joselyn Gabriela',
#                     'Rua Micolta Nancy Janeth',
#                     'Sanchez Peñarrieta Francisco Roberto',
#                     'Shiguango Mamallacta Jimmy Henry',
#                     'Shiguango Mamallacta Maria Margarita',
#                     'Silva Mera Jeniffer Angelica ',
#                     'Silva Mera Roxana Lilibeth',
#                     'Simba Freire Carlos Andres ',
#                     'Solá Cheme Shirley Camila',
#                     'Soto Malacatus Carmen Dolores',
#                     'Soto Malacatus Vicente Felipe',
#                     'Tandalla Guananga Diego Francisco ',
#                     'Tapia Gomez Jesus Nazareno',
#                     'Tiviano Punina Edison Mauricio ',
#                     'Troya Morales Maria Salome ',
#                     'Valdez Medina Leandro',
#                     'Vegas Maldonado Fabiola Jhojanna',
#                     'Velasco Quiñonez John Janner ',
#                     'Velez Cedeño Gissela Janeth ',
#                     'Velez Cedeño Shirley Rossibel',
#                     'Velez Ganchozo Gissela Jazmin ',
#                     'Vera Vasquez Jefferson Bernardino',
#                     'Vidal Pazmiño Edison Leonardo',
#                     'Vite Vaca Fannis',
#                     'Zambrano Loor Mercy Magdalena',
#                     'Zambrano Navarrete Gustavo Fabian'
#     ]
#     empleadoCombo['state'] = 'readonly'

#     tipoGastosPersonalCombo = ttk.Combobox(gastosPersonalFrame)
#     tipoGastosPersonalCombo['values'] = ['Préstamo', 'Anticipo']
#     tipoGastosPersonalCombo['state'] = 'readonly'

#     valorGastosPersonalEntry = tk.Entry(gastosPersonalFrame)
#     observacionGastosPersonalEntry = tk.Entry(gastosPersonalFrame)

#     columnasGastosPersonal = ('empleado', 'tipoGastosPersonal', 'valorGastosPersonal', 'observaciones')
#     gastosPersonalTree = ttk.Treeview(gastosPersonalFrame, columns=columnasGastosPersonal, show='headings')
#     gastosPersonalTree.heading('empleado', text='Empleado')
#     gastosPersonalTree.heading('tipoGastosPersonal', text='Tipo de Gasto')
#     gastosPersonalTree.heading('valorGastosPersonal', text='Valor')
#     gastosPersonalTree.heading('observaciones', text='Observaciones')

#     tituloLabel.grid(row=0, column=0, columnspan=4, sticky='WE')

#     empleadoLabel.grid(row=1, column=0, sticky='WE')
#     tipoGastosPersonalLabel.grid(row=1, column=1, sticky='WE')
#     valorGastosPersonalLabel.grid(row=1, column=2, sticky='WE')
#     observacionGastosPersonalLabel.grid(row=1, column=3, sticky='WE')

#     empleadoCombo.grid(row=2, column=0, sticky='WE')
#     tipoGastosPersonalCombo.grid(row=2, column=1, sticky='WE')
#     valorGastosPersonalEntry.grid(row=2, column=2, sticky='WE')
#     observacionGastosPersonalEntry.grid(row=2, column=3, sticky='WE')

#     gastosPersonalTree.grid(row=3, column=0, columnspan=4, sticky='nswe', pady=10)
