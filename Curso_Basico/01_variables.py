# --- VARIABLES ---

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

# --- VARIABLES EN UNA SOLA LINEA ---

# Podemos definir varias variables en una sola linea con sus respectivos valores

name, surname, age, alias = "Moises", "Hernandez", 33, "Molleja"

print(name, surname, age, alias)
print("Me llamo ", name, surname, ". Tengo", age, "años y me conocen como la ", alias)
print(f"Me llamo {name} {surname}. Tengo {age} años y me conocen como la {alias}")

# Mencionar que si bien no esta mal esto de poner varias variables en una sola linea, podria llegar a ser una mala practica porque podriamos equivocarnos, confundir variables o los valores de estas y podriamos echar a perder el programa y el codigo. Si se usa hay que tener cuidado, hay que hacerlo con precaucion y con datos o variables bien claras para evitar errores o confusiones. Ademas de que hace mas dificil el mantenimiento del codigo...

print("*********************************************************************************************************************************************")

# --- CAMBIO DE TIPO DE DATO DE LAS VARIABLES ---

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

"""
    CONSTANTES...
    
    EN PYTHON NO HAY CONSTANTES COMO TAL, SI QUEREMOS IDENTIFICAR UNA VARIABLE COMO CONSTANTE PARA TENER EN CUENTA QUE ESE DATO NO DEBE SER MODIFICADO, LO HABITUAL DENTRO DE LOS PROGRAMADORES DE PYTHON A NIVEL DE SINTAXIS ES DEFINIR ESA VARIABLE CON MAYÚSCULAS, ESTO ES LO QUE SE HA TOMADO COMO UNA BUENA PRACTICA PARA DECLARAR UNA VARIABLE COMO CONSTANTE
    
    EJEMPLO:
        CONST_NAME = 3.1416
"""