# --- CHALLENGES ---

""" 
    El famoso "Fizz Buzz"
    
    Escribe un programa que muestre por consola (con un print) los numeros del 1 al 100
    (ambos incluidos y con un salto de línea entre cada impresión), sustituyendo los siguientes:
    
    - Multiplos de 3 por la palabra "fizz"
    - Multiplos de 5 por la palabra "buzz"
    - Multiplos de 3 y 5 a la vez por la palabra "fizzbuzz"
"""

# numeracion = 0

# while numeracion < 100:
#     numeracion += 1
#     if numeracion % 3 == 0 and numeracion % 5 == 0:
#         print('fizzbuzz')
#     elif numeracion % 3 == 0:
#         print('fizz')
#     elif numeracion % 5 == 0:
#         print('buzz')
#     else:
#         print(numeracion)
        
def fizzbuzz(num):
    conteo_fizzbuzz = 0
    conteo_fizz = 0
    conteo_buzz = 0
    while num < 100:
        num += 1
        if num % 3 == 0 and num % 5 == 0:
            print('fizzbuzz')
            conteo_fizzbuzz += 1
        elif num % 3 == 0:
            print('fizz')
            conteo_fizz += 1
        elif num % 5 == 0:
            print('buzz')
            conteo_buzz += 1
        else:
            print(num)
    print(f'Fizzbuzz = {conteo_fizzbuzz}\nFizz = {conteo_fizz}\nBuzz = {conteo_buzz}')
        
# fizzbuzz(0)

def fizzbuzz_2():
    conteo_fizzbuzz = 0
    conteo_buzz = 0
    conteo_fizz = 0
    for element in range(1, 101):
        if element % 3 == 0 and element % 5 == 0:
            print('fizzbuzz')
            conteo_fizzbuzz += 1
        elif element % 3 == 0:
            print('fizz')
            conteo_fizz += 1
        elif element % 5 == 0:
            print('buzz')
            conteo_buzz += 1
        else:
            print(element)
    print(f'Fizzbuzz = {conteo_fizzbuzz}\nFizz = {conteo_fizz}\nBuzz = {conteo_buzz}')
            
# fizzbuzz_2()

""" 
    "Anagrama"
    
    Crea un programa que compare dos palabras o frases e indique si es una anagrama o no
"""

def anagram(word_one, word_two):
    word_one = sorted(word_one.lower().replace(' ',''))
    word_two = sorted(word_two.lower().replace(' ',''))
    if word_one == word_two:
        print('Las palabras/frases son "anagramas"')
    else:
        print('Las palabras NO son anagramas')

# anagram('Amor', 'Roma')
# anagram('sesos', 'Besos')
# anagram('rata', 'atar')
# anagram('Moto', 'mato')
# anagram('The Alias Men', 'Alan Smithee')
# anagram('Tom Marvolo Riddle', 'I am Lord Voldemort')

""" 
    "Serie Fibonacci"
    
    Escribe un programa que imprima los primeros 50 números de la sucesión de Fibonacci, empezando en cero. La serie Fibonacci se compone por una sucesión de números en la que el siguiente siempre es la suma de los dos anteriores...
        0, 1, 1, 2, 3, 5, 8, 13...
"""

# Solución de Brais

def fibonacci():
    
    prev = 0
    actual = 1
    
    for e in range(0, 50):
        print(prev)
        fib = prev + actual
        prev = actual
        actual = fib
    
# fibonacci()

# Mi solución. No logre concretarla porque me fallaron las operaciones y como organizar dichas operaciones en variables y todo eso, pero la lógica y el procedimiento que queria aplicar era el correcto

def fibonacci_dos():
    
    prev = 0
    actual = 1
    count = 0
    
    while count < 50:
        print(prev)
        fib = prev + actual
        prev = actual
        actual = fib
        count += 1
        
# fibonacci_dos()

""" 
    "Numero Primo"
    
    Escribe un programa que se encargue de comprobar si un número es primo o no. Hecho esto, imprime los números primos entre 1 y 100
"""

# Cabe mencionar que no entendi el codigo de este ejercicio. No entiendo que hace la variable is_divisible, que papel juega y porque aunque no entra al if donde cambia su valor, por alguna razon llega al if del not con el valor de True para que con el not cambie a False

def prime_numbers():
    
    for num in range(1, 101):
        if num >= 2:
            is_divisible = False
            
            for element in range(2, num):
                if num % element == 0:
                    is_divisible = True
                    break
            # if is_divisible == False: Esto es lo equivalente a la linea de abajo
            if not is_divisible:
                print(num)
        
# prime_numbers()

""" 
    "Invirtiendo Cadenas de Texto"
    
    Crea un programa que invierta el orden de una cadena de texto sin usar funciones propias del lenguaje que lo hagan de forma automática
    
        Ej: 'Hola Mundo' -> 'odnuM aloH'
"""

print('----- Mis soluciones -----')

saludo = 'Hola Mundo'

def inv_without_functions(text):
    reverse_text = []
    for element in text:
        reverse_text.append(element)
    reverse_text.reverse()
    reverse_text = ''.join(reverse_text)
        
    return reverse_text

# print(inv_without_functions(saludo))

def inv(text):
    text = list(text)
    text.reverse()
    text = ''.join(text)
    print(text)
    
# inv(saludo)

def inv_manual(text):
    reversed_text = text[::-1]
    print(reversed_text)
        
inv_manual('Hola Mundo')

print('----- Solución Brais -----')

# Solución Brais

def reverse(text):
    text_len = len(text)
    reverse_text = ''
    for index in range(0, text_len):
        reverse_text += text[text_len - index - 1]
    return reverse_text

print(reverse(saludo))

# En este último estaba confundiendo el comportamiento de len(), pensando que estaba a contar desde 0, cuando no es así, len() cuenta el número de elementos, pero no empieza en 0, si no como tal en 1, por ejemplo la palabra 'Hola', tiene 4 elementos o caracteres, asi que si le pasamos el len arrojara 4. LO ESTABA CONFUNDIENDO CON EL INDEX, que es la posición de cada elemento y que este si que si empieza a contar dichas posiciones desde 0