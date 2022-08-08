from modelo import connectSqlite
from sqlite3 import Error

# class IgLocales(connectSqlite):
#     def __init__(self):
#         super().__init__()

#     def insertMany(datos):
#         pass


class IgLocales():

    conn = None

    def __init__(self):
        self.conn = connectSqlite.dbConnect()

    def insertMany(self,datos):
        if self.conn:
            sqlStr = '''INSERT  INTO ig_locales (
                            codLocal,
                            local,
                            alias,
                            tipo,
                            ciudad,
                            direccion,
                            referencia,
                            codigoArea,
                            telefono,
                            codigoPostal,
                            estado)
                        VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)'''
            print(datos)
            print(sqlStr)
            try:
                self.conn.cur.executemany(sqlStr, datos)
                self.conn.commit()
            except Error as e:
                print(e)

    def insertManyPersonas(self, datos):
        if self.conn:
            sqlStr = '''INSERT INTO ig_locales (nombres,
                        apellidos,
                        tipoIdentificacion,
                        identificacion,
                        codigoNomina,
                        email,
                        login,
                        password,
                        estado)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
            '''
            self.conn.cur.executemany(sqlStr, datos)
    