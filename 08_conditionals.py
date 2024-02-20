# --- CONDITIONALS ---

# Los condicionales como su nombre lo indican condicionan acciones que dependiendo de la condición que se declare sera lo que el programa ejecutara...

# Para que el código de una condición se ejecute esta tiene que ser verdadera (True), si es falsa no se va a ejecutar el código

# Si tenemos varias condiciones, se va a saltar en las que la condición no se cumpla, es decir que sea falsa y va a irse a la condición que si se cumpla, es decir que sea verdadera

print("________Condición verdadera___________")

my_condition = True

if my_condition:
    print("Se ejecuta la condición del if")
    
print("Se ejecutó la condición")

print("________Condición falsa___________")

my_condition = False

if my_condition:
    print("Este print no se va a ejecutar")
    
print("No se ejecto la condión del if con la variable que tiene como valor False, por lo tanto no se tiene que ver el print que dice 'Este print no se va a ejecutar'")

my_condition_number = 5 * 2

if my_condition_number:
    print("Condición numerica cumplida")
    
print("Condición numerica sin limite en la condición cumplida")

# Esta condición puede que sea algo confusa porque esta corriendo el programa y no tenemos ningun error y lo confuso puede estar en que la condición no esta igualado a nada, por lo tanto podemos decir "como se cumple una condición si no se esta igualando a algo para que haya una comparativa y se pueda haber un resultado verdadero o falso". El punto es que mientras haya un valor que en este caso es una variable con ese valor a Python le vale, la condición es meramente el valor de la variable

print("________Condición igualada o con limite___________")

print("________Condición igualada verdadera___________")

my_condition_number = 5 * 2

if my_condition_number == 10:
    print("Se esta cumpliendo la condición igualada")
    
print("Condición cumplida. La variable tiene el mismo valor (10) que el valor con el que se le comparo")

print("________Condición igualada falsa___________")

if my_condition_number >= 11:
    print("Se esta cumpliendo la condición igualada")
    
print("Condición NO cumplida. La variable no tiene el mismo valor (10) que el valor con el que se le comparo. El valor de la variable no es igual ni mayor que 11")

print("________Condicional else___________")
# El condicional else viene siendo una traducción a "si no", y este se ocupa para darle una segunda condición al if, por decirlo de alguna manera es limitativo porque o se cumple la condición del if o se cumple la condición del else, no hay mas, es cualquiera de las dos

if my_condition_number > 10:
    print("El valor de la variable es mayor de 10")
else:
    print("El valor de la variable es menor o igual que 10")
    
print("________Condicionales con operadores logicos___________")
    
# Podemos hacer de los operadores logicos dentro de condicionales para dar mas de una condición a cumplir ya se que queramos que se cumpla una de todas, algunas o directamente todas

print("________I___________")
my_condition_number = 6 * 3

if my_condition_number > 10 and my_condition_number < 20:
    print("El valor de la variable esta dentro del rango")
    print(f"El valor de la variable es {my_condition_number}")
else:
    print("El valor de la variable esta FUERA de rango. Es menor o igual que 10 o igual o mayor que 20")
    print(f"El valor de la variable es {my_condition_number}")

print("________II___________")
my_condition_number = 5 * 5

if my_condition_number > 10 and my_condition_number < 20:
    print("El valor de la variable esta dentro del rango")
    print(f"El valor de la variable es {my_condition_number}")
else:
    print("El valor de la variable esta FUERA de rango. Es menor o igual que 10 o igual o mayor que 20")
    print(f"El valor de la variable es {my_condition_number}")
    
print("________Condicional elif___________")
# El condicional elif es una mezcla del if y el else, en otra palabras se puede traducir como "si no es esto, pero si es esto". Este da mas rango de opciones o condiciones ya que se pueden poner cuantos nosotros queramos y el programa va a ir evaluando condición por condición empezando por el if, seguido de los elif que tengamos hasta concluir con el último o con el else si es que lo hay o hasta que una condición se cumpla

print("________I___________")
my_condition_number = 15

if my_condition_number > 12 and my_condition_number < 17:
    print("La edad esta dentro del rango. Tiene la edad suficiente")
    print(f"La edad es de {my_condition_number} años")
elif my_condition_number < 12:
    print("La edad esta FUERA de rango. Es menor de 12 años. No cubre la edad")
    print(f"La edad es de {my_condition_number} años")
elif my_condition_number > 17 and my_condition_number <= 23:
    print("La edad esta FUERA de rango. Es mayor de 17 años. Sobrepasa la edad. Evaluar contratación")
    print(f"La edad es de {my_condition_number} años")
elif my_condition_number == 12:
    print("La edad esta en el mínimo aceptable")
    print(f"La edad es de {my_condition_number} años")
elif my_condition_number == 17:
    print("La edad esta en el límite aceptable")
    print(f"La edad es de {my_condition_number} años")
else:
    print("Candidato No viable. La edad supera los 23 años")
    print(f"La edad es de {my_condition_number} años")

print("________II___________")    
my_condition_number = 10

if my_condition_number > 12 and my_condition_number < 17:
    print("La edad esta dentro del rango. Tiene la edad suficiente")
    print(f"La edad es de {my_condition_number} años")
elif my_condition_number < 12:
    print("La edad esta FUERA de rango. Es menor de 12 años. No cubre la edad")
    print(f"La edad es de {my_condition_number} años")
elif my_condition_number > 17 and my_condition_number <= 23:
    print("La edad esta FUERA de rango. Es mayor de 17 años. Sobrepasa la edad. Evaluar contratación")
    print(f"La edad es de {my_condition_number} años")
