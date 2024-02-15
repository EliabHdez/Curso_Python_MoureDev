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

print("*********************************************************************************************************************************************")

# --- TIPOS DE DATOS ---

'''
    Hay diferentes tipos de datos
    - string
    - int
    - float
    - complex
    - booleano
    - entre otros
    
    https://github.com/Asabeneh/30-Days-Of-Python/blob/master/02_Day_Variables_builtin_functions/02_variables_builtin_functions.md
'''

# Cómo consultar el tipo de dato?
# El metodo type() nos sirve para saber el tipo de dato

print(type('Soy un dato de tipo str')) # Tipo str - cadena de texto
print(type(5)) # Tipo int - numero entero
print(type(3.1416)) # Tipo float - numero decimal
print(type(3 + 1j)) # Tipo complex
print(type(True)) # Tipo booleano

print("*********************************************************************************************************************************************")

# --- FUNCIONES DEL SISTEMA ---

# Python tiene funciones o metodos predeterminados que nos permiten hacer diferentes tipos de acciones para llegar a ciertos resultados en concreto

"""
    Existen diferentes y varios tipos de funciones o metodos. Por ejemplo
    
    int() -> Permite cambiar un numero decimal a entero
    float() -> Permite tener decimales
    str() -> Permite cambiar el tipo de dato a un string
    len() -> Te indica la cantidad de caracteres de un dato contando los espacios
"""

print("*********************************************************************************************************************************************")

# --- INPUTS ---

# El metodo o la funcion input nos sirve para solicitar mediante consola datos o valores que el usuario tendra que especificar. Esto no es muy comun, ya que los usuarios casi no interactuan con la terminal, esto se aplica mas para cuando instalas un programa donde te pregunta si quieres instalar y tu tienes que confirma o negar

"""
name = input("What's your name? ")
age = input("How old are you? ")

print(name)
print(age)
"""