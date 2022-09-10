from json import JSONDecoder, JSONEncoder
import json
import modelo.DBConnection as DBConnection
from tkinter.messagebox import *


class CierreVentas():

    _idCierreVentas = None
    _idLocal = None
    _fecha = None
    _data = None
    _idPor = None
    _estructuraBase = {
            'Ventas': {
                'VentaTotal' : "",
                'Anulaciones' :  "",
                'Devoluciones' : "",
                'Diferencia': "",
                'Cortesias' : [] },
            'FormasPagos' : {
                'Efectivo' : "",
                'FormasPagos': [] },
            'GastosGenerales': [],
            'PagosPersonal' : [],
            'Depositos' : []
        }

    def __init__(self):
        self.connection = DBConnection.DBConnection.Instance()
        self.cursor= self.connection.connect.cursor()

    @property
    def idCierreVentas(self):
        return self._idCierreVentas

    @idCierreVentas.setter
    def idCierreVentas(self, idCierreVentas):
        self._idCierreVentas = idCierreVentas

    @property
    def idLocal(self):
        return self._idLocal

    @idLocal.setter
    def idLocal(self, idLocal):
        self._idLocal = idLocal

    @property
    def fecha(self):
        return self._fecha
 
    @fecha.setter
    def fecha(self, fecha):
        self._fecha = fecha

    @property
    def data(self):
        return self._data
    
    @data.setter
    def data(self, data):
        self._data = data

    @property
    def idPor(self):
        return self._idPor
    
    @idPor.setter
    def idPor(self, idPor):
        self._idPor = idPor

    @property
    def estructuraBase(self):
        return self._estructuraBase

    def cierreVentasValues(self):
        return [
            self.idCierreVentas,
            self.idLocal,
            self.fecha,
            self.data,
            self.idPor
        ]

    def insert(self):
        insStr = f'INSERT INTO loc_cierreVentas VALUES(?, ?, ?, ?, ?)'
        try:
            self.cursor.execute(insStr, self.cierreVentasValues)
            self.idCierreVentas()
        except:
            showerror(title='Error en DB', message='No se pudo guardar el registro de datos del día.')

    def update(self):
        updStr = f'UPDATE loc_cierreVentas SET data = ?, idPor = ? WHERE idCierreVentas = ?'
        try:
            self.cursor.execute(updStr, (self.data(), self.idPor(), self.idCierreVentas()))
        except:
            showerror(title='Error en DB', message='No se pudo guardar los cambios en el registro de datos del día.')

    def replace(self):
        pass

    def delete(self):
        pass

    def queryById(self, idCierreVentas):
        selStr = f'SELECT * FROM loc_cierreVentas WHERE idCierreVentas = ?'
        self.cursor.execute(selStr, (idCierreVentas))
        cierreVentas = self.cursor.fetchone()
        if cierreVentas:
            self.idCierreVentas = cierreVentas[0]
            self.idLocal = cierreVentas[1]
            self.fecha = cierreVentas[2]
            self.data = cierreVentas[3]
            self.por = cierreVentas[4]
        else:
            self.idCierreVentas = 0
            self.idLocal = None
            self.fecha = None
            self.data = self.estructuraBase
            self.por = None
    
    def queryByLocalFecha(self, idLocal, fecha):
        selStr = 'SELECT * FROM loc_cierreVentas WHERE idLocal = ? AND fecha = ?'
        self.cursor.execute(selStr, (idLocal, fecha))
        cierreVentas = self.cursor.fetchone()
        # print(f'Datos leidos: {cierreVentas}')
        if cierreVentas:
            self.idCierreVentas = cierreVentas[0]
            self.idLocal = idLocal
            self.fecha = fecha
            self.data = cierreVentas[3]
            self.por = cierreVentas[4]
        else:
            self.idCierreVentas = 0
            self.idLocal = idLocal
            self.fecha = fecha
            self.data = self.estructuraBase
            self.por = None