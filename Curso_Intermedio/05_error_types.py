# --- Error Types ---

print('--- SintaxError ---')

# * SyntaxError *

# print 'Hola Moisés, buen día' # -> SyntaxError. (Descomentar para ver el error)
print('Hola Moisés, buen día')

print('--- NameError ---')

# * NameError *

# print(alias) # -> NameError. Quiere decir que no hay nada con el nombre 'alias', este nombre no esta definido. Variable 'alias' no definida. (Descomentar para ver el error)
alias = 'Predator Rider'
print(alias)

print('--- IndexError ---')

# * IndexError *

list_one = ['Python', 'C', 'C++', 'JavaScript', 'Java']
print(list_one[0])
print(list_one[1])
print(list_one[2])
print(list_one[3])
print(list_one[4])
# print(list_one[5]) # -> IndexError. Index en la lista fuera de rango, es decir no existe el numero de indice ya que los elementos no son los suficientes para llegar a ese numero de índice. (Descomentar para ver el error)
print(list_one[-3])
print(list_one[-1])

print('--- ModuleNotFoundError ---')

# * ModuleNotFoundError *

# import maths # -> ModuleNotFoundError. Quiere decir que no ha encontrado el modulo en cuestión. No lo encunetra porque no existe ya que esta mal el nombre y no hay un modulo que se llame asi. (Descomentar para ver el error)
import math
print('Módulo importado exitosamente')

print('--- AttributeError ---')

# * AttributeError *

# print(math.PI) # -> AttributeError. Quiere decir que no el atributo al que nos referimos no existe, no hay! En este caso indica que el modulo math no tiene ningun atributo llamado PI. (Descomentar para ver el error)
print(math.pi)

print('--- KeyError ---')

# * KeyError *

dict_one = {'Name':'Moises', 'Lastname':'Hernández', 1:'Motos'}

# print(dict_one['1']) # -> KeyError. Quiere decir que el valor asignado a una llave/key no es correcto. Esa llave/key/clave no existe. En el diccionario tenemos la key 1 no '1'. Es decir la key es un número representado como entero, no un número representado como string. (Descomentar para ver el error)
print(dict_one[1])
print(dict_one['Name'])
# print(dict_one['Lasname']) # -> De igual manera aqui tenemos un error y este es que lo hemos escrito mal, no necesariamente estamos confundiendo el tipo de dato, si no que tuvimos un error de dedo y gracias a este la key en el diccionario como tal no va a existir y de igual manera nos va a saltar el KeyError. (Descomentar para ver el error)
print(dict_one['Lastname'])

print('--- TypeError ---')

# * TypeError *

list_one = ['Python', 'C', 'C++', 'JavaScript', 'Java']

# print(list_one['C++']) # -> TypeError. Quiere decir que el tipo de dato que estamos pasando o solicitando no coincido con el tipo de dato que se tiene o con el que se puede o quiere trabajar. En este caso en particular con una lista tenemos que acceder mediante un indice y este es por medio de numeros enteros para conseguir trozos o rebanadas que vienen siendo los elementos de la lista. (Descomentar para ver el error)
# print(list_one['0']) -> Lo mismo...
print(list_one[0])
print(list_one[2])

my_int = '10'
# print(my_int + 5) -> TypeError: can only concatenate str (not "int") to str

print('--- ImportError ---')

# * ImportError *

# from math import PI # -> ImportError. Quiere decir que no estamos importando el bloque, una variable o lo que fuera correctamente. En este caso podemos ver que dice que no puede importar PI desde math y eso es porque PI no existe, no asi como tal, es pi. (Descomentar para ver el error)
from math import pi
print('pi importado correctamente')

print('--- ValueError ---')

# * ValueError *

# my_int = int('10 Años') # -> ValueError. Quiere decir que hay un error con un valor, un dato, un elemento. Queremos hacer algo que no es posible, como en este caso querer pasar a entero un cadena de texto que contien carácteres alfabeticos. (Descomentar para ver el error)
# print(my_int) # -> Aqui vemos el error, pero este se genera desde la linea de codigo de arriba
my_int = int('10')
print(type(my_int), 'Sin errores, ya que el valor a pasar a entero es numerico sin mas')

print('--- ZeroDivisionError ---')

# * ZeroDivisionError *

# print(4/0) # -> ZeroDivisionError. Quiere decir que no se puede dividir entre 0 basicamente
print(4/2)