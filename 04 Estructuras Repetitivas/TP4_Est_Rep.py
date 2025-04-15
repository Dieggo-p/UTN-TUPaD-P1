# Ejercicio 1
for i in range (0, 101):
    print(i)
    
# Ejercicio 2
n = input('Ingresa un número entero: ')

if n.startswith('-'):
    n = n[1:]
cantidad_digitos = len(n)
print('El número tiene', cantidad_digitos, 'dígitos.')

# Ejercicio 3
inicio = int(input('Ingrese el primer número: '))
fin = int(input('Ingrese el segundo número: '))

# Se asegura que el inicio sea menor que el fin para que este ordenado

menor = min(inicio, fin)
mayor = max(inicio, fin)

suma = 0 

for i in range(menor + 1, mayor):
    suma += i
print('La suma de los números entre', menor, 'y', mayor, 'es:', suma)

# Ejercicio 4
n = input('Ingrese un número o presione 0 para terminar: ')
suma = 0

while n != '0':
    suma += int(n)
    n = input('Ingrese un número o presione 0 para terminar: ')
print('La suma es:', suma)

# Ejercicio 5
import random

n = int(input('Adivina el número entre 0 y 9: '))
n2 = random.randint(0, 9)
intentos = 0
while n != n2:
    intentos += 1
    n = int(input('Otra vez, adivina el número entre 0 y 9: '))
    if n < n:
        print('El número es mayor')
    elif n > n:
        print('El número es menor')
print('Felicitaciones, adivinaste el número', n2, 'en', intentos, 'intentos')

# Ejercicio 6
for i in range (100, -1, -2):
    print(i)

# Ejercicio 7
n = int(input('Ingrese un número positivo: '))

if n > 0:
    suma = 0
    for i in range(0, n + 1):
        suma += i
    print('La suma de los números desde 0 hasta', n, 'es:', suma)
else:
    print('El número debe ser positivo')

# Ejercicio 8
# Cantidad de números a ingresar
numeros = 10

# Contandores
pares = 0
impares = 0
positivos = 0
negativos = 0

for i in range(numeros):
    n = int(input(f'Ingrese un número {i + 1}: '))
    
    # if para verificar si es par o impar
    if n % 2 == 0:
        pares += 1
    else:
        impares += 1
        
    # if para verificar si es positivo o negativo
    if n > 0: 
        positivos += 1
    elif n < 0:
        negativos += 1

print('\nRESULTADOS')
print('Pares:', pares)
print('Impares:', impares)
print('Positivos:', positivos)
print('Negativos:', negativos)

# Ejercicio 9
numeros = 10
suma = 0

for i in range(numeros):
    n = int(input(f'Ingrese un número {i + 1}: '))
    suma += n

media = suma / numeros
print('La media de los números ingresados es:', media)

# Ejercicio 10
n = input('Ingrese un número: ')

n_invertido = n[::-1]

print('El número invertido es:', n_invertido)