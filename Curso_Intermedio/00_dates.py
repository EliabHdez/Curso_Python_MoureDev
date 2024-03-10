# --- DATES ---

print('---------- datetime ----------')

from datetime import datetime

# 'datetime' nos sirve para la fecha y la hora. Con este podemos trabajar con la hora y la fecha actual o con alguna que nosotros le asignemos

now = datetime.now()

print(now.year)
print(now.month)
print(now.day)
print(now.hour)
print(now.minute)
print(now.second)

print(now)

timestamp = now.timestamp()

print(timestamp)

def imp_date(date):
    print(date.year)
    print(date.month)
    print(date.day)
    print(date.hour)
    print(date.minute)
    print(date.second)
    print(date.timestamp())
    
imp_date(now)

year_2025 = datetime(2025, 1, 1)

imp_date(year_2025)

print('---------- time ----------')

from datetime import time

# 'time' tiene que ver con la hora, sin embargo no tiene definida la hora como 'datetime'. time nos permite a nosotros estipular la hora que deseemos. Nosotros tenemos que construir esa hora, ya que por si solo 'time' no tiene ningun valor y si lo llamamos sin pasarle paramétros por default va a estar en 0.

current_time = time()
print(current_time)

current_time = time(23, 46, 58)
print(current_time.hour)
print(current_time.minute)
print(current_time.second)
print(current_time)

print('---------- date ----------')

from datetime import date

# 'date' es lo mismo que 'time' pero para las fechas, 'date' no tiene una o la fecha como tal, nosotros la tenemos que desginar y en comparación con 'time', 'date' si necesita llevar valores forzosamente, si no, nos arroja un error. Y estos valores son: "año, mes, dia"

current_date = date(2024, 9, 25)
print(current_date)
print(current_date.year)
print(current_date.month)
print(current_date.day)

# date nos permite trabajar con una fecha en especifico

current_date = date.today()
print(current_date.day)
print(current_date.month)
print(current_date.year)

print('---------- modificando fechas y horas ----------')

# Podemos modificar el tiempo y la fecha

print(current_time)
current_time = time(current_time.hour - 1, current_time.minute + 9, current_time.second - 5)
print(current_time)

print(current_date)
current_date = date(current_date.year + 2, current_date.month + 1, current_date.day + 3)
print(current_date)

# De un 'datetime' podemos extraer solo el date (fecha) o el time (hora)

year_2025.date() # Si queremos ver los resultados, lo podemos meter dentro de un print
year_2025.time() # Si queremos ver los resultados, lo podemos meter dentro de un print

print('---------- Diferencia entre fechas y horas ----------')

# Podemos obtener la diferencia en dias entre fechas. Esto siempre y cuando los elementos que utilicemos sean del mismo tipo, es decir 'datetime' o 'date'. Esto no lo podemos hacer solo con el time (horas)

print(year_2025)
print(now)
print(current_date)
print(current_time)

diff = year_2025 - now
print(diff)

diff = year_2025.date() - current_date
print(diff)

print('---------- timedelta ----------')

from datetime import timedelta

# El 'timedelta' nos permite obtener la diferencia entre cierto espacio de tiempo (fechas y horas). No necesariamente entre dos fechas, si no mas bien entre cierta cantidas de dias, semanas, horas, minutos, segundos...

start_delta = timedelta(hours=5, minutes=59)
end_delta = timedelta(hours=4, minutes=57)
print(end_delta - start_delta)

start_delta = timedelta(200, 100, 100, weeks=10)
end_delta = timedelta(300, 100, 100, weeks=13)
print(end_delta - start_delta)
print(end_delta + start_delta)
print(end_delta / start_delta)

start_delta = timedelta(days=200, seconds=100, milliseconds=100, weeks=10) # Esto es lo mismo que lo de arriba
end_delta = timedelta(days=300, seconds=100, milliseconds=100, weeks=13) # Esto es lo mismo que lo de arriba
print(end_delta - start_delta)

start_delta = timedelta(hours=2, weeks=3)
end_delta = timedelta(hours=6, minutes=18)
print(start_delta - end_delta)
print(start_delta + end_delta)