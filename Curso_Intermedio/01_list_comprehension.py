# --- LIST COMPREHENSION ---

# La comprension de lista la podriamos definir como una estructura que nos permite trabajar con listas de una manera mas amplia, es una manera de crear listas nuevas utilizando diferentes herramientas o recursos del propio lenguajes, como pueden ser funciones, rangos, condicionales etc. Vamos a poner algunos ejemplos haber si con eso se entiende un poco mejor

or_list = [1, 2, 3, 5, 6]
print(or_list)

my_range = range(8)
print(list(my_range))

# Apartir de este punto ya podemos ver lo que podriamos decir que es el 'list comprehension'. Una forma de crear listas pero utilizando mas funciones que nos permiten hacer con las listas muchas cosas

list_comp = [i + 1 for i in or_list]
print(list_comp)

def mult(number):
    return number * 5

list_comp = [mult(i) for i in or_list]
print(list_comp)

def mult(number):
    return number + 6

list_comp = [mult(i) for i in list(my_range)]
print(list_comp)

# Supongamos que la lista original ahora la tenemos que ampliar hasta el numero 90. Para hacerlo de forma manual pues tendriamos que modificarla y agregarle uno a uno los numeros faltantes para llegar hasta el 90, sin embargo con esta forma de trabajar con las listas lo podemos de hacer de una manera mas sencilla y rapida

or_list = [1, 2, 3, 5, 6]

or_list = [element + 1 for element in list(range(90))]
print(or_list)

print('----- Numbers -----')

def multiplos_diez(number):
    if number % 10 == 0:
        return 'N/A'
    else:
        return number
        
or_list = [multiplos_diez(i) for i in or_list]
print(or_list)

print('----- N/A -----')

or_list = [element + 1 for element in list(range(90))]

def multiplos_diez(number):
    if number % 10 == 0:
        return number
    else:
        return 'N/A'
        
or_list = [multiplos_diez(i) for i in or_list]
print(or_list)