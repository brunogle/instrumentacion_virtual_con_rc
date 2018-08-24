# -*- coding: utf-8 -*-
"""
@author: Ramiro
"""

# Traemos la libreria VISA
import pyvisa as visa

# Agreamos el path de las librerias
import sys
sys.path.insert(0, 'Libreria')
# Traemos la clase base que implmenta las funciones de VISA
from instrument import Instrument




# Pedimos la lista de instrumentos
rm=visa.ResourceManager('@py')
print(rm.list_resources())

# Abrimos un instrumento
INTRUMENT_INDEX = 0
instrument_handler=rm.open_resource(rm.list_resources()[INTRUMENT_INDEX])

# Implementamos la clase instrumento base
instrumento = Instrument(instrument_handler)

# Imprimimos el ID el instrumento
print("Esta conectado un: ")
instrumento.print_ID()


