# --- Regular Expressions ---

# Las expresiones regualares nos sirven para confirmar si una cadena de texto tiene o no ciertos datos, elementos etc

# Para hacer uso de las expresiones regulares en Python es necesario importar el modulo "re"

import re

print('----- MATCH -----')

# MATCH

# El match busca una coincidencia pero desde el inicio de la cadena, si no encuentra esta coincidencia (ya sea desde un numero, una letra, una palabra o frase) al inicio nos arrojara como resultado None

prueba = 'Esta es la lección 7. Expresiones regulares'

prueba_2 = 'Esta no es la lección 6.'

comprobacion = re.match('Esta es la lección 7', prueba, re.I) # la "I" es por "IGNORECASE". Esto quiere decir que ignora las mayusculas
print(comprobacion)

start, end = comprobacion.span()
print(prueba[start:end])

comprobacion = print(re.match('Esta es la lección', prueba_2))

print('----- Comprobacion de coincidencias -----')

# Comprobando si hay coincidencias con las cadenas de texto

print('----- No hay coincidencias -----')

# No hay coincidencias
if comprobacion == None: # Esta linea comprueba que no coincide la busqueda que estamos haciendo de una cadena de texto con la cadena de texto que contiene la variable (L-19)
    print(comprobacion)
    print('No hay coincidencias en la cadena de texto')
    
comprobacion = re.match('Esta es la lección 7', prueba)
    
print('----- Si hay coincidencias -----')

# if not(comprobacion == None): Esta es otra forma de hacer la comprobación, solo que me confundo un poco con el not, pero basicamente en este caso es que comprobacion sea diferente a None

# Si hay coincidencias
if comprobacion != None:
    print('Se encontaron coincidencias con la cadena de texto')
    print(comprobacion)
    start, end = comprobacion.span()
    print(prueba[start:end])
    
print(re.match('Expresiones regulares', prueba))

comprobacion = re.match('Esta no es la lección', prueba_2)
# if comprobacion is not None: Esta es otra forma de comprobacion (en este caso para el None)
if comprobacion != None:
    print(comprobacion)
    start, final = comprobacion.span()
    print(prueba_2[start:final])
    
print('')
print('----- SEARCH -----')
    
# SEARCH

# El search nos permite buscar en toda la cadena de texto y si hay alguna coincidencia nos arrojara un resultado, de lo contrario sera un None

buscar = re.search('leCción', prueba, re.I) # Estamos ignorando la "C" mayuscula
print(buscar) # Nos da la coincidencia aunque haya una mayuscula

correo = 'moises@gmail.com'

if correo:
    comprobacion = re.search('@gmail.com', correo)
    if comprobacion != None:
        start, final = comprobacion.span()
        print(start, final)
        print(correo[start:final])
        print('El correo electronico ingresado es válido')
        print(correo)
    else:
        print('Correo NO válido')

print('')
print('----- FINDALL -----')
        
# FINDALL

# El findall encuentra todas las coincidencias existentes y las guarda en una lista

prueba = 'Esta es la lección 7. Lección llamada: Expresiones regulares'

encuentra_todo = re.findall('leCción', prueba, re.I)
print(encuentra_todo)

print('')
print('----- SPLIT -----')

# SPLIT

# El metodo split() nos solicita un patter (patron) y un string (cadena de texto). Y lo que hace es que busca el patron y apartir de este si es que lo hay separa la cadena cada vez que encuentra este patron y esto lo guarda en una lista con cada división que hizo al encontrar este patron

separacion = re.split(':', prueba)
print(separacion)

prueba = 'Esta es la lección 7 -> Expresiones regulares -> Del curso intermedio de Python -> Por Brais Moure'

separacion = re.split('->', prueba)
print(separacion)

# Cabe mencionar que si le pasamos punto (.) como patron tiene un resultado un tanto raro, este no lo identifica como tal!!!

print('')
print('----- SUB -----')

# SUB

# El método sub() nos sirve para sustituir una palabra, frase o cadena dentro de la cadena de texto

prueba = 'Esta es la lección numero 7. llamada Lección: Expresiones regulares (l-7).'#-9'

sustitucion = re.sub('numero', '#', prueba)
print(sustitucion)

