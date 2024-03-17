# --- LAMBDAS ---

# Las Lambdas son como funciones anónimas

# Las funciones anónimas son las que no tienen nombre

""" 
    Funcion normal o con nombre:
        def "nombre_funcion":
            "código a ejecutar en la función"
        
    Función anónima y/o lambda:
        lambda "valores que recibe la lambda": "codigo a ejecutar en la lambda"
"""

# Para llamar a una lambda la podemos guardar dentro de una variable y posteriormente esa variable estaría funcionando como una función

sum_values = lambda one_value, second_value: one_value + second_value
print(sum_values(2, 4))

multiply_values = lambda first_value, second_value: first_value * second_value - 3
print(multiply_values(2, 4))

multiply_values_two = lambda first_value, second_value: first_value * second_value - sum_values(5, 9)
print(multiply_values_two(2, 4))

def sum_three_values(value):
    return lambda first_value, second_value: first_value + second_value + value

print(sum_three_values(5)(2,4))

def sum_three_values(value, value_two):
    return lambda first_value, second_value, thirty_value: first_value + second_value + value - thirty_value * value_two

print(sum_three_values(5, 9)(2, 4, 6))