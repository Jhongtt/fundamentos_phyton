## **Python como una calculadora**

#Ahora, se va a mostrar un nuevo lado de la función print(). Ya se sabe que la función es capaz
#de mostrar los valores de los literales que le son pasados por los argumentos.
#de hecho, puede hacer algo más. Observa el siguiente fragmento de código:

#1. Operadores aritméticos
print(2+2)
print(2*3)
print(2**3)
print(2/3)

#2. multiplicacion entera
print(2 ** 3)
print(2 ** 3.)
print(2. ** 3)
print(2. ** 3.)
print(2 ** 2 ** 3)
#3. multiplicacion
print(2 * 3)
print(2 * 3.)
print(2. * 3)
print(2. * 3.)




#4. division
print(6 / 3)
print(6 / 3.)
print(6. / 3)
print(6. / 3.)
print(4 / 6)

#5. division entera
print(6 // 3)
print(6 // 3.)
print(6. // 3)
print(6. // 3.)

print(6 // 4)
print(6. // 4)

print(-6 // 4)
print(6. // -4)

#6. resto de la division
print(14 % 4)

print(12 % 4.5)

print(9 % 6 % 2)

#7. suma
print(-4 + 4)
print(-4. + 8)

print(+2)

#8. resta
print(-4 - 4)
print(4. - 8)
print(-1.1)

print(-3**2)
print(-2 ** 3)
print(-(3 ** 2))

print(2 * 3 % 5)

print((5 * ((25 % 13) + 100) / (2 * 13)) // 2)


#laboratorio 1 Ejercicios de Operadores, Matematicos.

# Ejercicio 1: 5 + 3 * 2
# La multiplicación va antes que la suma
print(5 + 3 * 2)  # Resultado: 11

# Ejercicio 2: 8 / 2 + 4 * 3
# La división y multiplicación van antes que la suma
print(8 / 2 + 4 * 3)  # Resultado: 16.0

# Ejercicio 3: (7 + 3) * 2 - 5
# Primero el paréntesis, luego la multiplicación y al final la resta
print((7 + 3) * 2 - 5)  # Resultado: 15

# Ejercicio 4: 10 - 4 + 2 * 3
# La multiplicación va antes que la resta y la suma
print(10 - 4 + 2 * 3)  # Resultado: 12

# Ejercicio 5: (10 / 2) * (3 + 2) - 4
# Primero los paréntesis, luego la multiplicación y al final la resta
print((10 / 2) * (3 + 2) - 4)  # Resultado: 21.0

# Ejercicio 6: 2 + 3 * (4 - 1)
# Primero el paréntesis, luego la multiplicación y al final la suma
print(2 + 3 * (4 - 1))  # Resultado: 11

# Ejercicio 7: 5 * 2 ** 3
# La potencia tiene más prioridad que la multiplicación
print(5 * 2 ** 3)  # Resultado: 40

# Ejercicio 8: 6 + 4 / 2 ** 2
# Primero la potencia, luego la división y al final la suma
print(6 + 4 / 2 ** 2)  # Resultado: 7.0

# Ejercicio 9: 10 % 3 + 2 * 5
# El % da el residuo de la división, luego la multiplicación y al final la suma
print(10 % 3 + 2 * 5)  # Resultado: 11

# Ejercicio 10: (8 + 2) * 3 ** 2
# Primero el paréntesis, luego la potencia y al final la multiplicación
print((8 + 2) * 3 ** 2)  # Resultado: 90

# Ejercicio 11: 7 + 2 * (3 + 5) / 4
# Primero el paréntesis, luego multiplicación y división, al final la suma
print(7 + 2 * (3 + 5) / 4)  # Resultado: 11.0

# Ejercicio 12: 2 ** 3 * 4 / 2
# Primero la potencia, luego multiplicación y división de izquierda a derecha
print(2 ** 3 * 4 / 2)  # Resultado: 16.0

# Ejercicio 13: 9 - 6 + 3 ** 2
# Primero la potencia, luego resta y suma de izquierda a derecha
print(9 - 6 + 3 ** 2)  # Resultado: 12

# Ejercicio 14: (7 - 2) * 5 + 3 ** 2
# Primero el paréntesis y la potencia, luego la multiplicación y al final la suma
print((7 - 2) * 5 + 3 ** 2)  # Resultado: 34

# Ejercicio 15: 4 * 2 ** 3 / 8 + 1
# Primero la potencia, luego multiplicación y división, al final la suma
print(4 * 2 ** 3 / 8 + 1)  # Resultado: 5.00