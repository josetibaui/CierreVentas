import sqlite3
from sqlite3 import Error
import os


class dbConnect(sqlite3):

    sqlitePath = os.getcwd() + '/data/PalmerasERP.db'
    cur = None
    conn = None

    def __init__(self):
        super().__init__(self.sqlitePath)
        try:
            self.conn = sqlite3.connect(self.sqlitePath)
            self.cur = self.conn.cursor()
        except Error as e:
            print(f'No se pudo establecer la conección a la base de datos. Error ({e})')

    def cerrar(self):
        if self.cur:
            self.cur.close()
        
        if self.conn:
            self.conn.close

