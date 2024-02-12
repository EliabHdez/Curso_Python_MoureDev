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

print("*********************************************************************************************************************************************")

# TIPOS DE DATOS

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

# -----------------------------------------------------------------------------------------------------------

print("*********************************************************************************************************************************************")

# VARIABLES

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

print("*********************************************************************************************************************************************")

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

print("*********************************************************************************************************************************************")

# FUNCIONES DEL SISTEMA

# Python tiene funciones o metodos predeterminados que nos permiten hacer diferentes tipos de acciones para llegar a ciertos resultados en concreto

"""
    Existen diferentes y varios tipos de funciones o metodos. Por ejemplo
    
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

print("*********************************************************************************************************************************************")

# VARIABLES EN UNA SOLA LINEA

# Podemos definir varias variables en una sola linea con sus respectivos valores

name, surname, age, alias = "Moises", "Hernandez", 33, "Molleja"

print(name, surname, age, alias)
print("Me llamo ", name, surname, ". Tengo", age, "años y me conocen como la ", alias)
print(f"Me llamo {name} {surname}. Tengo {age} años y me conocen como la {alias}")

# Mencionar que si bien no esta mal esto de poner varias variables en una sola linea, podria llegar a ser una mala practica porque podriamos equivocarnos, confundir variables o los valores de estas y podriamos echar a perder el programa y el codigo. Si se usa hay que tener cuidado, hay que hacerlo con precaucion y con datos o variables bien claras para evitar errores o confusiones. Ademas de que hace mas dificil el mantenimiento del codigo...

# INPUTS

# El metodo o la funcion input nos sirve para solicitar mediante consola datos o valores que el usuario tendra que especificar. Esto no es muy comun, ya que los usuarios casi no interactuan con la terminal, esto se aplica mas para cuando instalas un programa donde te pregunta si quieres instalar y tu tienes que confirma o negar

"""
name = input("What's your name? ")
age = input("How old are you? ")

print(name)
print(age)
"""

# Es importante saber que las variables pueden cambiar su tipo, asi que hay que tener cuidado cuando trabajemos con ellas ya que Python no es un lenguaje de programacion fuertemente tipado, por lo tanto una variable que puede tener un valor entero despues podriamos reasignarla y darle un valor numero o de algun otro tipo

# Cambio del tipo de valor de una variable

name = False
age = "Moises"
alias = 33

print(name)
print(age)
print(alias)

# Cambiamos el tipo de valor de las variables, aunque anteriormente ya tenian un valor de cierto tipo al momento de declararlas y darles otro valor este cambia en la variable y si es de un tipo diferente la variable lo reconocera con el nuevo tipo de dato. Ej name ahora tiene un valor de tipo booleano, age tiene un valor de tipo string y alias tiene un valor de tipo entero

# Forzamos el tipo de dato de una variable??? -> Si bien podemos especificar en la variable que queremos que el valor sea un tipo en concreto no quiere decir que no se pueda cambiar el tipo de dato. El ponerle el tipo de dato en la variable no nos va a permitir un tipado ni un bloqueo en la misma, esto solo sirve a modo visual, a modo de aviso

address: str = ("Huehuetoca")
print(address)
address = 54696 # Veemos que aunque la variable address esta "tipada" aun asi en cuanto le asignamos un valor de diferente tipo este cambia
print(address)
print(type(address))

# Podriamos decir que es un tipado debil, ya que solo sirve a modo de aviso, ya que si le asignamos un valor de diferente tipo si va a cambiar el valor y el tipo de la variable

print("*********************************************************************************************************************************************")

# OPERADORES

"""
    Existen diferentes tipos de operadores. Tenemos los operadores de asignación, los operadores aritméticos, los de comparacion etc...
    
    Estos nos sirven para hacer operaciones, comparaciones entre otras cosas mas, por ejemplo:
    
    - suma
    - resta
    - multiplicacion
    - division
    - mayor, menor o igual
    - entre otros...
    
    https://github.com/Asabeneh/30-Days-Of-Python/blob/master/03_Day_Operators/03_operators.md
