# --- DICTIONARIES ---

# Los diccionarios es una estructura donde se almacenan datos clave:valor. Ej nombre:Moises, estos van como en grupo, de la mano

# Tenemos que definir que tipo de dato va a ser la clave y el valor

my_dict = dict()
my_other_dict = {}

print(type(my_dict))
print(type(my_other_dict))

my_other_dict = {"Moto":"Honda", "Modelo":"CBR600RR", "Cilindrada":600, "Tipo":"Deportiva"}

my_dict = {
    "Nombre":"Moisés",
    "Apellido":"Hernández",
    "Edad":33,
    "Ocupación":"Intento de programador",
    "Lenguajes":{"Python", "JavaScript", "HTML", "CSS"},
    1:1.76,
    "Tipo de sangre": "O+",
    "Sexo":"Masculino"
}

print("________desempaquetado de datos___________")
# Podemos desempaquetar datos mediante corchetes pasando como dato la clave
print(my_other_dict)
print(len(my_other_dict))
print(my_other_dict["Modelo"])

print(my_dict)
print(len(my_dict))
print(my_dict["Nombre"])

print("________modificando valor de una clave___________")
# Podemos modificar el valor de una clave. Esto lo hacemos de la siguiente manera
my_dict["Nombre"] = "Eliab"
print(my_dict["Nombre"])
print(my_dict[1]) # Recordar que esto es una clave, no un numero de índice.

print("________agregando datos___________")
# Podemos agregar mas datos clave:valor a los diccionarios. Esto lo hacemos de la siguiente manera
my_dict["País"] = "México"
print(my_dict)

# Cabe resaltar que si agregamos datos de la forma anterior, estos siempre se van a agregar hasta la última posición, si posteriormente nosotros agregamos datos de forma directa en el diccionario, estos se van a agregar en el orden donde los pongamos, como es el caso de tipo de sangre y sexo y aunque se hayan añadido despues de pais, al haberlos agregado de forma directa en el diccionario, se van a posicionar antes del agregado mediante codigo como el anterior, esto debido a que si recordamos el programa cada vez que se ejecuta lee primero las lineas de codigo que conforman el diccionario y despues las lineas donde se agrega otro elemento mediante corchetes, por lo tanto siempre va a leer lo que esta declarado directamente en el diccionario de forma directa

print("________del___________")
# Eliminar datos o elementos de un diccionario
del my_dict["Sexo"]
print(my_dict)

""" 
    my_other_dict = {"Moto":"Honda", "Modelo":"CBR600RR", "Cilindrada":600, "Tipo":"Deportiva"}

    my_dict = {
        "Nombre":"Moisés",
        "Apellido":"Hernández",
        "Edad":33,
        "Ocupación":"Intento de programador",
        "Lenguajes":{"Python", "JavaScript", "HTML", "CSS"},
        1:1.76,
        "Tipo de sangre": "O+",
        "Sexo":"Masculino"
} """

print("________in con valores___________")
# Metodo "in" en diccionarios con el valor
print("CBR600RR" in my_other_dict) # Resultado "False" porque? si si esta el valor "CBR600RR"
print("Hernández" in my_dict) # Resultado "False" porque? si si esta el valor "Hernández"

# PORQUE EL MÉTODO "in" SE BASA EN LAS CLAVES, LO QUE IDENTIFICA DENTRO DEL DICCIONARIO ES LA CLAVE, NO EL VALOR

print("________in con claves___________")
# Método "in" en diccionarios con la clave
print("Modelo" in my_other_dict)
print("Tipo" in my_other_dict)
print("Apellido" in my_dict)
print("Ocupación" in my_dict)
print("Tipo de sangre" in my_dict)

print("________items___________")
# La funcion items() identifica los datos mediante su clave:valor
print(my_dict.items())

print("________keys___________")
# La función keys() identifica las claves dentro del diccionario
print(my_dict.keys())

print("________values___________")
# La función values() identifica los valores de las claves (keys) dentro del diccionario
print(my_dict.values())

print("________fromkeys___________")
# La función fromkeys nos permite crear un nuevo diccionario con las puras claves (keys), sin valores
# Por lo que entendi en el curso el la función fromkeys no tiene mucho sentido ya que la ocupamos para crear un nuevo diccionario con las claves de otro ya existente, pero en realidad uno le tiene que especificar las claves y como le puede poner las de otro diccionario, como puedes ponerle claves nuevas y te las va a dar por buenas, por lo tanto no tiene mucho sentido, porque de ser asi solo creas un diccionario nuevo y ya. La diferencia que hay es que no le agregas valores a las claves al momento y no da error, pero fuera de eso, no tiene mucho sentido la función...
my_new_dict = my_other_dict.fromkeys({"Hobbit", "Trabajo", "Intereses"})
my_new_dict_second = my_other_dict.fromkeys(("Hobbit", "Trabajo", "Intereses"))
print(my_new_dict)
print(my_new_dict_second)
print(type(my_new_dict))
print(type(my_new_dict_second))

# Ahora bien, lo comentado es que lo mas recomendable es utilizar fromkeys con el constructor de diccionarios, asi podras crear un diccionario solo con las claves

# Incluso el constructor no necesita los "()", puede ir sin estos, seguido de forma directa de la función. Probe y cualquiera de las dos formas funciona, con o sin "()"
my_dict_from = dict.fromkeys({
    "Calle",
    "Colonia",
    "Municipio",
    "Estado"
})
print(my_dict_from)
print(type(my_dict_from))

