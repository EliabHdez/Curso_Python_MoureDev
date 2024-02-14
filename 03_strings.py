# --- STTRINGS ---

# Los strings es basicamente texto. Puede ser un texto compuesto desde una sola letra o numero, hasta una palabra o un conjunto de palabras. Para simplificarlo es todo aquel tipo de dato que va a ir entre comillas, ya sean dobles o simples

"""
    Cualquier duda o complemento de los strings, formateos etc... lo podemos checar en el siguiente enlace:
    
    https://github.com/Asabeneh/30-Days-Of-Python/blob/master/04_Day_Strings/04_strings.md
"""

string_uno = "10"
string_dos = "M"
string_tres = "M83"
string_cuatro = 'V12'
string_cinco = "Moises es mi nombre de pila"
string_seis = 'Eliab es mi segundo nombre'
string_siete = 'Hernandez Lopez son mis apellidos'
string_ocho = "Mientras el contenido se encuentre dentro de comillas lo tomara como de tipo string, no importa si ponemos palabras reservadas del sistema como True, False, print, etc, al estar dentro de comillas las toma como una palabras mas de un texto"

print(string_uno)
print(string_dos)
print(string_tres)
print(string_cuatro)
print(string_cinco)
print(string_seis)
print(string_siete)
print(string_ocho)

string_nombre = "Eliab"
string_apellido = "Hernández"

print("My name is " + string_nombre + " " + string_apellido)

# Dentro de los strings podemos ocupar caractéres especiales como el \n que sirve para dar un salto de línea \t que sirve para hacer una tabulación

salto_de_linea = "Este es un string\ncon salto de línea"
print(salto_de_linea)

tabulacion_de_string = "\tEste es un string con tabulación"
print(tabulacion_de_string)

# FORMATEO DE STRINGS

name, surname, age, alias = "Moisés", "Hernández", 33, "Molleja"

print("Mi nombre es %s %s y tengo %d años" %(name, surname, age)) # Este era el viejo metodo para formatear strings. Este metodo es el recomendado cuando se quiere proteger de cierta manera el codigo, hacer nuestros programas mas seguros, para que no haya errores al momento de pasarle variables, parametros, datos, etc. Ya que si definimos que se le va a pasar un string o un int o un float y a la mera hora nos equivocamos y le pasamos un valor con un tipo de dato diferente nos va a arrojar un error

# Ejemplo: print("Mi nombre es %s %s y tengo %d años" %(name, surname, alias))

print("Mi nombre es {} {} y tengo {} años".format(name, surname, age)) # Este es el nuevo estilo de formateo de strings

# Sin embargo hay otro metodo o estilo de formateo mas reciente que estuvo disponible a partir de Python 3.6 y que es el mas usado y como hasta este momento y ese estilo mas reciente es el de la inferencia o interpolación de datos, mejor conocido como f-strings

# Para hacer uso del metodo f-strings es necesario agregar una "f" antes de las comillas donde ira nuestro string

print("________f-strings___________")
print(f"Me llamo {name} {surname} y tengo {age} años.")

# Se puede concatenar pero no es lo mas óptimo, ya que aparte de ser mas laborioso, al lenguaje le cuesta mas trabajo ejecutar toda una concatenación que un formateo en el string

# DESEMPAQUETADO DE CARACTERES

print("___________________")
language = "Python"
a, b, c, d, e, f = language
print(a)
print(b)
print(c)
print(d)
print(e)
print(f)

print("___________________")

# DESEMPAQUETADO POR PARTES O CONTROLADO (DIVIDIDO O DIVISIÓN)

# En programación el conteo comienza desde 0, es decir que el conteo es... 0, 1, 2, 3 etc etc etc

# También podemos hacer el desempaquetado de derecha a izquierda, para esto se tiene que usar un indexado negativo y este empieza con -1, porque no con el 0 como cuando es de izq a der? Porque el 0 es un numero neutral, por lo tanto no puede ser negativo, debido a esto, el conteo negativo empieza con el 1. Es decir, el ultimo caracter es -1, seguido del -2, -3 y asi sucesivamente

first_letter = language[0]
print(first_letter)

second_letter = language[1]
print(second_letter)

last_letter = language[-1]
print(last_letter)

last_letter = language[-2]
print(last_letter)

last_letter = language[-5]
print(last_letter)

reversed_language = language[:-1]
print(reversed_language)

print("___________________")

language_slice = language[1:3]
print(language_slice)

language_slice = language[1:] # Aqui le estamos pasando un paramétro de donde tiene que empezar pero no donde tiene que terminar, por lo tanto toma todo hasta el final
print(language_slice)

language_slice = language[3:] # Aqui lo mismo que la anterior, pero empezando desde un nuevo caracter, en este caso el caracter que esta en la 3ra posición
print(language_slice)

language_slice = language[0:5:3] # Este no lo termine de entender muy bien, se brinca ciertos caracteres y muestra otros tantos pero no entendí la lógica, el como funciona!!! REVISARLO SI ES NECESARIO...
print(language_slice)

print("___________________")

# REVERSE (ORDEN REVERSIBLE)

reversed_language = language[::-1] # Repitiendo dos veces ':' conseguimos darle la vuelta al dato 180 grados, sin ninguna alteración en su estructura, vaya lo persivimos o leemos al reves
print(reversed_language)

print("___________________")

# FUNCIONES PARA STRINGS

marca_celular = "samsung"
modelo = "A54"
year_lanzamiento = "2023"
sistema_operativo = "ANDROID"

print(marca_celular.capitalize()) # Si el dato es de tipo alfabético (letra), la primera la pone con mayúscula
print(marca_celular.upper()) # Si el dato es de tipo alfabético (letra), todas las letras las pondra en mayúsculas
print(sistema_operativo.lower()) # Si el dato es de tipo alfabético (letra), todas las letras las pondra en minúsculas
print(marca_celular.upper().isupper()) # Aqui solo vamos a ver la confirmación de que el dato de la variable si esta en mayúsculas
print(marca_celular.count("s")) # Al metodo o funcion count() le tenemos que pasar un valor en forma de string. Este metodo va a contar cuantos caracteres iguales al declarado hay en el string en cuestión. Puede ser desde un solo caracter o varios, pero dentro de las mismas comillas y este lo tomara como un solo caracter...
print(marca_celular.count("sa"))
print(marca_celular.count("un"))
print(modelo.count("A54"))
print(modelo.count("A 54")) # Toma en cuenta los espacios
print(marca_celular.count("a")) # Diferencia entre mayúsculas y minúsculas
print(marca_celular.isnumeric()) # Nos indica si el dato dentro del string es numerico
print(modelo.isnumeric()) # Nos indica si el dato dentro del string es numerico
print(year_lanzamiento.isnumeric()) # Nos indica si el dato dentro del string es numerico
print(marca_celular.startswith("sa")) 
print(marca_celular.startswith("Sa")) # El startswith diferencia entre mayúsculas y minúsculas
print(marca_celular.endswith("g"))
print(marca_celular.endswith("ng"))
print(sistema_operativo.endswith("id")) # El endwith también diferencia entre mayúsculas y minúsculas