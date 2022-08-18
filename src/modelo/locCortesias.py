import modelo.DBConnection as DBConnection

class Cortesias():

    _idCortesia = None
    _cortesia = None
    _cuentaContabilidad = None
    _estado = None

    def __init__(self):
        self.connection = DBConnection.DBConnection.Instance()
        self.cursor= self.connection.connect.cursor()

    @property
    def idCortesia(self):
        return self._idCortesia
    
    @idCortesia.setter
    def idCortesia(self, idCortesia):
        self._idCortesia = idCortesia

    @property
    def cortesia(self):
        return self._cortesia
    
    @cortesia.setter
    def cortesia(self, cortesia):
        self._cortesia = cortesia

    @property
    def cuentaContabilidad(self):
        return self._cuentaContabilidad
    
    @cuentaContabilidad.setter
    def cuentaContabilidad(self, cuentaContabilidad):
        self._cuentaContabilidad = cuentaContabilidad

    @property
    def estado(self):
        return self._estado
    
    @estado.setter
    def estado(self, estado):
        self._estado = estado

    def cortesiasValues(self):
        return [
          self._idCortesia,
          self._cortesia,
          self._cuentaContabilidad,
          self._estado
        ]

    def insert(self):
        pass

    def update(self):
        pass

    def delete(self):
        pass

    def replace(self):
        pass

    def queryById(self, idCortesia):
        selStr = 'SELECT * FROM loc_cortesias WHERE idCortesia = ?'
        self.cursor.execute(selStr, (idCortesia,))
        return self.cursor.fetchone()

    def queryAll(self, estado=1):
        if estado == 1:
            whereStr=' WHERE estado = 1'
        else:
            whereStr=''

        orderStr = 'ORDER BY cortesia'
        selStr = f'SELECT * FROM loc_cortesias {whereStr} {orderStr}'
        self.cursor.execute(selStr)
        return self.cursor.fetchall()

    def queryByCortesia(self, cortesia=None, estado = 1):
        if cortesia == None:
            return None

        whereStr = 'WHERE cortesia = ?'

        if estado == 1:
            whereStr = whereStr + ' AND estado = 1'

        selStr = f'SELECT * FROM loc_cortesis {whereStr}'
        self.cursor.execute(selStr, (cortesia,))
        return self.cursor.fetchone()


if __name__ == '__main__':
    cor = Cortesias()
    todos = cor.queryAll(estado=1)
    print(f'Hay {len(todos)} rgistros')
    print(todos)
    print('----------------------------')
    cort = cor.queryById(1)
    print(cort)
    print('----------------------------')
    cort = cor.queryByCortesia('Cumpleañero')
    print(cort)
    print('----------------------------')