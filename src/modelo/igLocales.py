import modelo.DBConnection as DBConnection

class Locales():

    _idLocal = None
    _codLocal = None
    _local = None
    _alias = None
    _tipo = None
    _ciudad = None
    _direccion = None
    _referencia = None
    _codigoArea = None
    _telefono = None
    _codigoPostal = None
    _estado = None

    def __init__(self):
        self.connection = DBConnection.DBConnection.Instance()
        self.cursor= self.connection.connect.cursor()
        
    def close(self):
        self.connection.close()

    @property
    def idLocal(self):
        return self._idLocal
    
    @idLocal.setter
    def idLocal(self, idLocal):
        self._idLocal = idLocal

    @property
    def codLocal(self):
        return self._codLocal
    
    @codLocal.setter
    def codLocal(self, codLocal):
        self._codLocal = codLocal

    @property
    def local(self):
        return self._local
    
    @local.setter
    def local(self, local):
        self._local = local

    @property
    def alias(self):
        return self._alias
    
    @alias.setter
    def alias(self, alias):
        self._alias = alias

    @property
    def tipo(self):
        return self._tipo
    
    @tipo.setter
    def tipo(self, tipo):
        self._tipo = tipo

    @property
    def ciudad(self):
        return self._ciudad
    
    @ciudad.setter
    def ciudad(self, ciudad):
        self._ciudad = ciudad

    @property
    def direccion(self):
        return self._direccion
    
    @direccion.setter
    def direccion(self, direccion):
        self._direccion = direccion

    @property
    def referencia(self):
        return self._referencia
    
    @referencia.setter
    def referencia(self, referencia):
        self._referencia = referencia

    @property
    def codigoArea(self):
        return self._codigoArea
    
    @codigoArea.setter
    def codigoArea(self, codigoArea):
        self._codigoArea = codigoArea

    @property
    def telefono(self):
        return self._telefono
    
    @telefono.setter
    def telefono(self, telefono):
        self._telefono = telefono

    @property
    def codigoPostal(self):
        return self._codigoPostal
    
    @codigoPostal.setter
    def codigoPostal(self, codigoPostal):
        self._codigoPostal = codigoPostal

    @property
    def estado(self):
        return self._estado
    
    @estado.setter
    def estado(self, estado):
        self._estado = estado

    def localValues(self):
        return [
            self._codLocal,
            self._local,
            self._alias,
            self._tipo,
            self._ciudad,
            self._direccion,
            self._referencia,
            self._codigoArea,
            self._telefono,
            self._codigoPostal,
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

    def queryById(self, idLocal):
        selStr = 'SELECT * FROM ig_locales WHERE idlocal = ?'
        self.cursor.execute(selStr, (idLocal,))
        return self.cursor.fetchone()

    def queryAll(self, estado=1):
        if estado == 1:
            whereStr=' WHERE estado = 1'
        else:
            whereStr=''

        orderStr = 'ORDER BY codLocal'
        selStr = f'SELECT * FROM ig_locales {whereStr} {orderStr}'
        self.cursor.execute(selStr)
        return self.cursor.fetchall()

    def queryBycodLocal(self, codLocal=None, estado=1):
        if codLocal == None:
            return None

        whereStr = 'WHERE codLocal = ?'

        if estado == 1:
            whereStr=whereStr + ' AND estado = 1'

        selStr = f'SELECT * FROM ig_locales {whereStr}'
        self.cursor.execute(selStr, (codLocal, ))
        return self.cursor.fetchone()

    

#  No lo he probado
#     def insertMany(self,datos):
#         if self.conn:
#             sqlStr = '''INSERT  INTO ig_locales (
#                             codLocal,
#                             local,
#                             alias,
#                             tipo,
#                             ciudad,
#                             direccion,
#                             referencia,
#                             codigoArea,
#                             telefono,
#                             codigoPostal,
#                             estado)
#                         VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)'''
#             print(datos)
#             print(sqlStr)
#             try:
#                 self.conn.cur.executemany(sqlStr, datos)
#                 self.conn.commit()
#             except Error as e:
                # print(e)




if __name__== '__main__':
    loc= Locales()

    todos = loc.queryAll(estado=1)
    print(todos)
    print('--------------------------------------')
    localxcod = loc.queryBycodLocal(codLocal=0)
    print(localxcod)
    print('--------------------------------------')
    localxId = loc.queryById(10)
    print(localxId)
    print('--------------------------------------')
    loc.connection.close()