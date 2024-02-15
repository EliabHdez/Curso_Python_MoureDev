# --- LISTS ---

# Una lista sirve para agrupar datos

"""
    Podemos definir listas de las siguientes maneras:
    
    my_list = list() -> Con esta forma estamos declarando que va a ser una lista, pero no le asignamos los datos al momento. Podemos hacerlo, pero hay que añadir los corchetes. Los datos no pueden ir directamente dentro de los parentesís
    
    my_list_2 = [] -> Con esta forma ya esta declarada la lista como tal y se le pueden asignar los datos en ese momento
    
    Cualquiera de los dos constructores anteriores nos vale
    
    Los datos de las listas deben de ir separados por una coma
"""

my_list = list()
my_other_list = ["Moisés", "Eliab", "Hernández", "López"]

print(len(my_list))
print(my_other_list)

my_list = [33, 35, 25, 30, 62, 52, 30, 17]

print(my_list)
print(len(my_list))

# En las listas podemos guardar diferentes tipos de datos

my_other_list = ["Birmania", 12, "Huehue", "México", 55999]

person_data = ["Moisés", "Hernández", 33, 1.76, "Donadie"]

print(person_data)
print(my_other_list)

print(type(person_data))
print(type(my_other_list))

# Al igual que en el desempaquetado de datos de los strings, podemos solicitar un dato en específico de una lista

print(person_data[0])
print(person_data[1])
print(person_data[2])
print(person_data[3])
print(person_data[4])
#print(person_data[5]) IndexError - Index de lista fuera de rango

print("___________________")

# De igual manera lo podemos hacer del último dato al primero y se hace de la misma manera que en el desempaquetado, si vamos a solicitar los datos del último al primero, sera con indexado negativo empezando por el 1

print(person_data[-1])
print(person_data[-2])
print(person_data[-3])
print(person_data[-4])
print(person_data[-5])
#print(person_data[-6]) IndexError - Index de lista fuera de rango

print("___________________")

print(f"La dirección es: Calle: {my_other_list[0]} No. {my_other_list[1]}, en el Municipio de {my_other_list[2]}, en el Estado de {my_other_list[3]} CP: {my_other_list[4]}")

# El metodo count en las listas nos arroja el numero de concurrencias que hay de un mismo valor. En la lista el 30 se repite 2 veces. No confundir con el valor de un dato con el tipo de ese dato

print(my_list.count(30))
print(my_other_list.count("Birmania")) # Como vemos aqui el resultado que nos arroja es un 1, ya que lo que arroja como resultado es el valor del dato que es la palabra 'Birmania', NO el tipo de dato que seria string, que en la lista hay 3 de este tipo...

name, surname, age, height, alias = person_data # Desempaquetar una lista de esta manera aunque si bien es posible corremos el riesgo de regarla ya que si por alguna razon mutamos la lista, eso ya no será válido y nos arrojara un error. Pero bueno si se tiene que hacer por alguna razón lo hacemos y es mejor esta forma que la que esta a continuación. Eso si, hay que hacerlo con cuidado y asegurandonos de no mutar la lista y si lo hacemos agregar o quitar las variables que sean necesarias

print(name)
print(alias)

age, alias, surname, height, name = person_data[2], person_data[4], person_data[1], person_data[3], person_data[0] # Esto viene siendo lo mismo que lo anterior, solo que aqui acomodamos las variables en un orden que no coincide con los datos de nuestra lista, por lo tanto hay que asignarle de forma manual el dato a cada variable. Sin embargo aunque es posible hacerlo de esta manera no es lo mas recomendable, ya que es muy engrolloso y podemos cometer un error con facilidad
print(name)
print(height)

# Concatenación de listas

print(person_data + my_other_list)

print("___________________")

# MODIFICANDO LAS LISTAS -> AÑADIENDO Y ELIMINANDO ELEMENTOS

print("________append___________")
# Append inserta un dato al final de la lista
person_data.append("60 kgs")
print(person_data)

print("________insert___________")
# Insert agrega un elemento a la lista en el indice que le indiquemos. Primero anotamos el indice y separado por una coma el dato o elemento a añadir 
person_data.insert(4, "A+")
print(person_data)

print("________remove___________")
# Remove elimina un elemento de la lista en concreto (hay que pasarle un dato si o si)
person_data.remove("Donadie")
print(person_data)

