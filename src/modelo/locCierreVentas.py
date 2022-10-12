from re import S
import sqlite3
import modelo.DBConnection as DBConnection
from sqlite3 import Error
from tkinter.messagebox import *
from  datetime import date
from json import dumps, loads
import ast


class CierreVentas():

    _idCierreVentas = None
    _idLocal = None
    _fecha = None
    _data = None
    _idPor = None
    # _estructuraBase = {
            # "FormasPagos" : {
                # "Efectivo" : "",
                # "FormasPagos": [] },
            # "GastosGenerales": [],
            # "PagosPersonal" : [],
            # "Depositos" : [],
            # "Ventas": {
                # "VentaTotal" : "",
                # "Anulaciones" :  "",
                # "Devoluciones" : "",
                # "Diferencia": "",
                # "Cortesias" : [] }
        # }
    _estructuraBase = {
            "PagoEfectivo" : "",
            "FormasPagos": [],
            "GastosGenerales": [],
            "PagosPersonal" : [],
            "Depositos" : [],
            "Ventas" : "",
            "Anulaciones" :  "",
            "Devoluciones" : "",
            "Diferencia": "",
            "Cortesias" : []
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

    def fechaFormat(self,formato='%Y-%m-%d'):
        return self._fecha.strftime(formato)
 
    @fecha.setter
    def fecha(self, fecha):
        self._fecha = fecha

    @property
    def data(self):
        # return loads(self._data)
        # print(self._data)
        # return dict(ast.literal_eval(loads(self._data)))
        # print(f'Get data. Tipo: {type(self._data)}\n{self._data}')
        return(self._data)
    
    @data.setter
    def data(self, data):
        # self._data = dumps(data)
        # print(f'Set data. Tipo: {type(data)}\n{data}')
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

    def __str__(self):
        return str(self.cierreVentasValues)
    

    def cierreVentasValues(self):
        return [
            self.idCierreVentas,
            self.idLocal,
            self.fechaFormat(),
            self.data,
            self.idPor
        ]

    def insert(self):
        insStr = f'INSERT INTO loc_cierreVentas (idLocal, fecha, data, idPor) VALUES(?, ?, ?, ?)'
        try:
            self.cursor.execute(insStr, [self.idLocal, self.fechaFormat(), str(self.data), self.idPor])
            self.idCierreVentas = self.cursor.lastrowid
            self.connection.connect.commit()
        except Error as err:
            showerror(title='Error en DB', message=f'No se pudo guardar el registro de datos del día.\n{str(err)}')

    def update(self):
        updStr = f'UPDATE loc_cierreVentas SET data = ?, idPor = ? WHERE idCierreVentas = ?'
        try:
            self.cursor.execute(updStr, (str(self.data), self.idPor, self.idCierreVentas))
            self.connection.connect.commit()
        except Error as err:
            showerror(title='Error en DB', message=f'No se pudo guardar los cambios en el registro de datos del día.\n{str(err)}')

    def replace(self):
        pass

    def delete(self):
        pass

    def queryById(self, idCierreVentas):
        selStr = f'SELECT * FROM loc_cierreVentas WHERE idCierreVentas = ?'
        self.cursor.execute(selStr, (idCierreVentas))
        self.cierreVentas = self.cursor.fetchone()
        if self.cierreVentas:
            self.idCierreVentas = self.cierreVentas[0]
            self.idLocal = self.cierreVentas[1]
            self.fecha = self.cierreVentas[2]
            self._data = self.cierreVentas[3]
            self.por = self.cierreVentas[4]
        else:
            self.idCierreVentas = 0
            self.idLocal = None
            self.fecha = None
            self.data = dumps(self.estructuraBase)
            self.por = None
    
    def queryByLocalFecha(self, idLocal, fecha):
        selStr = 'SELECT * FROM loc_cierreVentas WHERE idLocal = ? AND fecha = ?'
        self.cursor.execute(selStr, (idLocal, fecha.strftime('%Y-%m-%d')))
        self.cierreVentas = self.cursor.fetchone()
        if self.cierreVentas:
            # print('\nCierre Ventas[3]:')
            # print(type(self.cierreVentas[3]))
            # print(self.cierreVentas[3])

            self.idCierreVentas = self.cierreVentas[0]
            self.idLocal = idLocal
            self.fecha = fecha
            self.data = ast.literal_eval(self.cierreVentas[3])
            # self.data = self.cierreVentas[3]
            # self.data = self.cierreVentas[3]
            self.por = self.cierreVentas[4]
            
            # print('\n_data:')
            # print(type(self._data))
            # print(self._data)
            # print('\ndata:')
            # print(type(self.data))
            # print(self.data)
        else:
            self.idCierreVentas = 0
            self.idLocal = idLocal
            self.fecha = fecha
            self.data = self.estructuraBase
            self.por = None
            
            # print(type(self.estructuraBase))
            # print(self.estructuraBase)
            # print(type(self._data))
            # print(self._data)
            # print(type(self.data))
            # print(self.data)
