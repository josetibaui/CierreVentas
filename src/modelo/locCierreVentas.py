from json import JSONDecoder
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
        cierreVentas = self.cursor.fetchone()
        if cierreVentas:
            self.idCierreVentas = cierreVentas[0]
            self.idLocal = cierreVentas[1]
            self.fecha = cierreVentas[2]
            self.data = JSONDecoder(cierreVentas[3])
            self.por = cierreVentas[4]
        else:
            self.idCierreVentas = 0
            self.idLocal = None
            self.fecha = None
            self.data = self.crearDataStructure
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
            self.data = JSONDecoder(cierreVentas[3])
            self.por = cierreVentas[4]
        else:
            self.idCierreVentas = 0
            self.idLocal = idLocal
            self.fecha = fecha
            self.data = self.crearDataStructure
            self.por = None

    def crearDataStructure(self):
        return {
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