# Es importante saber que el metodo remove elimina el primer elemento que se encuentra con el valor indicado
print(my_list)
my_list.remove(30) 
print(my_list)

person_data.insert(1, "Predator")
person_data.append("Programador")
person_data.append("Junior")

print(person_data)

print("___________________")

# Pop elimina el último elemento de la lista. Si no se le indica un dato concreto a eliminar, eliminara el último por defecto. La diferencia entre remove y pop es que el metodo pop almacena el dato eliminado y lo retorna...

# Que pasa en el siguiente caso y porque vemos que elimina de la lista el dato 'Junior' pero nos esta retornando 'Programador'???

"""
    Lo que sucede es lo siguiente:
        person_data.pop() -> En esta línea de código elimina el dato 'Junior' de la lista
        
        print(person_data) -> En esta línea nos muestra la lísta pero con el dato 'Junior' eliminado
        
        print(person_data.pop()) -> En esta línea es donde esta la clave y lo que sucede aquí es que le estamos solicitando nos imprima el dato eliminado, NO la lista como tal, solo el dato eliminado y la clave esta en que al tener el metodo pop() aun directamente en el print() vuelve a eliminar un elemento mas de la lista (recordar que el elemento 'Junior' ya no esta porque fue eliminado con la línea de código anterior), por lo tanto elimina el dato 'Programador', es por eso que ese es el dato que nos esta imprimiendo y no el de 'Junior'. En otras palabras hace las dos funciones en la misma línea de código, primero elimina el elemento y despues nos los imprime...
"""

print("________pop___________")
person_data.pop() 
print(person_data)
print(person_data.pop())

# Aqui sucede lo mismo que en el caso de arriba
person_data.pop(1) # Aqui elimina el dato que se encuentra en el índice 1
print(person_data) # Imprime la lista ya con el dato eliminado
print(person_data.pop()) # Y aqui vuelve a eliminar otro dato (el último por defecto al no tener un dato en especifico dentro de los parentesis) y ese dato es el que nos imprime, que en este caso es el dato '60 kgs'. De igual manera, elimina el dato y despues de haberlo eliminado nos lo imprime... Recordar que estamos solicitando nos imprima NO la lista, si no el dato eliminado
print(person_data) # Aquí podemos observar que en la lista ya no esta el dato '60 kgs'
print(person_data.pop(2)) # Si le pasamos un dato en especifico ese dato es el que elimina y de igual manera es el que nos retorna en la impresion, ya que hace las dos funciones en la misma línea de código
print(person_data)

print(my_list)
print(my_list.pop())
print(my_list)

print("___________________")

# Si quisieramos tener un poco mas control sobre el pop() o simplemente queremos entenderlo un poco mejor o de forma mas fácil, podríamos guardarlo en una variable para asi tener de una forma mas visual que elemento estamos eliminando

pop_list = [1, 2, 3, 4, 5, 6]

pop_data = pop_list.pop()
print(pop_data)

pop_data_second = pop_list.pop(2)
print(pop_data_second)

print("________del___________")
# Podemos eliminar un dato de una lista con 'del'. El metodo 'del' elimina elementos por medio del indice. Para esto anteponemos el metodo 'del' al nombre de la lista y le pasamos el indice del dato que queremos eliminar por medio de corchetes
pop_list.append(7)
print(pop_list)
del pop_list[4]
print(pop_list)

print("________clear___________")

# El metodo clear como su nombre lo indica limpia la lista, la deja vacía
print(pop_list)
pop_list.clear()
print(pop_list)

print("___________________")

# MODIFICANDO UN DATO, VALOR O ELEMENTO DE UNA LISTA

my_favorite_colors = ["Turquoise", "Aquamarine", "Black", "Red"]
print(my_favorite_colors)

# Podemos modificar un elemento de una lista declarando la lista y llamando al dato a modificar mediante su index dentro de corchetes, seguido de un igual y del nuevo dato que le vamos a dar
my_favorite_colors[1] = "Aqua Green"
print(my_favorite_colors)

#  Copy crea una copia de una lista

