import modelo.DBConnection as DBConnection

class FormasPagos():

    _idFormaPago = None
    _formaPago = None
    _cuentaContabilidad = None
    _estado = None

    def __init__(self):
        self.connection = DBConnection.DBConnection.Instance()
        self.cursor= self.connection.connect.cursor()

    
    @property
    def idFormaPago(self):
        return self._idFormaPago
    
    @idFormaPago.setter
    def idFormaPago(self, idFormaPago):
        self._idFormaPago = idFormaPago
    
    @property
    def formaPago(self):
        return self._formaPago
    
    @formaPago.setter
    def formaPago(self, formaPago):
        self._formaPago = formaPago

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

    def formasPagosValues(self):
        return [
            self._formaPago,
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

    def queryById(self, idFormaPago):
        selStr = 'SELECT * FROM loc_formasPagos WHERE idFormaPago = ?'
        self.cursor.execute(selStr, (idFormaPago,))
        return self.cursor.fetchone()

    def queryAll(self, estado=1):
        if estado == 1:
            whereStr=f' WHERE estado = 1'
        else:
            whereStr=''

        orderStr = 'ORDER BY formaPago'
        selStr = f'SELECT * FROM loc_formasPagos {whereStr} {orderStr}'
        self.cursor.execute(selStr)
        return self.cursor.fetchall()

    def queryByFormaPago(self, formaPago, estado=1):
        if formaPago == None:
            return None

        whereStr = 'WHERE formaPago = ?'

        if estado == 1:
            whereStr=whereStr + ' AND estado = 1'

        selStr = f'SELECT * FROM loc_formasPagos {whereStr}'
        self.cursor.execute(selStr, (formaPago,))
        return self.cursor.fetchone()

    def queryLikeCuentaContabilidad(self, cuentaContabilidad=None, estado=1):
        if cuentaContabilidad == None:
            return self.queryAll(estado)
        else:
            whereStr = 'WHERE (cuentaContabilidad LIKE ?)'

        if estado == 1:
            whereStr = whereStr + f' AND estado = {estado}'

        cuenta = f'%{cuentaContabilidad}%'
        orderStr = 'ORDER BY formaPago'
        selStr = f'SELECT * FROM loc_formasPagos {whereStr} {orderStr}'
        self.cursor.execute(selStr, (cuenta,))
        return self.cursor.fetchall()


if __name__ == '__main__':
    fp = FormasPagos()

    todos = fp.queryAll()
    print(todos)
    print('-'*20)

    una = fp.queryById(3)
    print(una)
    print('-'*20)

    una = fp.queryByFormaPago('Rappi')
    print(una)
    print('-'*20)

    contab = fp.queryLikeCuentaContabilidad('30')
    print(contab)
    print('-'*20)