import modelo.DBConnection as DBConnection

class Personas():

    _idPersona = None
    _nombres = None
    _apellidos = None
    _tipoIdentificacion = None
    _identificacion = None
    _codigoNomina = None
    _email = None
    _login = None
    _password = None
    _estado = None

    def __init__(self):
        self.connection = DBConnection.DBConnection.Instance()
        self.cursor= self.connection.connect.cursor()

    
    @property
    def idPersona(self):
        return self._idPersona

    @idPersona.setter
    def idPersona(self, idPersona):
        self._id = idPersona

    @property
    def nombres(self):
        return self._nombres

    @nombres.setter
    def nombres(self, nombres):
        self._nombres = nombres

    @property
    def apellidos(self):
        return self._apellidos

    @apellidos.setter
    def apellidos(self, apellidos):
        self._apellidos = apellidos

    @property
    def tipoIdentificacion(self):
        return self._tipoIdentificacion

    @tipoIdentificacion.setter
    def tipoIdentificacion(self, tipoIdentificacion):
        self._tipoIdentificacion = tipoIdentificacion

    @property
    def identificacion(self):
        return self._identificacion

    @identificacion.setter
    def identificacion(self, identificacion):
        self._identificacion = identificacion

    @property
    def codigoNomina(self):
        return self._codigoNomina

    @codigoNomina.setter
    def codigoNomina(self, codigoNomina):
        self._codigoNomina = codigoNomina

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, email):
        self._email = email

    @property
    def login(self):
        return self._login

    @login.setter
    def login(self, login):
        self._login = login

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, password):
        self._password = password

    @property
    def estado(self):
        return self._estado

    @estado.setter
    def estado(self, estado):
        self._estado = estado

    def personaValues(self):
        return [
            self._nombres,
            self._apellidos,
            self._tipoIdentificacion,
            self._identificacion,
            self._codigoNomina,
            self._email,
            self._login,
            self._password,
            self._estado
        ]

    def insert(self):
        insStr = '''INSERT INTO ig_personas (nombres,
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
        self.cursor.execute(insStr, tuple(self.personaValues()))
        self.connection.commit()
        self._idPersona = self.cursor.lastrowid()

    def update(self):
        updStr = '''
                UPDATE ig_personas
                SET (nombres = ?,
                    apellidos = ?,
                    tipoIdentificacion = ?,
                    identificacion = ?,
                    codigoNomina = ?,
                    email = ?,
                    login = ?,
                    password = ?,
                    estado = ?)
                WHERE idPersona = ?
                '''
        self.cursor.execute(updStr, tuple(self.personaValues().append(self._idPersona)))
        self.connection.commit()
    
    def delete(self):
        delStr = 'DELETE FOR ig_personas WHERE idPersona = ?'
        self.cursor.execute(delStr, (self._idPersona,))
        self.connection.commit()

    

    def replace(self, persona):
        if self.queryById(persona._idPersona):
            self.update()
        else:
            self.insert()

    def queryById(self, idPersona):
        selStr = 'SELECT * FROM ig_personas WHERE idPersona = ?'
        self.cursor.execute(selStr, (idPersona,))
        return self.cursor.fetchone()

    def queryAll(self, estado=1):
        if estado == 1:
            whereStr=f' WHERE estado = 1'
        else:
            whereStr=''

        orderStr = 'ORDER BY apellidos, nombres'
        selStr = f'SELECT * FROM ig_personas {whereStr} {orderStr}'
        self.cursor.execute(selStr)
        return self.cursor.fetchall()

    def queryLikeNombre(self, nombre=None, estado=1):
        if nombre == None:
            return self.queryAll(estado)
        else:
            whereStr = 'WHERE (nombres LIKE ? OR apellidos LIKE ?)'

        if estado == 1:
            whereStr = whereStr + ' AND estado = 1'

        likeNombre = f'%{nombre}%'
        orderStr = 'ORDER BY apellidos, nombres'
        selStr = f'SELECT * FROM ig_personas {whereStr} {orderStr}'
        self.cursor.execute(selStr, (likeNombre, likeNombre))
        return self.cursor.fetchall()

    def queryOneByIdentificacion(self, identificacion, estado=1):
        if identificacion == None:
            return None

        whereStr = 'WHERE identificacion = ?'

        if estado == 1:
            whereStr=whereStr + ' AND estado = 1'

        selStr = f'SELECT * FROM ig_personas {whereStr}'
        self.cursor.execute(selStr, (identificacion,))
        return self.cursor.fetchone()


    def checkAuth(self, usuario, contrasena, idLocal):
        selStr = '''select pe.* 
                from ig_perfiles_personas_locales as ppl,
                ig_perfiles as pf,
                ig_personas as pe
                where pf.idPerfil = ppl.idPerfil
                and pe.idPersona = ppl.idPersona 
                and pf.perfil  in ("Cajero", "Jefe de Local", "Supervisor")
                and pe.estado = 1
                and ppl.estado = 1
                and pf.estado = 1
                and pe.login = ?
                and pe.password = ?
                and ppl.idLocal = ?
                '''
        # print(f'{selStr}, {usuassrio}, {contrasena}, {idLocal}')
        self.cursor.execute(selStr, (usuario, contrasena, idLocal))
        return self.cursor.fetchone()


    def queryOneByLogin(self, login, estado=1):
        if login == None:
            return None

        whereStr = 'WHERE login = ?'
        
        if estado == 1:
            whereStr=whereStr + ' AND estado = 1'
        
        selStr = f'SELECT * FROM ig_personas {whereStr}'
        self.cursor.execute(selStr, (login,))
        return self.cursor.fetchone()

    def queryByCodLocal(self, codLocal, estado=1):
        if codLocal == None:
            return None

        selStr = 'SELECT pe.* FROM ig_personas AS pe, ig_personas_locales AS pl, ig_locales AS loc'
        whereStr = f'WHERE pl.idPersona = pe.idpersona AND pl.idLocal = loc.idLocal AND loc.codLocal = ?'
        if estado == 1:
            whereStr=whereStr + f' AND pe.estado = 1 AND pl.estado = 1 and loc.estado = 1'
        orderStr = 'ORDER BY apellidos, nombres'

        selStr = f'{selStr} {whereStr} {orderStr}'
        self.cursor.execute(selStr, (codLocal,))
        return self.cursor.fetchall()

    def queryByIdLocal(self, idLocal, estado=1):
        if idLocal == None:
            return None

        selStr = 'SELECT pe.* FROM ig_personas AS pe, ig_personas_locales AS pl, ig_locales AS loc'
        whereStr = f'WHERE pl.idPersona = pe.idpersona AND pl.idLocal = loc.idLocal AND loc.idLocal = ?'
        if estado == 1:
            whereStr=whereStr + f' AND pe.estado = 1 AND pl.estado = 1 and loc.estado = 1'
        orderStr = 'ORDER BY apellidos, nombres'

        selStr = f'{selStr} {whereStr} {orderStr}'
        self.cursor.execute(selStr, (idLocal,))
        return self.cursor.fetchall()


#  No lo he probado
#     def insertManyPersonas(self, datos):
#         if self.conn:
#             sqlStr = '''INSERT INTO ig_locales (nombres,
#                     apellidos,
#                     tipoIdentificacion,
#                     identificacion,
#                     codigoNomina,
#                     email,
#                     login,
#                     password,
#                     estado)
#             VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
#             '''
#             self.conn.cur.executemany(sqlStr, datos)
    

if __name__ == '__main__':
    per = Personas()
    todos = per.queryAll(estado=1)
    print(f'Hay {len(todos)} rgistros')
    print(todos)
    print('----------------------------')
    varios = per.queryLikeNombre(nombre='ramos', estado=0)
    print(varios)
    print('-------------------------------')
    unoci =per.queryOneByIdentificacion('1205651928')
    print(unoci)
    print('-------------------------------')
    login = per.queryOneByLogin(login='256')
    print(login)
    print('-------------------------------')
    listaLocal = per.queryBylocal(codLocal=11,estado=0)
    print(listaLocal)
    print('-------------------------------')
    id=per.queryById(idPersona=72)
    print(id)
    print('-------------------------------')
    auth=per.checkAuth('256', '17035', 2)
    print(auth)
    per.connection.close()
    # c1= DBConnection.DBConnection.Instance()
    # c2= DBConnection.DBConnection.Instance()

    # print("Id of c1 : {}".format(str(id(c1))))
    # print("Id of c2 : {}".format(str(id(c1))))

    # print("c1 is c2 ? " + str(c1 is c2))