"""
    Profundicemos un poco mas en el copy...
    
    El siguiente es el mismo codigo que vamos a ver debajo de este comentario, pero vamos a desmenuzar un poco lo que el programa hace
    
    my_favorite_colors_second = my_favorite_colors.copy() -> Aqui creamos la copia de la lista my_favorite_colors
    my_favorite_colors.clear() -> Aqui limpiamos o vaciamos la lista my_favorite_colors

    print(my_favorite_colors) -> Imprimimos las lista my_favorite_colors y vemos que la lista esta limpia, vacia
    print(my_favorite_colors_second) -> Aqui imprimimos la lista my_favorite_colors_seconds con los mismos datos de la lista my_favorite_colors, vaya, que es la copia que habiamos generado con anterioridad... Y aquí viene lo que podría llegar a confundirnos un poco y por eso este comentario para aclararlo!
    
    Como es que la lista my_favorite_colors_second tiene los mismos datos que tenia la lista my_favorite_colors si a esta última le hicimos un clear y la limpiamos, la vaciamos por completo?
    
    Repasemos...
    
    Lo primero que hicimos fue la copia de la lista my_favorite_colors y esta copia la guardamos en otra lista llamada my_favorite_colors_second, en este momento se crea la copia y es también en este momento que la nueva lista ya tiene los datos de la copia, posteriormente procedemos a limpiar la lista my_favorite_colors, pero para este punto que limpiamos esta lista my_favorite_colors, la lista my_favorite_colors_second ya habia sido creada y ya tenia la copia, ya contenia todos los datos. Por eso al momento de limpiar la lista my_favorite_colors no se ve afectada la lista my_favorite_colors_second, porque esta última ya era otra lista, una nueva y por lo tanto una independiente que no se ve afectada por lo que hagamos o no con la lista my_favorite_colors
    
    Puede resultar un poco confuso, espero que haya quedado claro con la explicación anterior, pero si no vamos a simplificarlo...
    
    A la lista 1 (my_favorite_colors), le creamos una copia. Esta copia es la lista 2 (my_favorite_colors_second). La lista 2 ya es un dato independiente de la lista 1, por lo tanto lo que se le haga a cualquiera de las dos ya no afecta a la otra.
    
    Es algo asi como que... tenemos un video que se llama mi_video, creamos una copia y esta copia se llama mi_video_1. Si eliminamos, modificamos, renombramos o borramos el contenido del video "mi_video", cualquiera de estas acciones no van a surtir efecto en la copia, es decir, el video "mi_video_1", va a seguir siendo el mismo, el mismo contenido, el mismo nombre y va a seguir estando ahi!
"""

print("_________copy and clear__________")
my_favorite_colors_second = my_favorite_colors.copy()
my_favorite_colors.clear()

print(my_favorite_colors)
print(my_favorite_colors_second) # La nueva lista con la copia de los datos de la lista my_favorite_colors

print("________reverse___________")
# Reverse reacomoda los datos de una lista justo al reves. El último es ahora el primero, el primero es el último y asi sucesivamente
print(my_favorite_colors_second)
my_favorite_colors_second.reverse()
print(my_favorite_colors_second)

print("________sort___________")
# Sort acomoda los datos o elementos de una lista por orden ya sea alfabético o alfanumérico
print(my_favorite_colors_second)
my_favorite_colors_second.sort() 
print(my_favorite_colors_second)

my_new_list = ["Moto", "Honda", "CBR", 600, 2.4, "Lts", True, False]
# my_new_list.sort() TypeError -> not supported between instances of 'int' and 'str'
# print(my_new_list)

print("___________________")

# Rebanadas de las listas -> Se le conoce asi por que son ciertos elementos de las listas

# Con esto podemos solcitar ciertos elementos en concreto como por bloques o bien crear listas nuevas o sub-listas

print(my_new_list[1:2])
# No se aclara en el curso, pero yo entenderia que esto es una sub-lista. Una lista dentro otra lista
my_new_list.append(my_new_list[0:2])
print(my_new_list)

# Y estas son listas nuevas derivadas de los datos extraidos de una lista ya existente
brand_model_list = my_new_list[0:3]
print(brand_model_list)

engine_list = my_new_list[3:6]
print(engine_list)

bool_list_moto = my_new_list[6:-1] # Si ponemos el indice correspondiente al último dato no va a tomarlo en cuenta, si queremos tambien tomar en cuenta en ultimo dato de la lista tenemos que poner el indice -1
print(bool_list_moto)