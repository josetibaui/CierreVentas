import hashlib
import platform
import datetime
from string import hexdigits

codLocal = -1
while codLocal < 0: 
    try:
        codLocal  = int(input('Ingrese el número del local en el que va a estar esta máquina: '))
        if codLocal < 0:
            raise ValueError
    except ValueError as e:
        print('Por favor ingrese un número positivo')
        codLocal = -1

cadena = f'{hex(codLocal)};{platform.system()};{platform.processor()};{datetime.datetime.now()}'
print(cadena)
coded = cadena.encode('utf-8')
cryp = hashlib.md5(cadena.encode('utf-8')).hexdigest()
print(coded)
print(cryp)
print(hashlib.sha512(hex(codLocal).encode('utf-8')).hexdigest())