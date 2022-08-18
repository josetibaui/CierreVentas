import modelo.DBConnection as DBConnection

class Egresos():

    _idEgreso = None
    _egreso = None
    _cuentaContabilidad = None
    _estado = None

    def __init__(self, esteLocal=None):
        self.connection = DBConnection.DBConnection.Instance()
        self.cursor= self.connection.connect.cursor()
        # self.esteLocal = esteLocal


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
        selStr = 'SELECT * FROM loc_egresos WHERE idEgreso = ?'
        self.cursor.execute(selStr, (idEgreso,))
        return self.cursor.fetchone()

    def queryAll(self, estado = 1):
        if estado == 1:
            whereStr=f' WHERE estado = 1'
        else:
            whereStr=''

        orderStr = 'ORDER BY egreso'
        selStr = f'SELECT * FROM loc_egresos {whereStr} {orderStr}'
        self.cursor.execute(selStr)
        return self.cursor.fetchall()

    def queryByEgreso(self, egreso, estado=1):
        if egreso == None:
            return None

        whereStr = 'WHERE egreso = ?'

        if estado == 1:
            whereStr=whereStr + ' AND estado = 1'

        selStr = f'SELECT * FROM loc_egresos {whereStr}'
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
        orderStr = 'ORDER BY egreso'
        selStr = f'SELECT * FROM loc_egresos {whereStr} {orderStr}'
        self.cursor.execute(selStr, (cuenta,))
        return self.cursor.fetchall()


if __name__== '__main__':
    egr = Egresos(1)

    uno = egr.queryById(9)
    print(uno)
    print('---------------------------')

    egreso = egr.queryByEgreso('Transporte')
    print(egreso)
    print('---------------------------')

    todos =egr.queryAll()
    print(todos)
    print('---------------------------')
    
    contab = egr.queryLikeCuentaContabilidad('52')
    print(contab)
    print('---------------------------')

    egr.connection.close()