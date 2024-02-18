# --- TUPLES ---

# Una tupla nos sirve

# Las tuplas son INMUTABLES, es decir que no se pueden modificar de ninguna manera

"""
    Podemos definir tuplas de las siguientes maneras:
    
    my_tuple = tuple() -> Con esta forma estamos declarando que va a ser una tupla, pero no le asignamos los datos al momento.
    
    my_tuple_2 = () -> Con esta forma ya esta declarada la tupla como tal y se le pueden asignar los datos en ese momento
    
    Cualquiera de los dos constructores anteriores nos vale
    
    Los datos de las tuplas deben de ir separados por una coma
    
    Las tuplas son inmutables, es decir que no se pueden modificar de ninguna manera
"""

print("________Constructores___________")

# Constructores para crear una tupla

my_tuple = tuple()
my_tuple_second = ()

my_tuple = (33, 1.76, "Moisés", "Hernández", "Moisés", "Predator_Rider")

print(my_tuple)
print(type(my_tuple))

print(my_tuple[0])
print(my_tuple[2])
# print(my_tuple[4]) IndexError: tuple index out of range
# print(my_tuple[-6]) IndexError: tuple index out of range
print(my_tuple.count("Hernández")) # Cuenta cuantas datos iguales hay dentro de la tupla
print(my_tuple.count("Hernandez")) # Diferencia cualquier tipo de caracter, como en este caso los acentos
print(my_tuple.count("Moisés"))

print(my_tuple.index("Predator_Rider")) # Nos indica el número de indice que tiene el valor que le pasamos
print(my_tuple.index("Moisés")) # Si hay más de un valor igual en la tupla nos va a indicar el indice correspondiente al primer valor encontrado

# my_tuple[5] = "La Molleja" # Como se menciono en la anotación del comentario inicial, las tuplas son inmutables, por lo tanto no podemos modificar ningun dato, elemento o valor -> TypeError: 'tuple' object does not support item assignment

print("________concatenación___________")

# Se pueden concatenar tuplas

my_tuple_second = (78, 69, 51, 35, 33)
my_tuples_concat = my_tuple + my_tuple_second
print(my_tuples_concat)

print(my_tuples_concat[1:4]) # Podemos encapsular cierto bloque de elementos o datos. Recordar que el último no lo toma en cuenta, es decir en este ejemplo no nos arroja en la impresión el dato correspondiente al indice 4. Solo toma en cuenta en 1, 2 y 3!

# Hay formas en las que podríamos modificar los datos o elementos de una tupla, sin embargo hay que tener en cuenta que para hacer esto, la tupla deja de ser una tupla y una de esas formas en convertirla en una lista. Al hacer esto hay que estar muy concientes que ya no es una tupla, es una lista y ahora podemos hacer todo lo que se puede hacer con una lista...

print("________tupla a lista___________")

my_tuple = list(my_tuple)
print(my_tuple)
print(type(my_tuple))

my_tuple[5] = "Slevin_Kelebra"

my_tuple.append("Las Motos")
my_tuple.insert(4, "O+")
my_tuple.insert(2, 60)

print(my_tuple)

my_tuple.pop(6)
print(my_tuple)

print("________convertimos nuevamente a tupla___________")

my_tuple = tuple(my_tuple)
print(my_tuple)
print(type(my_tuple))

""" Hay que procurar desde un inicio utilizar el tipo de estructura que vayamos a ocupar y que sea el que mas se adecue a nuestras necesidades y nuestro programa para no tener que estar haciendo cambios de este tipo como convertir una tupla en una lista o visceversa

Que los datos pueden cambiar y necesitamos una estructura mutable pues utilizamos listas, que necesitamos una estructura inmutable porque sus datos no se van a cambiar en ningun momento de nuestro programa utilizamos una tupla

El recurso de cambairlos hay que dejarlo al último y esto solo si por alguna razón a la mera hora necesitamos cambiar un valor de una tupla o bien necesitamos que una lista ya no se modifique para que no vaya a haber errores en el programa, solo asi. Ya que si estamos cambiando y cambiando estamos mas propensos a que nuestro programa vaya a tener un error, además de que mientras ocupemos datos que no sean mutables nuestro programa se hace mas seguro """

# Con las tuplas también podemos utilizar la accion reservada del sistema "del", sin embargo solo sera para algo muy concreto y es para eliminar la variable que contiene la tupla como tal, ya que una tupla al ser inmutable no nos permite borrar un elemento de esta, por lo tanto si queremos utilizar "del" y le pasamos un dato en concreto para eliminarlo no va a ser posible

""" 
    del my_tuple[7] TypeError: 'tuple' object doesn't support item deletion
    
    golda = "Katana"
    age_golda = 5

    print(golda, age_golda)

    golda = "Husky"

    print(golda)

    del golda, age_golda

    print(golda)
    print(age_golda)
    
    Como podemos observar y si descomentamos este codigo y lo corremos nos vamos a poder dar cuenta que la acción "del" borra como tal las variables, no solo el contenido de estas. De hecho en el error que da si imprimimos vamos a ver el error "NameError, que quiere decir que el nombre de la variable no esta definido
"""

del my_tuple # Eliminamos por completo la variable "my_tuple"
# print(my_tuple) NameError: name 'my_tuple' is not defined