sustitucion_2 = re.sub('numero 7', '#7', prueba)
print(sustitucion_2)

sustitucion_3 = re.sub('Expresiones regulares', 'RegEx -> Curso Intermedio de Python', prueba)
print(sustitucion_3)

# sustitucion_4 = re.sub('lección|Lección', 'LECCIÓN', prueba) # Para cambiar o sustituir dos o mas palabras las ponemos dentro de las mismas comillas, pero separadas por la barra recta

# O bien si sabemos en que varian exactamente las palabras a sustituir podemos hacerlo de una manera mas simplificada
sustitucion_4 = re.sub('[l|L]ección', 'LECCIÓN', prueba)
print(sustitucion_4)

print('----- PATTERNS REGEX (PATRONES PERSONALIZADOS) -----')

# PATTERNS REGEX (CUSTOM)

# Vamos a crear nuestros propios patrones y nuestras propias expresiones regulares

pattern_1 = r'[lL]ección' # Que contenga 'l' o 'L'
print(re.findall(pattern_1, prueba))

pattern_1 = r'[l|L]ección' # Que contenga 'l' o 'L'
print(re.findall(pattern_1, prueba))

pattern_1 = r'[l|L]ección|Expresiones' # Aqui en la palabra Expresiones la estamos condicionando o buscando con la primera letra en mayúscula si o si

print(re.findall(pattern_1, prueba))

pattern_1 = r'[lL]ección|expresiones' # Aqui en la palabra expresiones la estamos condicionado o buscando exclusivamente con minusculas, es por eso que no nos da ningun resultado
print(re.findall(pattern_1, prueba))

pattern_1 = r'[a-z]' # Estamos limitando a caracteres alfabeticos de la "a" a la "z" solo en minúsculas
print(re.findall(pattern_1, prueba))
print(re.match(pattern_1, prueba))

pattern_1 = r'[A-Z]' # Estamos limitando a caracteres alfabeticos de la "A" a la "Z" solo en MAYÚSCULAS
print(re.findall(pattern_1, prueba))
print(re.match(pattern_1, prueba))

pattern_1 = r'[0-9]' # Estamos limitando a caracteres numericos del 0 al 9, esto tambien puede llevar diferente rango de numeros por ej [0-5], [6-9] etc. Si hay un numero que lo hayamos pasado en la cadena como numero negativo, esta regex tomara solo el numero como tal, es decir si pasamos "-9", tomara en cuenta el "9", pero no el guión medio, es decir no sabra diferenciar si es un número positivo o negativo
print(re.findall(pattern_1, prueba))
print(re.search(pattern_1, prueba))

pattern_1 = r'\d' # La regex \d toma en cuenta solo los caracteres numericos (ninguno otro)
print(re.findall(pattern_1, prueba))

pattern_1 = r'\D' # La regex \D toma en cuenta solo los caracteres alfabeticos (letras, espacios, signos, etc, cualquiera que no sea un número)
print(re.findall(pattern_1, prueba))

pattern_1 = r'[l].' # El punto indica cualquier caracter que este a continuación del caracter que le pasamos, en este caso la "l". Excepto el caracter de salto de linea (\n)
print(re.findall(pattern_1, prueba))

pattern_1 = r'[l].*' # El astericos significa zero o mas veces. Pero basicamente lo que hace es que sea todo lo que esta despues del caracter que le pasamos, en este caso la "l". Arroja como resultaado todo lo demas despues de que se encuentra la primera "l" en la cadena. En otras palabras es todo un conjunto que parte de la primer "l" en adelante
print(re.findall(pattern_1, prueba))

print('----- REGEX Personales de práctica -----')

print('----- Letras, palabras y tildes -----')

# Letras mayúsculas, minúsculas y con acentos

name = 'Moisés'
pattern_2 = r'[a-z|A-Z]'
print(re.findall(pattern_2, name))

name = 'Moisés'
pattern_2 = r'[a-z|A-Z|á-ú]'
print(re.findall(pattern_2, name))

lastname = 'Hernández'
pattern_2 = r'[a-zA-Zá-ú]'
print(re.findall(pattern_2, lastname))

print('----- Números -----')

# Numeros simulando numeros telefonicos

