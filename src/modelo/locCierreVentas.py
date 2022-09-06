import modelo.DBConnection as DBConnection


class CierreVentas():

    _idCierreVentas = None
    _idLocal = None
    _fecha = None
    _data = None
    _idPor = None

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

    def cierreVentasValues(self):
        return [
            self.idLocal,
            self.fecha,
            self.data,
            self.idPor
        ]

    def insert(self):
        pass

    def update(self):
        pass

    def replace(self):
        pass

    def delete(self):
        pass

    def queryById(self, idCierreVentas):
        selStr = f'SELECT * FROM loc_cierreVentas WHERE idCierreVentas = ?'
        self.cursor.execute(selStr, (idCierreVentas))
        return self.cursor.fetchone()
    
    def queryByLocalFecha(self, idLocal, fecha):
        selStr = 'SELECT * FROM loc_cierreVentas WHERE idLocal = ? AND fecha = ?'
        self.cursor.execute(selStr, (idLocal, fecha))
        return self.cursor.fetchone()

    def crearDataStructure():
        return {
            'Ventas': {
                'VentaTotal' : 0.00,
                'Anulaciones' :  0.00,
                'Devoluciones' : 0.00,
                'Diferencia': 0.00,
                'Cortesias' : [] },
            'FormasPagos' : {
                'Efectivo' : 0.00,
                'FormasPagos': [] },
            'Egresos': [],
            'PagosPersonal' : [],
            'Depositos' : []
        }