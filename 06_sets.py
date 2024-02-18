# --- SETS ---

# Un set tambien es una estructura que nos permite almacenar un bloquee de datos o elementos

# Un set no es una estructura ordenada. Es decir que los elementos o datos los va guardando un poco como quiere y cada vez que el programa se ejecuta este orden cambia y cada elemento ocupa un orden distinto por lo tanto tiene un índice diferente cada vez

my_set = set()
my_other_set = {} # Inicialmente es un diccionario

print(type(my_set))
print(type(my_other_set))

my_other_set = {"Moisés", "Hernández", 33}
print(my_other_set)
print(type(my_other_set))

print(len(my_other_set))

""" print(my_other_set[2]) -> TypeError: 'set' object is not subscriptable. Con esto comprobamos que el set no es una estructurada ordenada, es por eso que no podemos desempaquetar datos por medio de su indice ya que estos cambian cada que se ejecuta el programa """

print("________add___________")
# Podemos agregar datos o elementos al set con "add"
my_other_set.add("Predator")
print(my_other_set)

# Los sets no admiten datos o elementos repetibles o duplicados. No comentamos las líneas de código porque no generan un error como tal, pero si vemos la impresion que genera en este punto veremos que aunque agregamos un elemento (ya existente como Moisés), no agrega uno más ya que este ya existe...
my_other_set.add("Moisés")
print(my_other_set)

print("________in___________")
# Podemos realizar búsqueda de elementos o comprobar si existe un elemento en el set mediante "in"
exist_in_set = "Moisés" in my_other_set
exist_in_set_second = "Moises" in my_other_set
print(exist_in_set)
print(exist_in_set_second)
# Podriamos consultarlo de forma directa sin utilizar variables
print(33 in my_other_set)
print("Hernandez" in my_other_set) # Porque arroja false??? Porque "Hernandez" esta sin acento en la "a" y no es lo mismo "Hernandez" que "Hernández"

print("________remove___________")
# Podemos eliminar datos o elementos de un set con la funcion remove()
print(my_other_set)
my_other_set.remove(33)
print(my_other_set)

print("________clear___________")
# Con clear al igual que en las listas y tuplas conseguimos limpiar, vaciar el set de los elementos almacenados en el
my_other_set.clear()
print(my_other_set) # Ahora tenemos un set vacio, sin ningun dato o elemento
print(len(my_other_set)) # Comprobamos que no tenemos ningun dato o elemento almacenado en el set

print("________del___________")

del my_other_set # Como ya lo mencionamos anteriormente, "del" es una función del sistema propio y elimina no el valor ni el dato, si no la variable como tal

print("___________________")
# Convertimos un set en una lista. Esto no es para nada recomendable sobre todo si vamos a trabajar con los indices de los elementos, ya que aunque va a pasar a ser una lista, el codigo como tal siempre que corra va a leer de entrada que es un set en primera instancia y los indices van a cambiar y estar variando cada vez que se corra el programa
my_set = {"Honda", "CBR", 600, "RR"}
my_list = list(my_set)
print(my_list)
print(type(my_list))
print(my_list[1])

my_other_set = {"Python", "JavaScript", "C++"}

print("________union___________")
# Union nos permite unir o juntar un set con otro
my_new_set = my_set.union(my_other_set)
print(my_new_set)

""" 
    my_new_set = my_set.union(my_other_set).union(my_new_set).union(my_set).union(my_other_set)

    Podemos juntar mas de uno, pero si llegamos a juntar uno que ya habiamos juntado anteriormente los elementos no se van a duplicar ya que recordemos que el set no admite datos o elementos repetidos ni duplicados
"""

print(my_new_set.union({"Swift", "React-Native", "Go"})) # Hay que tener cuidado cuando vayamos a usar "union" o cualquier otra función de forma directa en el codigo, sin antes guardarla en una variable, ya que se nos puede pasar poner los signos correspondientes, como en este caso las llaves. En un inicio se me paso ponerlas y estaba agregando los elementos letra por letra, parecia una lista, pero no tenia mucho sentido ya que al estar entre comillas cada elemento, aun estando como lista cada palabra dentro de comillas deberia de haber sido un dato, sin embargo no entiendo porque estaba haciendo ese efecto y no encontraba el problema, y el problema era que se me habia pasado poner las llaves. Asi que hay que tener mucho cuidado con este tipo de cosas...

print("________difference___________")
# La funcion difference nos muestra que elementos tiene el set al que se le asigno la funcion difference en comparación con el set que esta dentro de los parentesis de la funcion
print(my_new_set.difference(my_set))