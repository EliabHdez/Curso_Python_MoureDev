# Imprimiendo el primer Hola ...
# Hagamos un Hola mundo

print("Hola Python")
print('Hola Mundo')

"""
    Este es
    un comentario
    en varias
    lineas
"""

'''
    Los comentarios en varias lineas
    tambien se pueden hacer
    con comillas simples
'''

# -----------------------------------------------------------------------------------------------------------

print('-------------------------------------------------')

# Tipo de dato - Metodo type()

# El metodo type() nos sirve para saber el tipo de dato

'''
    Hay diferentes tipos de datos
    - string
    - int
    - float
    - complex
    - booleano
    - entre otros
'''

print(type('Soy un dato de tipo str')) # Tipo str - cadena de texto
print(type(5)) # Tipo int - numero entero
print(type(3.1416)) # Tipo float - numero decimal
print(type(3 + 1j)) # Tipo complex
print(type(True)) # Tipo booleano

# -----------------------------------------------------------------------------------------------------------

print('-------------------------------------------------')

# Variables

# Las variables tienen ciertos estandares y aunque podemos poner el nombre de una variable como queramos lo cierto es que hay estandares que nos ayudan a definir nombres de variables... Ej, podemos llamar a una variable firstName FirstName firstname, FIRSTNAME etc, pero esto al menos en Python no es como tal un error pero si una mala practica. Lo ideal es que si la variable va a llevar mas de una palabra estan esten separadas con un guion bajo. Ej first_name, my_first_name etc

first_name = 'Moises'
last_name = 'Hernandez'
my_string_variable = 'variable de cadena de texto'
my_bool_variable = False

print(first_name)
print(last_name)
print(my_string_variable)

# Con el print podemos imprimir en pantalla mas de una variable o dato separados por comas

print(first_name, last_name, my_string_variable, my_bool_variable)

print("__________________________________________________________________________________________")

# Vamos a mezclar un poco de todo de lo que hemos visto hasta ahorita

str_variable = "Hello Everybody"
int_variable = 33
cambio_tipo_de_dato = str(int_variable)
dato_cambiado = type(cambio_tipo_de_dato)

print(str_variable)
print(int_variable)
print(type(int_variable), "-> Tipo de dato que es en ese momento el dato de la varible int_variable")
print(cambio_tipo_de_dato, "-> Dato de la variable int_variable ya cambiado de tipo")
print(dato_cambiado, "-> Tipo de dato que es la variable int_variable, despues del cambio de dato. Este dato pasa a cambiar de tipo gracias al metodo 'str()'. El valor o dato de esta variable ya no se puede ocupar como numero")

print(type(print(first_name, last_name, my_string_variable, my_bool_variable))) # Prueba rara... jajaja. Print no tiene un tipo de dato por que es una funcion del sistema

# Fin pruebas de print con lo visto hasta este momento

print("__________________________________________________________________________________________")

# Funciones del sistema

# Python tiene funciones predeterminadas que nos permiten hacer diferentes tipo de cosas para llegar a ciertos resultados

"""
    Existen diferentes y varios tipos de funciones. Por ejemplo
    
    int() -> Permite cambiar un numero decimal a entero
    float() -> Permite tener decimales
    str() -> Permite cambiar el tipo de dato a un string
    len() -> Te indica la cantidad de caracteres de un dato contando los espacios
"""

variable_int = int(3.7416) # La funcion o metodo int() redondea el valor decimal a la baja
variable_float = 90+2.7
suma = variable_int + variable_float
variable_str = str(33)
variable_len = len("Eliab Hernandez") # Cuenta el numero de caracteres de un dato contando los espacios tambien

print(variable_int) # La funcion o metodo int() redondea el valor decimal a la baja
print(variable_float)
print(variable_str, "-> Aunque es un numero, el tipo de dato ya no es numerico; ni entero, ni decimal, ahora es del tipo de dato string")
print(type(variable_str))
print(variable_len, "-> Numero de caracteres totales contemplando el espacio que contiene la cadena de texto 'Eliab Hernandez'") # Cuenta el numero de caracteres de un dato contando los espacios tambien. El resultado sera un numero equivalente al numero de caracteres del dato
print("El resultado de la suma es:", float(variable_int + int(variable_float))) # Podemos observar en la impresion de pantalla que nos da el resultado con decimal aunque la suma de nuestros datos tengas valores enteros
print("El resultado de la suma es:", suma)

print("__________________________________________________________________________________________")

# Variables en una sola linea

# Podemos definir varias variables en una sola linea con sus respectivos valores

name, surname, age, alias = "Moises", "Hernandez", 33, "Molleja"

print(name, surname, age, alias)
print("Me llamo ", name, surname, ". Tengo", age, "años y me conocen como la ", alias)
print(f"Me llamo {name} {surname}. Tengo {age} años y me conocen como la {alias}")

# Mencionar que si bien no esta mal esto de poner varias variables en una sola linea, podria llegar a ser una mala practica porque podriamos equivocarnos, confundir variables o los valores de estas y podriamos echar a perder el programa y el codigo. Si se usa hay que tener cuidado, hay que hacerlo con precaucion y con datos o variables bien claras para evitar errores o confusiones. Ademas de que hace mas dificil el mantenimiento del codigo...