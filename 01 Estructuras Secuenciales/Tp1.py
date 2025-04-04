print('Hola Mundo')

n = input('Ingrese su nombre')
a = input('Ingrese su apellido')
e = input('Ingrese su edad')
l = input('Ingrese su lugar de residencia')

print(f'Soy {n} {a}, tengo {e} y vivo en {l}.')

radio = float(input("Ingrese el radio del círculo: "))
pi = 3.1416
area = pi * radio ** 2
perimetro = 2 * pi * radio

print(f"Área del círculo: {area}")
print(f"Perímetro del círculo: {perimetro}")

segundos = int(input('Ingrese una cantidad de segundos'))
hora = segundos / 3600
print(f'La cantidad de segundos ingresada equivale a {hora:.2f} hs')

numero = int(input('Ingrese un numero'))
print(f"Tabla de multiplicar del {numero}:")

for i in range(1, 11):
    print(f"{numero} x {i} = {numero * i}")
    
n1 = int(input('Ingrese un numero distinto de 0'))
n2 = int(input('Ingrese un numero distinto de 0'))

if n1 == 0 or n2 == 0:
    print('Los numeros tienen que ser distintos de 0')
else: 
    suma = n1 + n2
    resta = n1 - n2
    mult = n1 * n2
    div = n1 / n2
    print(f'La suma de {n1} y {n2} es {suma}')
    print(f'La resta de {n1} y {n2} es {resta}')
    print(f'La multiplicacion de {n1} y {n2} es {mult}')
    print(f'La division de {n1} y {n2} es {div}')
    
altura = float(input('ingrese su altura en metros'))
peso = float(input('ingrese su peso en kilogramos'))

imc = float(peso) / float(altura) ** 2
print(f'su indice de masa corporal es {imc:.2f}')

grados = float(input('Ingresa los grados celcius'))
farenheit = (grados * 9/5) + 32
print(farenheit)

n1 = input('Ingrese un numero')
n2 = input('Ingrese otro numero')
n3 = input('Ingrese otro numero')   

promedio = (int(n1) + int(n2) + int(n3)) / 3
print('El promedio es:', promedio)