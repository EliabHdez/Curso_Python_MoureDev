# --- Package Manager ---

# Gestor de paquetes para Python

# Para esto utilizamos el famoso "pip"

""" 
    pip install <nombre modulo> -> Instala el modulo
    
    pip list -> Este comando nos despliega una lista de modulos que se han instalado de pip
    
    Package         Version
    --------------- -----------
    numpy           1.26.4
    pandas          2.2.2
    python-dateutil 2.9.0.post0
    pytz            2024.1
    six             1.16.0
    tzdata          2024.1
    
    pip uninstall <nombre modulo> -> Desinstala el modulo
    
    pip show <nombre modulo> -> Nos muestra la información del modulo    
"""

import numpy # Se installo el modulo numpy mediante el paquete pip -> pip install numpy

print(numpy.version.version)

list_numpy = numpy.array([35, 24, 62, 52, 30, 33, 17])
print(type(list_numpy))
print(list_numpy * 2)

import pandas # Se installo el modulo pandas mediante el paquete pip -> pip install pandas

import requests # Se installo el modulo requests mediante el paquete pip -> pip install requests

response = requests.get('https://pokeapi.co/api/v2/pokemon?limit=151')
print(response)
print(response.status_code)
# print(response.json())

from Arithmetics_Operations import bamatop

suma = bamatop.sum_nums(1, 4)
resta = bamatop.rest_nums(11, 2)

print(suma)
print(resta)

from Greetings import persgret

first_greeting = persgret.greeting_1('Moises')

print(first_greeting)