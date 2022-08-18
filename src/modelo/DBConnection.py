import sqlite3
import os

class Singleton:

    def __init__(self, cls):
        self._cls = cls

    def Instance(self):
        try:
            return self._instance
        except AttributeError:
            self._instance = self._cls()
            return self._instance

    def __call__(self):
        raise TypeError('Esta clase (singleton) se instancia con el método Instace()')

    def __instancecheck__(self, inst) -> bool:
        return isinstance(inst, self._cls)


@Singleton
class DBConnection(object):

    sqlitePath = os.getcwd() + '/data/PalmerasERP.db'
    def __init__(self):
        self.connect = sqlite3.connect(self.sqlitePath)
    
    def __str__(self):
        return 'Database connection object'

    def close(self):
        self.connect.close()

