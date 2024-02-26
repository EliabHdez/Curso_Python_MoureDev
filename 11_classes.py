# --- CLASSES ---

# Las clases son un tipo de objeto que podemos crear o definir a nuestra medida

# Una buena práctica dentro del lenguaje y de los programadores de Python es escribir el nombre de las clases con CamelCase (la primer letra de cada palabra en mayúsculas, sin espacios y sin guiones bajos)

""" 
    - El parametro que se le pasa al 'self' lo podemos ver como la variable
    - El valor que se le pasa a la "variable" del self, es el dato que se guarda en esa variable
    - Y el self viene siendo como la manera de ligar esta "variable" y su "valor" a la clase. Es decir que estos parametros, valores y datos pertenecen a la clase...
    
    class Person:
    def __init__(self, firstname, lastname):
        self.name = firstname
      ligadura.variable = valor variable  
"""

class EmptyPerson:
    pass

print(EmptyPerson) # Puede ir sin parentesis
print(EmptyPerson()) # O con parentesis como seria lo mas común. Los parentesis los necesitamos cuando la clase tenga algo que vaya a ejecutarse

# CONSTRUCTOR DE CLASES

class ExamplePerson:
    def __init__(self, name, lastname) -> None: # Esto es lo que se conoce como un constructor de clase. Aunque estemos ocupando el 'def' no quiere decir que sea una función. El '__init__' definie el constructor y debe de ir acompañado de 'def'. Esto como tal es un espacio que nos indica o nos permite establecer datos asociados con la clase. Puede llevar el None o no
        
    # El 'self' es obligatorio si queremos crear una clase que tenga un constructor
    
    # 'self' se refiere a 'el' mismo. Se refiere a la instancia de la clase
    
        self.name = name # El parametro que acompaña el 'self' es una propiedad asignada al 'self' que pertenece a la clase y esta la igualamos a la propiedad o el dato que va a contener el constructor. Es decir, le asignamos el valor o parametro del constructor al parametro de la clase asignado al 'self'. Vaya que el ´self´ debe tener un parametro o dato con cual identificarlo, que NO es el mismo que el parametro del constructor. Se le puede asignar el parametro del constructor pero no quiere decir que sean lo mismo o iguales. El del constructor se le asignara al del 'self'. Por decirlo de otra manera, estamos asignando un valor a la propiedad del parametro 'self'
        self.lastname = lastname
        # pass . El 'pass' se ocupa cuando se crea una función que no tiene nada, que esta vacía
    
example_person = ExamplePerson('Nahun', 'Fernández')
print(example_person.name)
print(example_person.lastname)

# En la siguiente clase podemos observar como los parametros del constructor y del self son diferentes. Los parametros del constructor son los que se van a manejar dentro de la clase y los del self fuera de la clase

# Podemos definir valores dentro del constructor o directamente en el 'self'. La diferencia va a estar al momento de llamar la clase. Si lo valores estan en el constructor, hay que asignarle datos a estos valores al llamar a la clase. Si los valores estan directamente en el self, ya no es necesario pasar datos al momento de llamar la clase, ya que estos ya se le pasaron directamente al self 

print("________valores dentro del constructor___________")

print("________example one___________")

class Person:
    def __init__(self, firstname, lastname):
        self.name = firstname
        self.surname = lastname
        
person = Person('Moisés', 'Hernández')

print(person.name, person.surname)
print(f'Mi nombre es {person.name} {person.surname}')

print("________example two___________")

class PersonTwo:
    def __init__(self, firstname, lastname):
        self.full_name = f'{firstname} {lastname}'
        
person_two = PersonTwo('Eliab', 'López')

print(person_two.full_name)
print(f'Mi nombre es {person_two.full_name}')

print("________valores directamente en el self___________")

class PersonSecond:
    def __init__(self):
        self.name = 'Efraín'
        self.surname = 'López'
        
person_second = PersonSecond()

print(person_second.name, person_second.surname)
print(f'Mi nombre es {person_second.name} {person_second.surname}')

print("________funciones en una clase___________")

# FUNCIONES DENTRO DE UNA CLASE

class PersonFour ():
    def __init__(self, gamertag, apodo) -> None:
        self.gamertag = gamertag
        self.apodo = apodo
        self.alias = f'{apodo} - {gamertag}'
        
    def walk(self): # Al pasar el parametro 'self', por defecto vamos a poder acceder a todo lo que este guardado dentro del 'self', esto si hay un constructor o inicializador de clase
        # print(f'{self.gamertag} la "{self.apodo}" está caminando')
        walking = f'{self.gamertag} la "{self.apodo}" está caminando'
        print(walking)

