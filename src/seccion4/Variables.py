
# Variables son espacios en memoria que se utilizan para almacenar datos. En Python, no
#  es necesario declarar el tipo
var = 1
print(var)

#.1 como empliar una variable
var = 1
account_balance = 1000.0
client_name = 'John Doe'
print(var, account_balance, client_name)
print(var)

var = 1
print(var)

var ="3.8.5"
print("Python version: " + var)

#2. Cómo asignar un nuevo valor a una variable ya existente

var = 1
print(var)
var = var + 1
print(var)

var = 100
var = 200 + 300
print(var)

#3. Resolviendo problemas matemáticos simples

a = 3.0
b = 4.0
c = (a ** 2 + b ** 2) ** 0.5
print("c =", c)

#laboratorio 1 Variables

# Variables con el número de manzanas de cada persona
john = 3
mary = 5
adam = 6

# Imprimir las tres variables en una línea separadas por coma
print(john, mary, adam, sep=", ")

# Sumar las tres variables
total_apples = john + mary + adam

# Imprimir el total
print("Número total de manzanas:", total_apples)

# Experimentando con nuevas variables y operaciones
double_john = john * 2
print("El doble de manzanas de Juan:", double_john)

difference = adam - john
print("Diferencia entre Adán y Juan:", difference)

half_mary = mary / 2
print("La mitad de manzanas de María:", half_mary)

floor_division = total_apples // 4
print("Manzanas si se reparten entre 4 personas:", floor_division)

remainder = total_apples % 4
print("Manzanas que sobran al repartir entre 4:", remainder)

squared = adam ** 2
print("Manzanas de Adán al cuadrado:", squared)

#4 Operadores Abreviados
x = 5
x *= 2  # Equivalente a x = x * 2
print(x)

sheep = 12
sheep += 1
print(sheep)

x *= 2
sheep += 1
print(sheep)
 
 #laboratorio 2 convertidor simple

kilometers = 12.25
miles = 7.38

miles_to_kilometers = miles * 1.61
kilometers_to_miles = kilometers / 1.61

print(miles, "millas son", round(miles_to_kilometers, 2), "kilómetros")
print(kilometers, "kilómetros son", round(kilometers_to_miles, 2), "millas")

#laboratorio 3 operadores y expresiones

x = 0
x = float(x)
y = 3*x**3 - 2*x**2 + 3*x - 1
print("y =", y)

x = 1
x = float(x)
y = 3*x**3 - 2*x**2 + 3*x - 1
print("y =", y)

x = -1
x = float(x)
y = 3*x**3 - 2*x**2 + 3*x - 1
print("y =", y)

#laboratorio 4 ejercicio de algoritmo 

# Ejercicio 1: Puntaje total del jugador
nivel1 = int(input("Puntos nivel 1: "))
nivel2 = int(input("Puntos nivel 2: "))
nivel3 = int(input("Puntos nivel 3: "))
total_puntaje = nivel1 + nivel2 + nivel3
print("Puntaje total:", total_puntaje)

# Ejercicio 2: Tiempo total de juego en segundos
horas = int(input("Horas jugadas: "))
minutos = int(input("Minutos jugados: "))
segundos = int(input("Segundos jugados: "))
tiempo_total = horas * 3600 + minutos * 60 + segundos
print("Tiempo total en segundos:", tiempo_total)

# Ejercicio 3: Daño total causado
ataque1 = int(input("Daño ataque 1: "))
ataque2 = int(input("Daño ataque 2: "))
ataque3 = int(input("Daño ataque 3: "))
dano_total = ataque1 + ataque2 + ataque3
print("Daño total:", dano_total)

# Ejercicio 4: Experiencia total ganada
exp_mision1 = int(input("Experiencia misión 1: "))
exp_mision2 = int(input("Experiencia misión 2: "))
exp_mision3 = int(input("Experiencia misión 3: "))
exp_total = exp_mision1 + exp_mision2 + exp_mision3
print("Experiencia total:", exp_total)

# Ejercicio 5: Porcentaje de vida restante
# Ejercicio 1: Puntaje total del jugador
nivel1 = int(input("Puntos nivel 1: "))
nivel2 = int(input("Puntos nivel 2: "))
nivel3 = int(input("Puntos nivel 3: "))
total_puntaje = nivel1 + nivel2 + nivel3
print("Puntaje total:", total_puntaje)

# Ejercicio 2: Tiempo total de juego en segundos
horas = int(input("Horas jugadas: "))
minutos = int(input("Minutos jugados: "))
segundos = int(input("Segundos jugados: "))
tiempo_total = horas * 3600 + minutos * 60 + segundos
print("Tiempo total en segundos:", tiempo_total)

