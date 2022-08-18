import modelo.DBConnection as DBConnection

class PagosPersonal():

    _idPagoPersonal = None
    _tipoPago = None
    _cuentaContabilidad = None
    _estado = None

    def __init__(self) -> None:
       self.connection = DBConnection.DBConnection.Instance()
       self.cursor= self.connection.connect.cursor()

    @property
    def idPagoPersonal(self):
        return self._idPagoPersonal
    
    @idPagoPersonal.setter
    def idPagoPersonal(self, idPagoPersonal):
        self._idPagoPersonal = idPagoPersonal

    @property
    def tipoPago(self):
        return self._tipoPago
    
    @tipoPago.setter
    def tipoPago(self, tipoPago):
        self._tipoPago = tipoPago

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

    def personasValues(self):
        return [
            _tipoPago,
            _cuentaContabilidad,
            _estado
        ]

    def insert(self):
        pass

    def update(self):
        pass

    def delete(self):
        pass

    def replace(self):
        pass

    def queryById(self, idPagoPersonal):
        selStr = 'SELECT * FROM loc_pagosPersonal WHERE idPagoPersonal = ?'
        self.cursor.execute(selStr, (idPagoPersonal,))
        return self.cursor.fetchone()

    def queryAll(self, estado = 1):
        if estado == 1:
            whereStr=' WHERE estado = 1'
        else:
            whereStr=''

        orderStr = 'ORDER BY tipoPago'
        selStr = f'SELECT * FROM loc_pagosPersonal {whereStr} {orderStr}'
        self.cursor.execute(selStr)
        return self.cursor.fetchall()

    def queryByTipoPago(self, tipoPago, estado=1):
        if tipoPago == None:
            return None

        whereStr = 'WHERE tipoPago = ?'

        if estado == 1:
            whereStr=whereStr + ' AND estado = 1'

        selStr = f'SELECT * FROM loc_pagosPersonal {whereStr}'
        self.cursor.execute(selStr, (tipoPago,))
        return self.cursor.fetchone()

    def queryLikeCuentaContabilidad(self, cuentaContabilidad=None, estado=1):
        if cuentaContabilidad == None:
            return self.queryAll(estado)
        else:
            whereStr = 'WHERE (cuentaContabilidad LIKE ?)'

        if estado == 1:
            whereStr = whereStr + ' AND estado = 1'

        cuenta = f'%{cuentaContabilidad}%'
        orderStr = 'ORDER BY tipoPago'
        selStr = f'SELECT * FROM loc_pagosPersonal {whereStr} {orderStr}'
        self.cursor.execute(selStr, (cuenta,))
        return self.cursor.fetchall()


if __name__ == '__main__':
    pagop = PagosPersonal()
    unoId = pagop.queryById(1)
    todos = pagop.queryAll()
    unoTipo = pagop.queryByTipoPago('Préstamo')
    contab = pagop.queryLikeCuentaContabilidad('1102')

    print(unoId)
    print('-------------------------------------')
    print(todos)
    print('-------------------------------------')
    print(unoTipo)
    print('-------------------------------------')
    print(contab)
    print('-------------------------------------')
    pagop.connection.close()