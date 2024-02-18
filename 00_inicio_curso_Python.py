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

""" 
    IMPORTANTE: HAY QUE PROCURAR QUE CUANDO DECLAREMOS UN DATO ESE DATO SEA SIEMPRE DEL MISMO TIPO EN NUESTRO PROGRAMA. ES DECIR, SI DECLARAMOS UNA VARIABLE, QUE SEA SIEMPRE UNA VARIABLE, SI ES CONSTANTE QUE SIEMPRE SEA UNA CONSTANTE, QUE SI ES UNA LISTA O TUPLA SIEMPRE SEA UNA LISTA O TUPLA...
    
    NO ESTAR CAMBIANDO EL TIPO DE DATO
    
    SI SE VA A CAMBIAR QUE SEA TAL CUAL POR QUE ASI LO REQUERIMOS, PERO A MEDIDA QUE SEA POSIBLE HAY QUE PROCURAR NO MUTAR NUESTROS DATOS, VARIABLES, ETC... ESTO HACE MAS SEGURO AL PROGRAMA Y ES MENOS PROBABLE QUE TENGAMOS ERRORES ADEMÁS DE QUE HACE AL CODIGO MAS FÁCIL EN SU MANTENIMIENTO
"""

""" 
    "del"
    
    La función "del" es una funcion propia del sistema, que nos sirve para eliminar. Pero esta a diferencia de las funciones que nos encontramos que nos permiten eliminar datos o elementos como remove(), pop() es que no es propia de algo en especifico como de una lista, tupla etc, esta es del sistema y elimina todo por completo, es decir que va a eliminar la variable, el constructor, una función etc...
    
    Ejemplos:
    
    my_fisrt_variable = "Hola Mundo"
    list(("Moises", "Hernandez", 33))
    function myAlias{
        my_alias = "Predator"
        print(my_alias)
    }
    
    del my_first_variable
    del list()
    del myAlias
    
    Con "del" conseguimos eliminar la variable, la lista y la función por completo, NO solo los datos o instrucciones almacenadas en ellas
"""