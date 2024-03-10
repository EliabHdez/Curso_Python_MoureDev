# --- OPERADORES ---

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

print(3 > 4)
print(3 < 4)
print(3 >= 4)
print(3 <= 4)
print(3 == 4)
print(3 != 4)
print(3 > 4 == 2)
print(3 < 4 > 2) # Se pueden comparar varios datos al mismo tiempo utilizando varios operadores en la misma linea, aunque no entiendo del todo el resultado y como hace la comparación...

print("___________________")
print("Hola" > "Python")
print("Hola" < "Python")
print("Hola" >= "Python")
print("Hola" <= "Python")
print("Hola" == "Python")
print("Hola" != "Python")

# Con strings o cadenas de texto lo que comparan los operadores comparativos es una ordenación alfabética de las letras

# Hay que tener en cuenta que si hace diferencia entre mayúsculas y minúsculas al momento de la comparativa

### ORDENACION ALFABÉTICA POR ASCII ###

print("___________________")
print("Hola" == "Hola")
print("Hola" == "Xbox")
print("Hola" >= "Xbox")
print("Hola" <= "Xbox")
print("Hola" == "Bola")
print("Hola" >= "Bola")

print("___________________")
print("Hola" == "Ilmo")
print("Hola" >= "Ilmo")
print("Hola" <= "Ilmo")

print("___________________")
print("Hola" == "Gato")
print("Hola" >= "Gato")
print("Hola" <= "Gato")

print("___________________")
print("Hola" == "Gula")
print("Hola" >= "Gula")
print("Hola" <= "Gula")

print("___________________")
print("aaaa" == "aaaa")
print("aaaa" >= "abaa")
print("aaaa" <= "aaba")

print("___________________")
print("AAAA" >= "aaaa")
print("aaaa" >= "AAAA")
print("aaaa" <= "AAAA")
print("AAAA" == "aaaa")

# NO hay que confundirse y creer que compara el número de caractéres de los strings, para eso necesitariamos hacer uso del metodo len()

print("___________________")
print(len("Hola") >= len("Python"))
print(len("Hola") <= len("Python"))
print(len("Hola") == len("Python"))

print("___________________")
print(len("Hola") > len("Xbox"))
print(len("Hola") < len("Xbox"))
print(len("Hola") >= len("Xbox"))
print(len("Hola") <= len("Xbox"))
print(len("Hola") == len("Xbox"))

print("___________________")
print(len("aaaa") > len("aaba"))
print(len("aaaa") < len("aaba"))
print(len("aaaa") >= len("aaba"))
print(len("aaaa") <= len("aaba"))
print(len("aaaa") == len("aaba"))

# OPERADORES LÓGICOS

"""
    Existen 3 operadores lógicos: 'and', 'or' y 'not'
    
    - and
        True + True = True
        True + False = False
        False + False = False
        
    - or
        True + True = True
        True + False = True
        False + False = False
        
    - not
        Negación: Cambia el valor booleano por el contrario, es decir si es True le dice que no es True y pasa a ser False y visceversa
        
    Si en una sola comparativa hay varios datos a comparar ya sea con iguales o diferentes operadores logicos aplican las mismas reglas de cada uno de los operadores logicos. Y esta la hace en orden de los operadores logicos da igual si el and o el or esta uno antes que el otro. Donde pudiera llegar a cambiar seria si encerramos una comparativa entre parentésis, lo cual forzaria al programa a hacer esta comparativa que esta dentro de los parentésis primero para posteriormente hacer la que se encuentre afuera
"""

print("________and___________")
print(3 < 4 and "Hola" < "Python")
print(3 > 4 and "Hola" < "Python")
print(3 > 4 and "Hola" > "Python")

print("________or___________")
print(3 < 4 or "Hola" < "Python")
print(3 < 4 or "Hola" > "Python")
print(3 > 4 or "Hola" > "Python")

print(3 < 4 or "Hola" > "Python" and 9 < 4)
print(3 > 4 and "Hola" < "Python" or 9 > 4)
print(3 > 4 or "Hola" > "Python" and 4 == 4)
print(3 < 4 or ("Hola" > "Python" and 4 == 4)) # Con los paréntesis al igual que en las operaciones matemáticas estamos indicandole prioridad con respecto a que tiene que comparar primero
print(3 < 4 or ("Hola" > "Python" and 4 != 4))

print("________not___________")
print(not(3 > 4)) # Se aplica la negación al resultado correcto. 3 no es mayor que 4, pero al tener el operador not, le estamos diciendo que ese False no es correcto y cambia a True
print(not(3 < 4))