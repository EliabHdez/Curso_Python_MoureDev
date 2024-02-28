content = '--- Módulo de operaciones matemáticas ---'

def add_values(num_one, num_two, num_three):
    add_nums = num_one + num_two + num_three
    print(add_nums)
    
def mult_values(num_one, num_two, num_three):
    mult_nums = num_one * num_two * num_three
    print(mult_nums)
    
def rest_values(num_one, num_two, num_three):
    rest_nums = num_one - num_two - num_three
    print(rest_nums)
    
def div_values(num_one, num_two, num_three):
    div_nums = num_one / num_two / num_three
    print(div_nums)
    
def pot_value(number, pot):
    pot_number = number ** pot
    print(pot_number)
    
def operations(num_one, num_two, num_three):
    add_nums = num_one + num_two + num_three
    rest_nums = num_one - num_two - num_three
    mult_nums = num_one * num_two * num_three
    div_nums = num_one / num_two / num_three
    print('Los resultados son los siguientes:')
    print(f'Suma: {add_nums}')
    print(f'Resta: {rest_nums}')
    print(f'Multiplicación: {mult_nums}')
    print(f'División: {div_nums}')
    print('*** Operaciones realizadas con éxito ***')
    
def end_module(text):
    print('Fin del módulo')