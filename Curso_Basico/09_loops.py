# --- LOOPS/BUCLES/CICLOS ---

# Los loopes o bucles son mecanismos que son sirven para iterar (iterar = repetir). En otras palabras los loops nos sirven para pasar por el código varias veces

print("________while___________")

# BUCLE WHILE

my_condition = 0

while my_condition < 10:
    print(f'El valor de la variables es menor a 10. Valor = {my_condition}')
    my_condition += 2 # Esto es lo mismo que 'my_condition = my_condition + 2
    # Si no incrementamos el valor de la variable, el loop sería infinito, porque la variable siempre estaría valiendo "0" por lo tanto, este loop se repetiría de por vida, o hasta que la compu explote...
    print(my_condition)
else: # El condicional else tambien se puede ocupar con el while
    print(f"El valor de la variable es mayor o igual a 10. Valor = {my_condition}")
    
print('La ejecución de nuestro programa continúa...')

print(my_condition)

while my_condition < 20:
    my_condition += 1
    if my_condition == 15:
        print("Valor variable igual a 15")
    print(my_condition)
    
print("________break___________")

# El break nos sirve para detener la ejecución de un bucle, el break detendra la ejecución del bucle en el punto que lo declaremos aunque este en situaciones normales debiera seguirse ejecutando porque se siga cumpliendo la condición del bucle 

my_condition_second = 3

while my_condition_second < 20:
    my_condition_second += 3
    if my_condition_second == 15:
        print(my_condition_second)
        print(f"Se detiene la ejecución. Valor variable = {my_condition_second}")
        break # El bucle se detiene aquí y deja de ejecutarse aunque debería de continuar debido a que todavía hay mas numeros menores que 20 despúes del 15, pero como le declaramos el break, en el momento que llega aqui y se cumple la condición del if (que es a donde pertence el break) en este momento se detiene la ejecución y el ciclo del bucle
    print(my_condition_second)
else:
    print('No se cumplio la condición del if para poder ejecutar el break y el bucle while se ejecuto completo')
    
print("________for___________")
    
# BUCLE FOR

# Bucle for nos sirve para recorrer los datos o elementos de una estructura o dato en concreto como puede ser un string, lista, tupla, etc

print("________list___________")
my_list = [78, 69, 51, 35, 33]

for element in my_list:
    print(element)

print("________string___________")    
my_string = "Katana"

for element in my_string:
    print(element)
    
print("________tupla___________")

my_tuple = ("Moises", 'Hernandez', 33, 1.76)

for element in my_tuple:
    print(element)
    
print("________set___________")

my_consoles = {'PS1', 'PS2', 'PS4', 'Xbox 360', 'Xbox One'}

for element in my_consoles:
    print(element)
    
print("________dict___________")

my_moto = {'Tipo':'Moto', 'Marca':'Honda', 'Modelo':'CBR600RR', 'Cilindrada':600}

for element in my_moto:
    print(element)
    
for element in my_moto.values():
    print(element)
    # También podemos hacer uso del condicional "else" en el bucle for
else:
    print('El bucle "for" a finalizado')

print("________break___________")
# De igual manera podemos hacer uso del "break" para detener la ejecución del bucle en un momento en específico

for element in my_moto.values():
    print(element)
    if element == 'Honda':
        print(f'{element} es la marca de la moto')
        break # El "break" directamente acaba con el bucle for y se sale del bucle
else:
    print('Finalizado el bucle for') # Con el break vemos que este print que pertenece al condicional else no se ejecuta y eso es debido a que el condicional else se ejecuta después de que el bucle se haya ejecutado por completo. Si se detiene la ejecución del bucle con el break el condicional else ya no se ejecuta, debido a que el bucle no se ejecuto por completo
    
print("________continue___________")
# El "continue" sirve para que la ejecución del bucle continue. Sin embargo no le encuentro mucho sentido ya que la ejecución del bucle continua si no tiene un break. Si hay un "if" de por medio y no tiene declarada una acción a ejecutar después de la condición si tiene uso el continue ya que sin este marcaria error de sintaxis, pero si el "if" si tiene una acción que debe ejecutar no sirve de nada el continue ya que mientras no tenga un break el bucle continuara ejecutandose sin problema, y no le encuentro mucho sentido poner un "if" con una condición a cumplir sin que tenga una acción a ejecutar al haber cumplido la condición...

for element in my_moto.values():
    
    print(element)
    if element == 'Honda':
        # print(f'{element} es la marca de la moto')
        continue # El "continue" vuelve al "for" sin ejecutar lo que esta debajo
    print("Se ejecuta el if completo")
else:
    print('Finalizado el bucle for')

print("*****************************************")
print("Continuamos con la ejecución del programa")