""" 
    No podemos crear diccionarios con ninguno de los dos contructores si no le pasamos el valor a las claves y menos aun si lo hacemos sin la palabra reservada dict, ya que al no declarar esta palabra estariamos creando realmente un set()
    
    dict_test_without_values = dict({
        "Prueba",
        "Diccionario",
        "Sin valores"
    })
    print(dict_test_without_values)
    print(type(dict_test_without_values))
    
    El codigo dentro de este comentario no vale, da error, ya que las claves no tienen valores y si quitamos la palabra reservada dict() para que no de error, estariamos creando un set()
    
    Para crear un diccionario sin valores en las claves, ahi si que si podriamos usar la función fromkeys como en el codigo de arriba de este comentario! Lo cual al parecer no es muy habitual, pero se podria sar el caso de que lo necesitemos...
"""

print("________fromkeys para crear diccionarios en base a una lista, tuplas o sets___________")
# Podemos cambiar una lista a diccionario o dicho de otra manera, crear un diccionario en base a una lista con la función fromkeys(). Puede que esto ya tenga mas sentido y mas uso...
# Igual podriamos hacer lo mismo con una tupla o un set
my_list = [1, 2, 3, 4, 5]
print(my_list)
print(type(my_list))

my_number_dict = dict.fromkeys(my_list)
print(my_number_dict)
print(type(my_number_dict))

# Podemos reutilizar las claves de otro diccionario para crear uno nuevo sin valores con fromkeys. Esto puede que también ya tenga mas sentido, ya que nos ahorramos mucho código y tiempo en estar creando uno nuevo y estar anotando todas las claves
my_new_dict = dict.fromkeys(my_dict)
print(my_new_dict)

# Con la función fromkeys() podemos asignar un valor igual a todas las claves
my_new_dict = dict.fromkeys(my_number_dict, "Es un número entero")
print(type(my_new_dict))
print(my_new_dict)

my_new_dict_second = dict.fromkeys(my_number_dict, ("Es un número entero", "Y clave del diccionario"))
print(my_new_dict_second)

print("________tambien podemos pasar un diccionario a lista, tupla o set___________")

my_new_list = list(my_new_dict)
print(type(my_new_list))

my_new_tuple = tuple(my_new_dict)
print(my_new_tuple)
print(type(my_new_tuple))

my_new_set = set(my_new_dict)
print(my_new_set)
print(type(my_new_set))

print("________values___________")
# Con values accedemos a los valores de las claves del diccionario
my_values_dict = my_new_dict.values()
print(my_values_dict)
print(type(my_values_dict)) # Nos arroja el tipo de dato dentro de un diccionario, es decir, que son los valores de las claves (no, nos da como tal el tipo de dato, ya que el valor de las claves puede contener cualquier tipo de dato, string, int, float, etc, por lo tanto no nos podría decir que tipo de dato es cada uno, asi que lo engloba como tal y solo nos especifíca que son los valores dentro del diccionario)

my_values_dict_second = my_new_dict_second.values()
print(my_values_dict_second)
print(type(my_values_dict_second)) # Nos arroja el tipo de dato dentro de un diccionario, es decir, que son los valores de las claves (no, nos da como tal el tipo de dato, ya que el valor de las claves puede contener cualquier tipo de dato, string, int, float, etc, por lo tanto no nos podría decir que tipo de dato es cada uno, asi que lo engloba como tal y solo nos especifíca que son los valores dentro del diccionario)

print("________listas, tuplas, set o diccionarios incluso de los valores de un dict___________")

# Tambien podemos hacer listas, tuplas y/o sets de las claves o valores de los diccionarios utilizando las funciones de keys() y values() respectivamente y conviertiendolas a cualquiera de las mencionadas al principio de este comentario

print(my_other_dict)
print(type(my_other_dict))

keys_list = list(my_other_dict.keys())
print(keys_list)
print(type(keys_list))
values_list = list(my_other_dict.values())
print(values_list)
print(type(values_list))

keys_tuple = tuple(my_dict.keys())
print(keys_tuple)
print(type(keys_tuple))

# values_set = set(my_dict.values()) -> Esto da un error debido a que el diccionario tiene un set en uno de los valores de una clave. Es posible que si queremos hacer listas, tuplas o sets con las claves o valores de un diccionario nos encontremos con este problema y no sea posible, por lo tanto hay que estar atentos que datos de un diccionario queremos hacer una lista, tupla o set, de igual manera en viceversa

my_dict = {
    "Nombre":"Moisés",
    "Apellido":"Hernández",
    "Edad":33,
    "Ocupación":"Intento de programador",
    1:1.76,
    "Tipo de sangre": "O+",
    "Sexo":"Masculino"
}

# Reasignamos el diccionario my_dict para eliminar la clave/valor lenguajes que era la que nos daba problemas al querer crear un set de los valores, sin embargo la tupla que generamos con las claves si corresponde al primer diccionario my_dict, por lo tanto la tupla si va a contener la clave lenguajes, pero el set no va a contener el valor de esta clave que eran los lenguajes de programación y lo podemos corroborar en la impresión de la consola
values_set = set(my_dict.values())
print(values_set)
print(type(values_set))