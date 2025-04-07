edad = int(input("Ingrese su edad: "))

if edad >= 18:
    print("Eres mayor de edad.")
else :
    print("Eres menor de edad.")


nota = int(input('Ingrese su nota: '))

if nota >= 6:
    print('Aprobado')
else:
    print('Desaprobado')
    
    
num = int(input('Ingrese un número: '))

if num % 2 == 0:
    print('El número es par')
else: 
    print('El número es impar')
    

dad = int(input('Ingrese su edad: '))

if edad < 12:
    print('Eres un niño/a')
elif edad >= 12 and edad < 18:
    print('Eres un adolescente')
elif edad >= 18 and edad < 30: 
    print('Eres un adulto/a joven')
elif edad >= 30:
    print('Eres un adulto/a mayor')
    
    
contraseña = input('Ingrese su contraseña de entre 8 y 14 caracteres: ')
verificar = len(contraseña)

if verificar >= 8 and verificar <= 14:
     print ('Ha ingresado una contraseña correcta')
else: 
    print('Por favor, ingrese una contraseña de entre 8 y 14 caracteres')


import random
from statistics import mode, median, mean 
numeros = [random.randint(1, 100) for i in range(50)]

moda = mode(numeros)
print('moda = ', moda)
mediana = median(numeros)
print('mediana = ', mediana)
media = mean(numeros)
print('media = ', media)

if moda > mediana and mediana > media:
    print("Sesgo positivo")
elif moda < mediana and mediana < media:
    print("Sesgo negativo")
elif moda == mediana and mediana == media: 
    print("Sin sesgo")
    
    
frase = input('Ingrese una frase o palabra: ')
vocales = ['a', 'e', 'i', 'o', 'u']
if frase[-1] in vocales:
    print(frase + '!')
else: 
    print(frase)
    
    
nombre = input('Ingrese su nombre: ')
opcion = int(input('Ingrese un numero según la opcion deseada: la opcion que desea: 1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO. 2. Si quiere su nombre en minúsculas. Por ejemplo: pedro. 3. Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro.'))
if opcion == 1: 
    print(nombre.upper())
elif opcion == 2: 
    print(nombre.lower())
elif opcion == 3: 
    print(nombre.title())
else: 
    print('Opción no válida.')


terremoto = int(input('Ingrese la magnitud del terremoto: '))

if terremoto < 3: 
    print('Muy leve (imperceptible)')
elif terremoto >= 3 and terremoto < 4:
    print('Leve (Ligeramente perceptible)')
elif terremoto >= 4 and terremoto < 5:
    print('Moderado (sentido por las personas, pero generalmente no causa daños)')
elif terremoto >= 5 and terremoto < 6:
    print('Fuerte (puede causar daños en estructuras débiles)')
elif terremoto >= 6 and terremoto < 7:
    print('Muy fuerte (puede causar daños significativos)')
elif terremoto >= 7:
    print('Extremo (puede causar graves daños a gran escala)')


hemisferio = input('Ingrese su hemisferio (Norte o Sur): ')
mes = input('Ingrese el mes: ')
dia = int(input('Ingrese el día: '))


if hemisferio == 'norte' and mes == 'diciembre' and dia >= 21 or (mes == 'enero' or mes == 'febrero' or mes == 'marzo' and dia <= 20):
    print('Invierno')
elif hemisferio == 'norte' and mes == 'marzo' and dia >= 21 or mes == 'abril' or mes == 'mayo' or mes == 'junio' and dia <= 20:
    print('Primavera')
elif hemisferio == 'norte' and mes == 'junio' and dia >= 21 or mes == 'julio' or mes == 'agosto' or mes == 'septiembre' and dia <= 20:
    print('Verano')
elif hemisferio == 'norte' and mes == 'septiembre' and dia >= 21 or mes == 'octubre' or mes == 'noviembre' and dia <= 20:
    print('Otoño')
elif hemisferio == 'sur' and mes == 'diciembre' and dia >= 21 or mes == 'enero' or mes == 'febrero' or mes == 'marzo' and dia <= 20:
    print('Verano')
elif hemisferio == 'sur' and mes == 'marzo' and dia >= 21 or mes == 'abril' or mes == 'mayo' or mes == 'junio' and dia <= 20:
    print('Otoño')
elif hemisferio == 'sur' and mes == 'junio' and dia >= 21 or mes == 'julio' or mes == 'agosto' or mes == 'septiembre' and dia <= 20:
    print('Invierno')
elif hemisferio == 'sur' and mes == 'septiembre' and dia >= 21 or mes == 'octubre' or mes == 'noviembre' and dia <= 20:
    print('Primavera')
else:
    print('Mes o día inválido')


