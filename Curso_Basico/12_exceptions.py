# --- EXCEPTIONS HANDLING (MANEJO DE ERRORES) ---

# El manejo de excepciones/errores sirve para tratar de controlar que nuestro programa no se muera si es que llegase a tener algun error de cualquier tipo

""" 
    Si queremos controlar un error lo tenemos que hacer mediante un 'try'
    
    El diagrama es el siguiente:
    
    try:
        <<< Run code >>>
    except: (Puede o no puede tener un tipo de error en concreto)
        Ejecuta este código cuando haya una excepción o error, cualquiera de los dos que sea el caso
    else:
        Si no hay excepciones o errores ejecuta este código
    finally:
        Siempre ejecuta este bloque de código (este código se ejecuta pase lo que pase. Haya una excepción o no el bloque de finally se ejecuta)
        
    TANTO EL ELSE COMO EL FINALLY SON OPCIONALES, SI QUEREMOS O NECESITAMOS PODEMOS HACER USO DE ELLOS, PERO ASI MISMO PODEMOS PRESCINDIR DE ELLOS
    
    El "except" se va a ejecutar cuando haya una excepción o error. Sin embargo no necesariamente tiene que haber un error para que se ejecute. Puede ser meramente una excepción en la ejecución del código, vaya, algo que no se ejecuta en el try, pero que no genera algun error.
    
    El "else" solo se ejecuta si no hay una excepción/error, es decir que el código no pase por el "except"
    
    El "finally" se ejecuta siempre. Es decir ya sea que el codigo pase por el except o el else el finally si o si se va a ejecutar
        
    Estos bloques nosotros los tenemos que definir
"""

number_one = 5
number_two = 3
print(number_one + number_two)

number_two = '3'

# Inicio pruebas de try por mi cuenta antes de ver el video relacionado con el tema

print('*************************************************************')

try:
    number_one + number_two
except: # Se ejecuta cuando haya una excepción/error
    if type(number_one) or type(number_two) != int:
        print('Tipo de dato erroneo. No se pueden sumar')
else: # Se ejecuta cuando NO haya una excepción/error
    if type(number_one) and type(number_two) == int:
        suma_datos = number_one + number_two
        print(f'El resultado de la suma es: {suma_datos}')
finally: # Se ejecuta siempre
    print('Ejecución finalizada')

print('*************************************************************')
    
try:
    number_one + number_two
except:
    if type(number_one) or type(number_two) != int: # Probablemente pueda ahorrarme esta linea de código
        if type(number_one) != int:
            print(f'Tipo de dato erroneo, (dato: {number_one}, tipo: {type(number_one)}). Generando cambio del tipo de dato.')
            number_one = int(number_one)
            # print(type(number_one))
            print('.............................100%.............................')
        if type(number_two) != int:
            print(f'Tipo de dato erroneo (dato: {number_two}, tipo: {type(number_two)}). Generando cambio del tipo de dato.')
            number_two = int(number_two)
            # print(type(number_two))
            print('.............................100%.............................')    
else:
    print('Tipos de datos correctos. Generando la operación aritmética')
finally:
    suma_datos = number_one + number_two
    print(f'El resultado de la suma es: {suma_datos}')
    print('Ejecución finalizada')
    
# Fin de las pruebas del try realizadas por cuenta propia antes de ver el tema. Pruebas realizadas con éxito

print('*************************************************************')

num_one = 9
num_two = 5

try:
    print(num_one + num_two)
except:
    if type(num_one) != int:
        print(f'Tipo de dato erroneo, (dato: {num_one}, tipo: {type(num_one)}).')
    if type(num_two) != int:
        print(f'Tipo de dato erroneo (dato: {num_two}, tipo: {type(num_two)}).')  
else:
    print('Tipos de datos correctos. Operación aritmética realizada')
finally:
    print('Ejecución finalizada')
    
print('*************************************************************')

num_one = '9'

try:
    print(num_one + num_two)
except:
    if type(num_one) != int:
        print(f'Tipo de dato erroneo, (dato: {num_one}, tipo: {type(num_one)}).')
    if type(num_two) != int:
        print(f'Tipo de dato erroneo (dato: {num_two}, tipo: {type(num_two)}).')  
else:
    print('Tipos de datos correctos. Operación aritmética realizada')
finally:
    print('Ejecución finalizada')
    
print('*************************************************************')

# EXCEPCIONES POR TIPO DE ERROR

try:
    print(num_two + num_one)
    print('Ejecución realizada con éxito')
except ValueError:
    print('Se ha producido un ValueError')
except TypeError:
    print('Se ha producido un TypeError')
    
print('*************************************************************')
    
# CAPTURA DE LA INFORMACION DE LA EXCEPCION/ERROR

try:
    print(num_two + num_one)
    print('Ejecución realizada con éxito')
except ValueError as error:
    print('Se ha producido un error Value')
    print(error)
except TypeError as error:
    print('Se ha producido un error Type')
    print(error)
    
print('*************************************************************')

# EXCEPTION -> El exception nos sirve para capturar cualquier tipo de error y se utiliza para capturar la información del error

# En las siguientes lineas de codigo tenemos un error de tipo TypeError, por lo tanto si quitaramos el Exception el programaria fallaría ya que ese tipo de error no estaría controlado, el ValueError no nos valdría, pero con el Exception controlamos ese error de tipo TypeError o cualquier otro

try:
    print(num_two + num_one)
    print('Ejecución realizada con éxito')
except ValueError as error:
    print('Se ha producido un error Value')
    print(error)
except Exception as error:
    print('Se ha producido un error')
    print(error)