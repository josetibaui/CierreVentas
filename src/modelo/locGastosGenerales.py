import modelo.DBConnection as DBConnection

class GastosGenerales():

    _idEgreso = None
    _egreso = None
    _cuentaContabilidad = None
    _estado = None

    def __init__(self):
        self.connection = DBConnection.DBConnection.Instance()
        self.cursor= self.connection.connect.cursor()


    @property
    def idEgreso(self):
        return self._idEgreso
    
    @idEgreso.setter
    def idEgreso(self, idEgreso):
         self._idEgreso = idEgreso 
    
    @property
    def egreso(self):
        return self._egreso
    
    @egreso.setter
    def egreso(self, egreso):
         self._egreso = egreso 
    
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

    def egresoValues(self):
        return [
            self._egreso,
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

    def queryById(self, idEgreso):
        selStr = 'SELECT * FROM loc_gastosGenerales WHERE idEgreso = ?'
        self.cursor.execute(selStr, (idEgreso,))
        return self.cursor.fetchone()

    def queryAll(self, estado = 1):
        if estado == 1:
            whereStr=f' WHERE estado = 1'
        else:
            whereStr=''

        orderStr = 'ORDER BY gastoGeneral'
        selStr = f'SELECT * FROM loc_gastosGenerales {whereStr} {orderStr}'
        self.cursor.execute(selStr)
        return self.cursor.fetchall()

    def queryByGastoGeneral(self, gastoGeneral, estado=1):
        if egreso == None:
            return None

        whereStr = 'WHERE gastoGeneral = ?'

        if estado == 1:
            whereStr=whereStr + ' AND estado = 1'

        selStr = f'SELECT * FROM loc_gastosGenerales {whereStr}'
        self.cursor.execute(selStr, (egreso,))
        return self.cursor.fetchone()

    def queryLikeCuentaContabilidad(self, cuentaContabilidad=None, estado=1):
        if cuentaContabilidad == None:
            return self.queryAll(estado)
        else:
            whereStr = 'WHERE (cuentaContabilidad LIKE ?)'

        if estado == 1:
            whereStr = whereStr + f' AND estado = {estado}'

        cuenta = f'%{cuentaContabilidad}%'
        orderStr = 'ORDER BY gastoGeneral'
        selStr = f'SELECT * FROM loc_gastosGenerales {whereStr} {orderStr}'
        self.cursor.execute(selStr, (cuenta,))
        return self.cursor.fetchall()


if __name__== '__main__':
    gasto = GastosGenerales()

    uno = gasto.queryById(9)
    print(uno)
    print('---------------------------')

    gastos = gasto.queryByGastoGeneral('Transporte')
    print(gastos)
    print('---------------------------')

    todos =gasto.queryAll()
    print(todos)
    print('---------------------------')
    
    contab = gasto.queryLikeCuentaContabilidad('52')
    print(contab)
    print('---------------------------')

    gasto.connection.close()