# --- File Handling ---

print('--- .txt file ---')

# .txt file

# Para ingresar a un archivo hay que hacerlo desde el directorio padre

# Es importante tener en cuenta que al momento de hacer uso de las funciones estas no se ejecutan desde el archivo en 0, que quiere decir? que van a ejecutarse con el resto del contenido del archivo que haya quedado de las funciones que esten por encima, es decir, si una funcion arriba leyo 10 caracteres y la funcion que tenemos por debajo es la readline, esta segunda no va a comenzar a ejecutarse desde el principio del archivo, si no que se ejecutara con lo que sigue despues de los 10 caracteres que leyo la funcion anterior y asi sucesivamente

""" 
    Read Only (r)
    Read and Write (r+)
    Write Only (w)
    Write and Read (w+)
    Append Only (a)
    Append and Read (a+)
"""

import os # El módulo os es una biblioteca estándar que proporciona una interfaz para interactuar con el sistema operativo en el que se ejecuta el programa. Permite realizar operaciones relacionadas con la gestión de archivos, directorios, rutas, variables de entorno y otras funcionalidades del sistema operativo.

txt_file = open('Curso_Intermedio/my_txt_file.txt', 'r+') # Leer y escribir. Si el archivo ya existe lo abre
# print(txt_file.read()) # De esta manera leemos el archivo completo
# print(txt_file.read(10)) # De esta manera podemos leer una parte concreta, el parametro dentro de los parentesis indica el numero de indexado con el que queremos trabajar. Si queremos una parte concreta despues de haber leido todo el archivo completo, el archivo se seguira leyendo y apartir de ahi nos "arrojara" la parte en concreta, para lo cual siempre sera "nada", ya que siempre leera de primeras el archivo completo y lo consecuente es nada, ya no hay mas en el archivo, por lo tanto siempre sera espacio en blanco. Esto puede ser que no aplique si escribimos algo mas en el archivo pero desde aqui, usando codigo o la funcion write...

# print(txt_file.readline())
# print(txt_file.readline())

# print(txt_file.readlines())

# Ambos for actuan igual. Cada linea del texto es un elemento. No importa si se aplica la funcion readlines o no, por defecto el texto se divide por cada una de las lineas que lo componen y esto lo toma como un elemento. QUe bien la diferencia puede estar en que la funcion readlines nos crea una lista de cada una de las lineas y apartir de cada elemento que conforma la lista (que son cada una de las lineas del texto), nos las imprime por separado y cada una en cada paso del for

for element in txt_file:
    print(element)
    
for element in txt_file.readlines():
    print(element)
    
# txt_file.write('En estos momentos estoy tomando un curso de Python') -> Si esto lo hubieramos dejado asi como estaba, esto se hubiera escrito en el archivo de forma corrida en la ultima linea de este, sin espacios, saltos de linea ni nada de nada. Hubiera quedado de esta manera... "Me dedico a la programacionEn estos momentos estoy tomando un curso de Python". Así que vamos a ponerlo de tal manera que quede con su repectivo orden

# Tener cuidado con la función write, ya que lo que le añade al archivo es permanente, no importa si comentamos el codigo, lo que ya escribio ya ahi se queda y si no lo comentamos cada vez que se ejecute el programa seguira añadiendo lo que se ejecuta en el write...

# txt_file.write('. En estos momentos estoy tomando un curso de Python')
# txt_file.write('\nQuiero especializarme en Python, JavaScript y C++')

print('')
print('----- Creación de un archivo desde 0 -----')
print('')


# CREACION DE UN ARCHIVO DESDE CERO

text_file_2 = open('Curso_Intermedio/my_txt_file_2.txt', 'w+') # Si el archivo no existe, lo crea. Para esto es necesario pasarle el parametro de escritura (w+)
text_file_2.write('Motos deportivas en mente.\n- Honda CBR600 RR\n- Yamaha R6\n- Kawasaki Ninja 650R') # Escribe información en el archivo

text_file_2.write('\nAnalizando la mejor de las opciones...')

text_file_2 = open('Curso_Intermedio/my_txt_file_2.txt', 'r+') # Abre el archivo en formato lectura. Si no hacemos este paso no se imprime en consola
for element in text_file_2.readlines():
    print(element)

text_file_2.close() # Cerramos el archivo

with open('Curso_Intermedio/my_txt_file_2.txt', 'a') as text_file_extend:
    text_file_extend.write('\nOtra opcion mas al listado es\n- Honda CBR 900 RR Fireblade')
    
text_file_2 = open('Curso_Intermedio/my_txt_file_2.txt', 'r+')
text_file_2.read()
# for element in text_file_2.readlines():
#     print(element)

""" os.remove('Curso_Intermedio/my_txt_file_2.txt') # Eliminanos el archivo """

print('')
print('--- .json file ---')
print('')

# .json file

import json

json_file = open('Curso_Intermedio/my_json_file.json', 'w+')

json_test = {
    'name':'Eliab',
    'lastname':'Hernandez',
    'age':33,
    'occupation':'Programmer',
    'languages':['Python', 'C++', 'JavaScript']
}

json.dump(json_test, json_file, indent=2)

json_file.close()

json_file = open('Curso_Intermedio/my_json_file.json', 'r')

print(json_file.read())

json_dict = json.load(open('Curso_Intermedio/my_json_file.json'))
print(json_dict)
print(type(json_dict))
print(json_dict['languages'])
print(json_dict['name'])
print(json_dict['occupation'])
json_dict['occupation'] = 'Enginner Software'
print(json_dict['occupation'])

print('')
print('--- .csv file ---')
print('')

# .csv file

import csv

csv_file = open('Curso_Intermedio/my_csv_file.csv', 'w+')

csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Marca', 'Modelo', 'Año', 'Cilindrada'])
csv_writer.writerow(['Kawasaki', 'H2R', 2022, '1200cc'])
csv_writer.writerow(['Ducati', 'Pannigale', 2021, '1200cc'])
csv_writer.writerow(['MV-Agusta', '', 2019, ''])

csv_file.close()

csv_file = open('Curso_Intermedio/my_csv_file.csv', 'r')
print(csv_file.read())
csv_file = open('Curso_Intermedio/my_csv_file.csv', 'r')
print(csv_file.readlines())

print('')
print('--- .xml file ---')
print('')

# .xml file

import xml

xml_file = open('Curso_Intermedio/my_xml_file.xml', 'w+', encoding='utf-8')
xml_file.write('<title>Probando el manejo de archivos XML</title>')
xml_file = open('Curso_Intermedio/my_xml_file.xml', 'r')
print(xml_file.read())

# .xlsx file -> Este debe de instalarse para poder ocupar el modulo