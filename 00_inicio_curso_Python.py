# Imprimiendo el primer Hola ...
# Hagamos un Hola mundo

""" 
    PYTHON ES UN LENGUAJE DE TIPADO DINAMICO 

    ESTO QUIERE DECIR QUE SE PUEDE CAMBIAR EL TIPO DE DATO, ES DECIR QUE PODEMOS TENER DE INICIO UN DATO DE TIPO STRING Y DESPUES CAMBIARLO A UN TIPO DE DATO INT Y ASI CON CUALQUIR TIPO DE DATO 
    
    HAY QUE TENER CUIDADO CON ESTO PORQUE OJO ESTO PUEDE SER MUY SUSCEPTIBLE A ERRORES
    
    EJEMPLO DEL TIPADO DINAMICO:
    
    number_one = 5
    number_two = 3
    
    CAMBIAMOS EL VALOR DE LA VARIABLE number_two
    
    number_two = "3" -> Cambiamos el tipo de dato de la variable. Ahora aunque sigue teniendo el numero tres el tipo de dato ya no es de tipo int (numerico), ahora es de tipo string (cadena de texto)
"""

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
    - string (los strings vacíos adoptan el tipo de dato booleano "False")
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
    
    La función "del" es una funcion propia del sistema, que nos sirve para eliminar. Pero esta a diferencia de las funciones que nos encontramos que nos permiten eliminar datos o elementos como remove(), pop() es que no es propia de algo en especifico como de las listas, tuplas etc, esta es del sistema y nos sirve para eliminar casi cualquier cosa. Es decir podemos eliminar desde una variable, un constructor, una función etc... hasta eliminar un dato o elemento en especifico. Esto va a depender de como y en donde utilicemos la función "del"
    
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
    
    Pero... si la usamos de la siguiente manera conseguimos eliminar datos o elementos en concreto por ejemplo de una lista, tupla, diccionario etc...
    
    del my_dict["Sexo"]
    print(my_dict)
    
    Con esto logramos eliminar el valor relacionado con la clave "sexo" en el diccionario y NO eliminamos el diccionario completo como tal, porque? porque le estamos especificando un dato o elemento que deseamos eliminar. Si no le pasaramos este dato, si eliminaria el diccionario como tal, completo *** Ver el archivo 07 para tener contexto del diccionario, la clave y el valor que elimino ***
"""

""" 
    Semejanzas y diferencias entre listas, tuplas, sets y diccionarios
    
    Semejanzas
     - La estructura de todos es mediante un constructor
     - Para todos se utilizan "()" para crear el constructor. Ej list(), tuple(), set(), dict()
     - Todos guardan datos mediante un bloque
     - Todos admiten las funciones "type" y "len" (puede ser que también algunas otras)
     - Las listas y las tuplas pueden hacer uso de los corchetes para solictar/desempaquetar datos por medio del número de índice. Ej my_list[1], my_tuple[5]. Los diccionarios tambien pueden hacer uso de los corchetes, pero no ocupan el índice
     - Las listas y las tuplas pueden hacer uso de los corchetes para solictar/desempaquetar datos por bloques mediante el número de índice. Ej my_list[1:3], my_tuple[5:7]
     - En los sets y los diccionarios se usan llaves para guardar los datos o elementos
     - Todos pueden hacer uso de las funciones clear() para limpiar y vaciar las estructuras
     - Todos pueden hacer uso de las funciones remove(), para eliminar un elemento de la estructura
     - Las listas y las tuplas son estructuras ordenadas
     - Las listas y las tuplas permiten concatenación entre ellas (siempre y cuando sean todas listas o tuplsa, no entre diferentes tipos de estructuras)
     
    Diferencias
     - Las listas utilizan "[]" para guardar los datos o elementos. Ej my_list = []
     - Las tuplas utilizan "()" para guardar los datos o elementos. Ej my_tuple = ()
     - Los sets y diccionarios utilizan "{}" para guardar los datos o elementos. Ej my_set/dict = {}
     - Las listas son estructuras mutables (modificables)
     - Las tuplas son estructuras inmutables (no se pueden modificar)
     - Las tuplas y los sets no admiten datos o elementos repetidos/duplicados
     - Los sets no pueden utilizar "[]" para solicitar/desempaquetar datos o elementos por el número de índice
     - Los sets son estructuras desordenadas. Cada que se ejecuta el programa, los datos cambian den posición dentro del set
     - Los sets no permiten concatenación entre estos mismos
     - Los diccionarios ocupan los "[]" para desempaquetar datos pero lo hacen mediante la clave para returnar el valor de dicha clave. Ej my_dict["Nombre"] -> retorna el valor "Moisés"
"""