"""

# OPERADORES ARITMÉTICOS

print(3 + 4)
print(3 - 4)
print(3 * 4)
print(3 / 4)
print(10 % 3) # El operador modulo nos arroja como resultado cuantos numeros sobran de la suma de "x" numero hasta llegar al numero indicado. Ej 3+3=6+3=9, el tope es 10, por lo tanto ya no se puede sumar mas otros 3, y del 9 que es el ultimo numero de la suma de esos "3" para llegar al 10, falta un numero y este es el resultado que arroja el operador de moduloQ|1E23R6Y7U890'
print(10 / 3)
print(10 // 3) # El operador floor division (//) redondea hacia abajo un número hacia su entero más cercano
print(2 ** 3) # El operador '**' es para la potencia o elevación (2*2=4*2=8)
print(2 ** 3 + 3 - 7 / 1 // 4) # Podemos mezclar los operadores aritmeticos entre ellos las veces que queramos para realizar operaciones complejas, siempre y cuando todos los valores sean de tipo númerico

print("Hola " + "Python, " + "¿Qué tal?") # El operador '+' sirve aparte de poder hacer sumas para concatenar datos. Es decir ir poniendo el siguiente dato delante del anterior
# print("Hola " + 5) Esto da un error ya que no podemos ni sumar ni concatenar datos de tipo string con datos numericos, si lo necesitamos como tal, necesitariamos hacer uso del metodo str o directamente anotar el numero como tipo str
print("Hola " + str(5)) # Aqui estamos cambiando el tipo de dato, pasa de ser un dato de tipo int a str. Por lo tanto NO nos vamos a encontrar un error al momento de correr el programa
print("Hola " + "99") # Aqui estamos declarando el numero como dato de tipo string de manera directa, por lo tanto de igual manera NO vamos a tener un error

# Algunos operadores nos sirven para los datos de tipo string, sin embargo no hacen una operación matematica con el texto, si no mas bien sirven para concatenar o multiplicar dicho texto, ej, el operador '+' sirve para concatenar, pero el operador '*' sirve para multiplicar el str. Hay que tener muy bien definido como funciona este ultimo porque podria haber alguna confusión con su funcionamiento, pero para que quede lo mas claro posible, no se va a multiplar el numero con el texto, mas bien va a multiplicar el texto por el numero de veces correspondiente al numero asignado en dicha multiplicación

print("Hola " * 5) # Si observamos multiplico o repitió 5 veces la palabra 'Hola', no es que haya multiplicado el 5 por el hola, eso no se puede hacer!!!. Esto se puede hacer con operaciones aritmeticas siempre y cuando el resultado de un numero entero

print("Hola " * int(2 ** 3 + 12 / 2)) # Porque tuvimos que utilizar el metodo int??? Esto es debido a que en la operación hay una división y la división va a arrojar un valor de tipo float por defecto, por lo tanto si no ocupamos el metodo int() no arrojaria un error. Comprobemoslo...!!!

# IMPORTANTE: RECORDAR QUE LAS OPERACIONES LAS VA A REALIZAR DE ACUERDO A LA REGLA DE LOS SIGNOS, ES DECIR: PRIMERO LA DIVISION, DESPUES DE LA MULTIPLICACION, DESPUES LA SUMA Y HASTA EL ULTIMO LA RESTA (CONFIRMAR QUE ESTE BIEN LA REGLA DE LOS SIGNOS COMO LA EH DESCRITO ANTERIORMENTE), PERO POR EL RESULTADO (14 VECES REPETIDA LA PALABRA) PODEMOS DEDUCIR QUE LAS OPERACIONES SE REALIZARON EN ESE ORDEN...

print(2 ** 3 + 12 / 2) # Como vemos en la terminal, el valor de esta operación es '14.0' y esto es debido a la división que ejecuta la operación, si quitamos la división, nuestro resultado seria un número entero. Comprobemoslo...!!!

print(2 ** 3 + 12 - 2) # Observemos el resultado...

# Tambien lo podemos hacer de la siguiente manera, talvez no sea muy comun tener un dato float para esto pero por si llegase a ser el caso...
my_float = 2.5 * 2
print(int(my_float)) # Y porque tebemos que convertir el resultado a un valor de tipo entero? Porque aunque la operación sea una multiplicación al haber un numero de tipo float va a dar como resultado un numero con decimal. Tal cual el resultado de esta operación no es 5, es 5.0... Por lo tanto tenemos que hacer uso del metodo int()

# OPERADORES COMPARATIVOS