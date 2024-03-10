# --- FUNCTIONS ---

# Las funciones se crean con la palabra reservada "def". La estructura para declarar una función es la siguiente: def nombre_funcion ():

# Las funciones pueden llevar parametros dentro de los paréntesis

# FUNCION SIMPLE

print("________función simple___________")

def name_function ():
    print("Esto es una función")
    
# Para ejecutar la funcion() es necesario llamarla...

name_function()

# FUNCION CON PARAMETROS

print("________función con parámetros___________")
# Pasando valores o parámetros dentro de los paréntesis

def add_values (first_value, second_value):
    print(first_value + second_value)
    
add_values(5, 13)
add_values(54969, 54715)
add_values("5", "7")
add_values("Moises ", "Hernandez")
add_values(1.4, 5.2)

# METODO RETURN

print("________sin return___________")

def add_values_second (first_value, second_value):
    first_value + second_value
    
resultado = add_values_second(10, 12)
print(resultado) # Nos imprime "None", ya que la función no retorna nada, solo se ejecuta

print("________con return___________")

def add_values_third (first_value, second_value):
   return first_value + second_value
    
resultado = add_values_third(10, 12)
print(resultado) # Nos returna el resultado. Cuando se usa el return, es necesario guardar lo que la función retorna en una variable

# INICIO FUNCION DE PRACTICA

""" nombre = input('Cuál es tu nombre? ').capitalize()
edad = input("¿Cuántos años tienes? ") """

# """ def com_values (name, age):
#     name = nombre
#     age = edad    
#     while name.isdigit() == True:
#         print("Nombre NO válido")
#         name = input("Escriba su nombre ")
#     while age.isdigit() == False:
#         print("Edad NO válida")
#         age = input("Por favor ingresa solo dígitos para capturar tu edad ")
#     age = int(age)
#     if age < 16:
#         no_apto = "El candidato NO es apto. No alcanza la edad mínima"
#         print(no_apto)
#     elif age >= 16:
#         apto = "El candidato SI es apto"
#         print(apto)
#     elif age >= 50:
#         no_apto_grande = "El candidato NO es apto. Sobrepasa la edad"
#         print(no_apto_grande) """
        
# """ def com_values (name, age):
#     name = nombre
#     age = edad    
#     while name.isdigit() == True:
#         print("Nombre NO válido")
#         name = input("Escriba su nombre ")
#     while age.isdigit() == False:
#         print("Edad NO válida")
#         age = input("Por favor ingresa solo dígitos para capturar tu edad ")
#     age = int(age)
#     def aptos ():
#         if age < 16:
#             datos_cand = f'{name} - {age} años. '
#             no_apto = "El candidato NO es apto. No alcanza la edad mínima"
#             print(datos_cand, no_apto)
#         elif age >= 16 and age < 50:
#             datos_cand = f'{name} - {age} años. '
#             apto = "El candidato SI es apto"
#             print(datos_cand, apto)
#         elif age >= 50:
#             datos_cand = f'{name} - {age} años. '
#             no_apto_grande = "El candidato NO es apto. Sobrepasa la edad"
#             print(datos_cand, no_apto_grande)
#     return name, edad """
    
""" def com_values (name, age):
    name = nombre
    age = edad    
    while name.isdigit() == True:
        print("Nombre NO válido")
        name = input("Escriba su nombre ")
    while age.isdigit() == False:
        print("Edad NO válida")
        age = input("Por favor ingresa solo dígitos para capturar tu edad ")
    age = int(age)
    return name, edad
        
com_values(nombre, edad)
datos_cand = com_values(nombre, edad)
# print(datos_cand)

nombre = datos_cand[0]
edad = int(datos_cand[1])

if edad < 16:
    no_apto = f'{nombre} - {edad} años. El candidato NO es apto. No alcanza la edad mínima requerida'
    print(no_apto)
elif edad >= 16 and edad < 50:
    apto = f'{nombre} - {edad} años. El candidato SI es apto para el puesto'
    print(apto)
elif edad >= 50:
    no_apto_grande = f'{nombre} - {edad} años. El candidato NO es apto. Sobrepasa la edad'
    print(no_apto_grande) """
    
# FIN FUNCION DE PRACTICA

# REORDENANDO LOS PARAMETROS DE LA FUNCION
    
print("________definiendo orden de los parametros___________")

def name_lastname (nombre, apellido):
    print(f'{nombre} {apellido}')
    
# Si no seguimos el orden de los parámetros en la llamada de la función, podemos rectificarlos y definirlos
name_lastname('Hernandez', 'Moises')
name_lastname(apellido='Hernandez', nombre='Moises') # Hemos reasignado el valor de los parametros de la función

# DEFAULT - PARAMETROS POR DEFECTO

print("________default - parametros por defecto___________")

def name_lastname_default (nombre, apellido, alias = 'Sin alias'):
    print(f'{nombre} {apellido}, {alias}')
    
name_lastname_default('Moises', 'Hernandez', 'Predator')
name_lastname_default('Moises', 'Hernandez')

def imp_texts (*text):
    for element in text:
        print(element)
    
imp_texts("Hola, como estás?", "Bien y tú???")

def imp_texts (*text):
    print(type(text))
    for element in text:
        print(element.upper())
        
imp_texts("Hola, como estás?", "Bien y tú???")