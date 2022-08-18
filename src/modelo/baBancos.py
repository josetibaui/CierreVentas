import DBConnection

class Bancos():

    _idBanco = None
    _banco = None
    _cuentaContabilidad = None
    _estado = None

    def __init__(self):
        self.connection = DBConnection.DBConnection.Instance()
        self.cursor= self.connection.connect.cursor()

    def bancosValues(self):
        return [
            _banco,
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

    def queryById(self, idBanco):
        selStr = f'SELECT * FROM ba_bancos WHERE idBanco = {idBanco}'
        self.cursor.execute(selStr)
        return self.cursor.fetchone()

    def queryAll(self, estado = 1):
        if estado == 1:
            whereStr=f' WHERE estado = 1'
        else:
            whereStr=''

        orderStr = 'ORDER BY banco'
        selStr = f'SELECT * FROM ba_bancos {whereStr} {orderStr}'
        self.cursor.execute(selStr)
        return self.cursor.fetchall()

    def queryBybanco(self, banco, estado=1):
        if banco == None:
            return None

        whereStr = f'WHERE banco = "{banco}"'

        if estado == 1:
            whereStr=whereStr + ' AND estado = 1'

        selStr = f'SELECT * FROM ba_bancos {whereStr}'
        self.cursor.execute(selStr)
        return self.cursor.fetchone()

    def queryLikeCuentaContabilidad(self, cuentaContabilidad=None, estado=1):
        if cuentaContabilidad == None:
            return self.queryAll(estado)
        else:
            whereStr = f'WHERE (cuentaContabilidad LIKE "%{cuentaContabilidad}%")'

        if estado == 1:
            whereStr = whereStr + f' AND estado = {estado}'

        orderStr = 'ORDER BY tipoPago'
        selStr = f'SELECT * FROM ba_bancos {whereStr} {orderStr}'
        self.cursor.execute(selStr)
        return self.cursor.fetchall()


if __name__== '__main__':
    banco = Bancos()
    idBanco = banco.queryById(1)
    todos = banco.queryAll()
    nombre = banco.queryBybanco('Internacional')
    cuenta = banco.queryLikeCuentaContabilidad('2')

    print(idBanco)
    print('---------------------------------')
    print(todos)
    print('---------------------------------')
    print(nombre)
    print('---------------------------------')
    print(cuenta)
    print('---------------------------------')

    banco.connection.close()