elif my_condition_number == 12:
    print("La edad esta en el mínimo aceptable")
    print(f"La edad es de {my_condition_number} años")
elif my_condition_number == 17:
    print("La edad esta en el límite aceptable")
    print(f"La edad es de {my_condition_number} años")
else:
    print("Candidato No viable. La edad supera los 23 años")
    print(f"La edad es de {my_condition_number} años")

print("________III___________")    
my_condition_number = 22

if my_condition_number > 12 and my_condition_number < 17:
    print("La edad esta dentro del rango. Tiene la edad suficiente")
    print(f"La edad es de {my_condition_number} años")
elif my_condition_number < 12:
    print("La edad esta FUERA de rango. Es menor de 12 años. No cubre la edad")
    print(f"La edad es de {my_condition_number} años")
elif my_condition_number > 17 and my_condition_number <= 23:
    print("La edad esta FUERA de rango. Es mayor de 17 años. Sobrepasa la edad. Evaluar contratación")
    print(f"La edad es de {my_condition_number} años")
elif my_condition_number == 12:
    print("La edad esta en el mínimo aceptable")
    print(f"La edad es de {my_condition_number} años")
elif my_condition_number == 17:
    print("La edad esta en el límite aceptable")
    print(f"La edad es de {my_condition_number} años")
else:
    print("Candidato No viable. La edad supera los 23 años")
    print(f"La edad es de {my_condition_number} años")

print("________IV___________")    
my_condition_number = 12

if my_condition_number > 12 and my_condition_number < 17:
    print("La edad esta dentro del rango. Tiene la edad suficiente")
    print(f"La edad es de {my_condition_number} años")
elif my_condition_number < 12:
    print("La edad esta FUERA de rango. Es menor de 12 años. No cubre la edad")
    print(f"La edad es de {my_condition_number} años")
elif my_condition_number > 17 and my_condition_number <= 23:
    print("La edad esta FUERA de rango. Es mayor de 17 años. Sobrepasa la edad. Evaluar contratación")
    print(f"La edad es de {my_condition_number} años")
elif my_condition_number == 12:
    print("La edad esta en el mínimo aceptable")
    print(f"La edad es de {my_condition_number} años")
elif my_condition_number == 17:
    print("La edad esta en el límite aceptable")
    print(f"La edad es de {my_condition_number} años")
else:
    print("Candidato No viable. La edad supera los 23 años")
    print(f"La edad es de {my_condition_number} años")

print("________V___________")    
my_condition_number = 17

if my_condition_number > 12 and my_condition_number < 17:
    print("La edad esta dentro del rango. Tiene la edad suficiente")
    print(f"La edad es de {my_condition_number} años")
elif my_condition_number < 12:
    print("La edad esta FUERA de rango. Es menor de 12 años. No cubre la edad")
    print(f"La edad es de {my_condition_number} años")
elif my_condition_number > 17 and my_condition_number <= 23:
    print("La edad esta FUERA de rango. Es mayor de 17 años. Sobrepasa la edad. Evaluar contratación")
    print(f"La edad es de {my_condition_number} años")
elif my_condition_number == 12:
    print("La edad esta en el mínimo aceptable")
    print(f"La edad es de {my_condition_number} años")
elif my_condition_number == 17:
    print("La edad esta en el límite aceptable")
    print(f"La edad es de {my_condition_number} años")
else:
    print("Candidato No viable. La edad supera los 23 años")
    print(f"La edad es de {my_condition_number} años")

print("________VI___________")    
my_condition_number = 25

if my_condition_number > 12 and my_condition_number < 17:
    print("La edad esta dentro del rango. Tiene la edad suficiente")
    print(f"La edad es de {my_condition_number} años")
elif my_condition_number < 12:
    print("La edad esta FUERA de rango. Es menor de 12 años. No cubre la edad")
    print(f"La edad es de {my_condition_number} años")
elif my_condition_number > 17 and my_condition_number <= 23:
    print("La edad esta FUERA de rango. Es mayor de 17 años. Sobrepasa la edad. Evaluar contratación")
    print(f"La edad es de {my_condition_number} años")
elif my_condition_number == 12:
    print("La edad esta en el mínimo aceptable")
    print(f"La edad es de {my_condition_number} años")
elif my_condition_number == 17:
    print("La edad esta en el límite aceptable")
    print(f"La edad es de {my_condition_number} años")
else:
    print("Candidato No viable. La edad supera los 23 años")
    print(f"La edad es de {my_condition_number} años")
    
# Las variables vacias tienen el valor de False

string_one = ""

if string_one:
    print("Mi cadena de texto NO está vacía") # Aquí esto no se va a imprimir porque la condición no se cumple, ya que la cadena de texto si está vacía. Por lo tanto la condición es False. Recordar que una cadena de texto vacía adopta el tipo de dato booleano False
    print(f"El texto dice: {string_one}")
    
# Ocupando en operador lógico "not"

string_one = ""

if not string_one:
    print("Mi cadena de texto SI está vacía") # Aquí ya se cumple la condición porque aunque la cadena de texto siga vacia, estamos haciendo uso del operador lógico not que es negación, el cual cambia el valor booleano al opuesto... True -> False y False -> True
    print(f"El texto dice: {string_one}")
    
# Y viceversa con una cadena de texto llena

string_one = "Katana es una gorda traviesa"

if string_one:
    print("Mi cadena de texto NO está vacía")
    print(f"El texto dice: {string_one}")
    
# Ocupando en operador lógico "not"

string_one = "Katana es una gorda traviesa"

if not string_one:
    print("Mi cadena de texto SI está vacía")
    print(f"El texto dice: {string_one}")
    
print("**************************************************")
print("La ejecución continúa fuera de los condicionales")