person_four = PersonFour('Predator_Rider', 'Molleja')
print(person_four.alias)
person_four.walk()

class PersonSix():
    def __init__(self) -> None:
        self.name = ''
        self.surname = ''
        self.alias = ''
        
    def talk(self):
        print(f'{self.name} ({self.alias}) {self.surname}, es considerada la mujer con la voz mas hermosa de México')
        
person_six = PersonSix()
person_six.name = 'Karla'
person_six.surname = 'Cabello'
person_six.alias = 'Voz de Diosa'
person_six.talk()

class PersonSeven():
    def __init__(self, firstname, lastname, alias = 'No definido') -> None:
        self.name = firstname
        self.surname = lastname
        self.alias = alias
        self.full_name = f'{firstname} {lastname} - {alias}'
        self.action = f'{firstname} {lastname} esta de vacaciones'
        
    def alias_person(self):
        print(f'{self.name} {self.surname}, mejor conocido(a) como "{self.alias}"')
        
    def vacaciones_person(self):
        print(self.action)
        
person_seven = PersonSeven('Eliab', 'Hernandez')
print(person_seven.full_name)
        
person_seven = PersonSeven('Valentino', 'Rossi', 'El Rey')
print(person_seven.full_name)
person_seven.alias_person()

person_seven.name = 'Jose'
person_seven.surname = 'Sosa'
person_seven.alias = 'José José - El Príncipe de la Canción'
person_seven.alias_person()

person_seven.vacaciones_person()

person_seven.action = 'Karlita "Voz de Diosa" deja asombrados a los oyentes en su primera presentación'
person_seven.vacaciones_person()

# Tambien puede cambiar el tipo de dato que contiene el self de las clases

person_seven.alias = 666
print(person_seven.alias)

print("________propiedad publica y privada del self___________")

# PROPIEDAD PUBLICAS Y PRIVADAS DEL SELF DENTRO DE LAS CLASES

"""  Las propiedades o variables (por llamarlas de alguna manera para identificarlas) del self dentro de las clases pueden ser públicas o privadas, esto quiere decir que puedes tener acceso a ellas o no, fuera de la clase.

Si la propiedad es pública se puede acceder a ella fuera de la clase e incluso se puede modificar y la manera de declararla es simplemente poniendo el nombre de la propiedad después del self

Si la propiedad es privada no se va a poder acceder a ella fuera de la clase y por ende tampoco va a poder ser modificada. Para declarar una propiedad privada es necesario escribir dos guiones bajos (__) después del self y antes del nombre de la propiedad.

NOTA: Es importante saber que podemos usar el nombre de la propiedad privada para "cambiar" el valor de dicha propiedad y pongo cambiar entre comillas porque aunque parezca que eso hacemos en realidad no es asi, lo que hacemos es crear una nueva propiedad con ese nuevo valor, la propiedad privada seguira teniendo el mismo valor que le asignamos al momento de llamar la clase o bien el que le asignemos de forma directa en la clase. Esto lo podemos comprobar el los print de hasta abajo donde veremos que si cambia el nombre pero que si imprimimos la funcion que nos retorna la propiedad privada seguira siendo el mismo que le asignamos al llamar a la clase y con el 'vars' veremos que esta creando una nueva propiedad con el mismo nombre de la propiedad privada pero con el nuevo valor asignado """

class Moto():
    def __init__(self, brand, model, year) -> None:
        self.__brand = brand # Propiedad Privada
        self.model = model # Propiedad Pública
        self.year = year # Propiedad Pública
        
    def get_brand(self):
        return self.__brand
    
    def brand_model(self):
        print(f'Motocicleta {self.__brand}, Modelo {self.model}, Año {self.year}')
        
moto_honda = Moto('Honda', 'CBR600RR', 2003)
moto_honda.brand_model()
moto_honda.model = 'Fireblade 900'
moto_honda.year = 2005
moto_honda.brand_model()
moto_honda.__brand = 'Ducati'
print(moto_honda.__brand)
print(vars(moto_honda))
print(moto_honda.get_brand())
moto_honda.__brand = 'Yamaha'
moto_honda.brand_model()
print(moto_honda.__brand)
print(moto_honda.get_brand())
print(vars(moto_honda))