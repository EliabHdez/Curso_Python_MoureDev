# --- Higher Order Functions / Funciones de Orden Superior ---

# Las funciones de orden superior las podemos entender como funciones que tienen dentro otras funciones y que al llamar a la funcion superior se ejecutan las funciones que esta contiene en su interior

def sum_one(value):
    return value + 1

def sum_five(value):
    return value + 5

# LA SIGUIENTE ES UNA FUNCION DE ORDEN SUPERIOR

# La función de orden superior la estamos ocupando como una función base para que ejecute diferentes funciones, pero siempre basandonos en la función principal

def sum_values_more_function(first_value, second_value, f_sum):
    return f_sum(first_value + second_value)

def sum_values_more_function(first_value, second_value, f_sum):
    return f_sum(first_value + second_value)

print(sum_values_more_function(5, 2, sum_one)) # El valor que recibe la función sum_one es el resultado de la suma de first_value + second_value

print(sum_values_more_function(5, 2, sum_five)) # El valor que recibe la función sum_five es el resultado de la suma de first_value + second_value

# CLOSURES

# Los closures lo podemos entender como una función que retorna una función

# En los closures tambien tenemos una función de orden superior

# Este primer ejemplo es el realizado en el tutorial por Brais, donde retorna la función a secas, guardamos la función general en una variable y al momento de imprimir esta variable a esta le asignamos el valor de la función interna

def sum_ten():
    def add(num):
        return num + 10
    return add

add_closure = sum_ten()
print(add_closure(5))

# El siguiente ejemplo fue realizo por mi para hacer una prueba donde pude confirmar que al retornar la función interna ahi mismo le podemos pasar el valor de la función y posteriormente ejecutar la función principal

def sum_ten():
    def add(num):
        return num + 10
    return add(5)

print(sum_ten())

def sum_ten(or_value):
    def add(num):
        return num + 10 + or_value
    return add

print(sum_ten(5)(3))

# No es lo mismo el return de la función interna que el return que ejecuta la función principal. 

# En el primer ejemplo la función interna retorna la suma de los valores, pero este no lo vemos por ningun lado ya que no lo estamos guardando, imprimiendo ni llamando a la función interna, por lo tanto si lo retorna por que a fin de cuentas el codigo se ejecuta, la función hace lo suyo pero no lo tenemos visible por ningun lado. Lo que vemos es el valor de original_value ya que este es el que retornamos de la función general y esta si la estamos llamando e incluso la estamos imprimiendo

print('--- Ejemplo 1 ---')

def sum_ten(original_value):
    def add(num):
        return num + 10 + original_value
    return original_value

print(sum_ten(3))

# Mientras que en el ejemplo 2 estamos retornando la función interna que a su vez esta retorna la suma de los elementos o valores tanto los que le tenemos que pasar a la funciones como los que estan declarados dentro de las mismas

# A que vamos con esto? Que cada retorn se ejecuta y devuelve lo pertinente en base a la función a la que pertenece

print('--- Ejemplo 2 ---')

def sum_ten(original_value):
    def add(num):
        return num + 10 + original_value
    return add(5)

print(sum_ten(1))

# Higher Order Functions -> Funciones de orden superior incluidas en el propio Python

# Built-in

print('--- Map ---')

# Map -> La función de orden superior map requiere un objeto iterable y el resultado es que map genera de un iterable otro iterable en función del codigo que tenga la función que le hemos pasado en sus parámetros

numbers = [2, 5, 10, 16]

def multiply(number):
    return number * 2

return_map = list(map(multiply, numbers))
print(return_map)

print('--- Lambda en map ---')

# Uso de lambdas en el map

numbers = [3, 6, 9, 13]

return_map = list(map(lambda number: number * 2, numbers))
print(return_map)

print('--- Filter ---')

# Filter -> La función de orden superior map requiere un objeto iterable y lo que basicamente hace es un filtrado en base al codigo de la función que le pasemos en sus parámetros. El filter ocupar el true y el false para poder filtrar lo que va a devolver en el objeto iterador que va a crear como resultado

numbers = [3, 6, 9, 13, 5, 11, 8, 24]

def greater_than(number):
    if number > 10:
        return True
    return False

return_filter = list(filter(greater_than, numbers))
print(return_filter)

def greater_than(number):
    if number > 10:
        return True
    # return False

return_filter = list(filter(greater_than, numbers))
print(return_filter)

def greater_than(number):
    if number > 10:
        return False
    return True

return_filter = list(filter(greater_than, numbers))
print(return_filter)

print('--- Mas simplificado ---')

# Todo lo anterior es lo mismo que...

def greater_than(number):
    return number > 10 # El True ya esta implicito en la condición, si es mayor es True, si no es mayor es False

return_filter = list(filter(greater_than, numbers))
print(return_filter)

print('--- Mini practica ---')

# Filtrar números pares e impares

def par(num_par):
    if num_par % 2 == 0:
        return True
    
return_filter = list(filter(par, numbers))
print(return_filter)

def impar(num_impar):
    if num_impar % 2 == 0:
        return False
    return True
    
return_filter = list(filter(impar, numbers))
print(return_filter)

# Ooooo... lo que seria lo mismo que...

def impar(num_impar):
    if num_impar % 2 != 0:
        return True
    
return_filter = list(filter(impar, numbers))
print(return_filter)
    
# Ooooo... lo que seria lo mismo que...

def par(num_par):
    return num_par % 2 == 0
    
return_filter = list(filter(par, numbers))
print(return_filter)

print('--- Lambda en filter ---')

# Uso de lambdas en el filter

numbers = [3, 6, 9, 13, 5, 11, 8, 24]

return_filter = list(filter(lambda num: num > 10, numbers))
print(return_filter, '-> Mayores que 10')

return_filter = list(filter(lambda num: num < 10, numbers))
print(return_filter, '-> Menores que 10')

return_filter = list(filter(lambda num: num % 2 == 0, numbers))
print(return_filter, '-> Números pares')

return_filter = list(filter(lambda num: num % 2 != 0, numbers))
print(return_filter, '-> Números impares')

print('--- Reduce ---')

# La función reduce si bien ya esta integrada en el lenguaje como tal, esta en un modulo independiente el cual tenemos que importar

from functools import reduce

# Reduce -> La función reduce de igual manera necesita un objeto iterable y con este lo que hace al menos en el siguiente ejemplo es ir reduciendo la cantidad de elementos del iterable mediante la suma del primer valor con el segundo valor. El resultado de la suma de los dos primeros valores pasa a ser el primer valor, lo suma con el segundo y asi sucesivamente hasta llegar al final del objeto iterable

nums = [2, 4, 6, 8, 10]

def sum_values(first, second):
    return first + second

print(reduce(sum_values, nums))

print('--- Lambda en reduce ---')

# Lambdas en reduce

print(reduce(lambda one, two: one + two, nums))