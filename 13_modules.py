# --- MODULES ---

# Los módulos son archivos con codigo independientes. Para hacer uso de los módulos o de estos archivos es necesario tener acceso a ellos, es decir que los tengamos a nuestra disposición

# Los módulos son lo que se conoce en otros lenguajes como librerias, archivos que nos permiten hacer uso de su código aun estando en otro archivo, esto con la finalidad de no repetir código una y otra vez, además de que si ese código que estamos ocupando requiere algun tipo de mantenimiento no lo tengamos que realizar en 2, 3, 5, 10, 50 programas donde tengamos el mismo código, basta con hacerlo en el archivo que estamos ocupando como módulo y listo!!!

# Para hacer uso de los módulos es necesario que estos en su nombre de archivo no tengan como encabezado un número

""" 
    import 10_functions 
        Este archivo no lo podemos importar como modulo debido a que su nombre esta encabezado por un número, es decir que en el inicio del nombre tiene digitos numericos 
"""

# IMPORTAR UN MODULO COMPLETO

# Para la importación de un modulo completo lo hacemos de la sig manera: "import 'nombre modulo'"

# Cuando importamos un modulo completo, estamos importanto todo el archivo/fichero en concreto, por lo tanto estamos importanto todo el contenido del archivo y podemos hacer uso de todo este contenido, sin embargo es necesario anteponer el nombre del modulo al dato/valor/elemento que vamos a ocupar

import one_module

print(one_module.content)

one_module.add_values(5, 9, 6)
one_module.rest_values(5, 9, 6)
one_module.mult_values(5, 9, 6)
one_module.div_values(5, 9, 6)

print('*************************************************************')

# IMPORTAR UN ELEMENTO/DATO/VALOR EN CONCRETO

# Para la importación de un elemento en concreto dentro del modulo lo hacemos de la sig manera: "from 'nombre modulo' import 'nombre del elemento/dato/valor/etc'"

# Cuando importamos un elemento en concreto solo vamos a poder hacer uso de ese elemento/dato/valor en concreto, no vamos a poder hacer uso de los demás elementos que se encuentren en el modulo. A su vez cuando importamos un elemento en concreto nada mas, no es necesario anteponer el nombre del modulo al elemento, lo podemos llamar o usar de forma directa

# Podemos importar mas de un elemento/dato/valor/etc a la vez, separando por comas cada elemento/dato a importar

from one_module import content, end_module
from one_module import operations, pot_value

print(content)
print('* Potencia *')
pot_value(5, 8)
print('* Operaciones básicas *')
operations(5, 9, 6)
end_module('Fin del módulo')

print('*************************************************************')

# Python también tiene modulos propios, es decir que son de su propio sistema. Estos vienen dentro de todo el ecosistema del lenguaje y se instalan junto con Python

# Uno de esos módulos es el módulo 'math'

print("________módulo del sistema math___________")

import math

print(math.pi) # Valor de PI
print(math.pow(2, 8)) # Potencia

# Podemos tambien darle un nombre o un alias por decirlo de alguna manera a una dato en concreto que importemos

from math import pi as pi_value # Este último es el nombre o alias que le hemos dado al valor importado del módulo

print(pi_value)