# Ejercicio 3: Daño total causado
ataque1 = int(input("Daño ataque 1: "))
ataque2 = int(input("Daño ataque 2: "))
ataque3 = int(input("Daño ataque 3: "))
dano_total = ataque1 + ataque2 + ataque3
print("Daño total:", dano_total)

# Ejercicio 4: Experiencia total ganada
exp_mision1 = int(input("Experiencia misión 1: "))
exp_mision2 = int(input("Experiencia misión 2: "))
exp_mision3 = int(input("Experiencia misión 3: "))
exp_total = exp_mision1 + exp_mision2 + exp_mision3
print("Experiencia total:", exp_total)

# Ejercicio 5: Porcentaje de vida restante
vida_maxima = int(input("Vida máxima del personaje: "))
vida_actual = int(input("Vida actual del personaje: "))
porcentaje_vida = (vida_actual / vida_maxima) * 100
print("Porcentaje de vida restante:", round(porcentaje_vida, 2), "%")

# Ejercicio 6: Oro total recolectado
oro_mision1 = int(input("Oro misión 1: "))
oro_mision2 = int(input("Oro misión 2: "))
oro_mision3 = int(input("Oro misión 3: "))
oro_total = oro_mision1 + oro_mision2 + oro_mision3
print("Oro total recolectado:", oro_total)

# Ejercicio 7: Velocidad promedio de un vehículo
distancia = float(input("Distancia recorrida (km): "))
tiempo = float(input("Tiempo tomado (horas): "))
velocidad_promedio = distancia / tiempo
print("Velocidad promedio:", round(velocidad_promedio, 2), "km/h")

# Ejercicio 8: Costo total de mejoras
mejora1 = int(input("Costo mejora 1: "))
mejora2 = int(input("Costo mejora 2: "))
mejora3 = int(input("Costo mejora 3: "))
costo_total_mejoras = mejora1 + mejora2 + mejora3
print("Costo total de mejoras:", costo_total_mejoras)

# Ejercicio 9: Tiempo restante para completar misión
tiempo_total_mision = int(input("Tiempo total de la misión (segundos): "))
tiempo_transcurrido = int(input("Tiempo transcurrido (segundos): "))
tiempo_restante = tiempo_total_mision - tiempo_transcurrido
print("Tiempo restante:", tiempo_restante, "segundos")

# Ejercicio 10: Nivel promedio del equipo
nivel_jugador1 = int(input("Nivel jugador 1: "))
nivel_jugador2 = int(input("Nivel jugador 2: "))
nivel_jugador3 = int(input("Nivel jugador 3: "))
nivel_promedio = (nivel_jugador1 + nivel_jugador2 + nivel_jugador3) / 3
print("Nivel promedio del equipo:", round(nivel_promedio, 2))

# Ejercicio 11: Daño crítico
dano_base = int(input("Daño base del ataque: "))
multiplicador_critico = float(input("Multiplicador crítico: "))
dano_critico = dano_base * multiplicador_critico
print("Daño crítico:", round(dano_critico, 2))

# Ejercicio 12: Tiempo total en horas y minutos
tiempo_minutos = int(input("Tiempo total jugado en minutos: "))
horas_convertidas = tiempo_minutos // 60
minutos_restantes = tiempo_minutos % 60
print("Tiempo total:", horas_convertidas, "horas y", minutos_restantes, "minutos")

# Ejercicio 13: Porcentaje de misiones completadas
total_misiones = int(input("Número total de misiones: "))
misiones_completadas = int(input("Misiones completadas: "))
porcentaje_misiones = (misiones_completadas / total_misiones) * 100
print("Porcentaje de misiones completadas:", round(porcentaje_misiones, 2), "%")

# Ejercicio 14: Costo total de objetos en tienda
objeto1 = int(input("Costo objeto 1: "))
objeto2 = int(input("Costo objeto 2: "))
objeto3 = int(input("Costo objeto 3: "))
costo_total_objetos = objeto1 + objeto2 + objeto3
print("Costo total de objetos:", costo_total_objetos)

# Ejercicio 15: Tiempo promedio de una partida
partida1 = int(input("Tiempo partida 1 (minutos): "))
partida2 = int(input("Tiempo partida 2 (minutos): "))
partida3 = int(input("Tiempo partida 3 (minutos): "))
tiempo_promedio = (partida1 + partida2 + partida3) / 3
print("Tiempo promedio de partida:", round(tiempo_promedio, 2), "minutos")

# Ejercicio 16: Porcentaje de enemigos derrotados
total_enemigos = int(input("Número total de enemigos: "))
enemigos_derrotados = int(input("Enemigos derrotados: "))
porcentaje_enemigos = (enemigos_derrotados / total_enemigos) * 100
print("Porcentaje de enemigos derrotados:", round(porcentaje_enemigos, 2), "%")