num_df_edomex_1 = '5532798126'
num_df_edomex_2 = '5621179856'
num_df_edomex_3 = '9984715263'
pattern_3 = r'^[55|56]'
print(re.findall(pattern_3, num_df_edomex_1))
print(re.findall(pattern_3, num_df_edomex_2))
print(re.findall(pattern_3, num_df_edomex_3))

print('----- Telefonos de México -----')

if len(num_df_edomex_1) == 10:
    num_comprobation_1 = re.findall(pattern_3, num_df_edomex_1)
    if len(num_comprobation_1) == 1:
        print(num_df_edomex_1)
    else:
        print(f'El número ingresado NO es válido: ({num_df_edomex_1})')
        
if len(num_df_edomex_2) == 10:
    num_comprobation_2 = re.findall(pattern_3, num_df_edomex_2)
    if len(num_comprobation_2) == 1:
        print(num_df_edomex_2)
    else:
        print(f'El número ingresado NO es válido: ({num_df_edomex_2})')
        
if len(num_df_edomex_3) == 10:
    num_comprobation_3 = re.findall(pattern_3, num_df_edomex_3)
    if len(num_comprobation_3) == 1:
        print(num_df_edomex_3)
    else:
        print(f'El número ingresado NO es válido: ({num_df_edomex_3})')
        
print('')        
print('----- Telefonos de Cancún -----')
        
num_can_1 = '55-3279-8126'
num_can_2 = '56-2117-9856'
num_can_3 = '998-471-5263'

pattern_4 = r'^[99]'

if len(num_can_1) == 10 or len(num_can_1) == 12:
    num_comprobation_1 = re.findall(pattern_4, num_can_1)
    if len(num_comprobation_1) == 1:
        print(num_can_1)
    else:
        print(f'El número ingresado NO es válido: ({num_can_1})')
        
if len(num_can_1) == 10 or len(num_can_1) == 12:
    num_comprobation_2 = re.findall(pattern_4, num_can_2)
    if len(num_comprobation_2) == 1:
        print(num_can_2)
    else:
        print(f'El número ingresado NO es válido: ({num_can_2})')
        
if len(num_can_1) == 10 or len(num_can_1) == 12:
    num_comprobation_3 = re.findall(pattern_4, num_can_3)
    if len(num_comprobation_3) == 1:
        print(num_can_3)
    else:
        print(f'El número ingresado NO es válido: ({num_can_3})')
        
print('')
print('----- Validando E-mail -----')

print('')
# email = 'moises_hl@gmail.com.mx'

email_validation = r'^[A-Za-z0-9._+-]+@[A-Za-z0-9]+\.[a-z]+\.[a-z]+$' # Con esta regex al parecer tambien cubrimos dominios como por ej el .com.mx

# email_validation = r'^[A-Za-z0-9._+-]+@[A-Za-z0-9]+\.[a-z.]+$' # Pero con esta tambien cubrimos dominios como .com.mx porque? Porque dentro del ultimmo string que estamos definiendo despues del punto agregamos tambien el punto, eso quiere decir que el string seguido del punto puede o no contener un punto, asi que por lo tanto el .com.mx no lo toma como separado, .com y despues .mx, si no que lo considera como un solo string .com.mx gracias a esto ultimo [a-z"."]...

# email_validated = re.findall(email_validation, email)
# print(email_validated)

def emails_validation(email):
    email_validating = r'^[A-Za-z0-9._+-]+@[A-Za-z0-9]+\.[a-z]+\.?[a-z]+$'
    email_validated = re.findall(email_validating, email)
    if len(email_validated) == 1:
        print(email)
    else:
        print('Email NO valido')
        
emails_validation('moises_hl@gmail.com') # Check
emails_validation('moises_hl@gmail.com.mx') # Check
emails_validation('moises_hlgmail.com.mx') # Sin @
emails_validation('moises_hl@gmailcom') # Sin punto antes del com
emails_validation('moises_hl@@gmailcom') # Con doble @
emails_validation('moises_hl@gmail..com') # Con doble punto antes del com
emails_validation('moises_hl@.com') # Sin cadena de texto despues del aroba
emails_validation('@gmail.com') # Sin cadena de texto antes del aroba