# Ejercicio 1
multiplos_4 = list(range(4,101,4))
print(multiplos_4)

#Ejercio 2
lista = [1, 2, 3, 4, 5]
print(lista[2])

#Ejercicio 3
lista_vacia = []

lista_vacia.append('hola')
lista_vacia.append('como')
lista_vacia.append('estas')
print(lista_vacia)

#Ejercicio 4
lista_animales = ['perro', 'gato', 'conejo', 'pez']

lista_animales[1] = 'loro'
lista_animales[-1] = 'oso'
print(lista_animales)

#Ejercicio 5
# Lo que hace el codigo de la consigna numero 5 es eliminar el numero mas grande de la lista y dejar el resto de los numeros
numeros = [1, 2, 3, 4, 5]
numeros.remove(max(numeros))
print(numeros)


#Ejercicio 6
lista_numeros = list(range(10, 31, 5))
print(lista_numeros[1:3])

#Ejercicio 7
autos = ['sedan', 'polo', 'suran', 'gol']
autos[1:3] = 'vento', '208'
print(autos)

#Ejercicio 8
dobles = []
dobles.append(5*2)
dobles.append(10*2)
dobles.append(15*2)
print(dobles)

#Ejercicio 9
compras = [['pan', 'leche'], ['arroz', 'fideos', 'salsa'], ['agua']]

compras[2].append('jugo')
compras[1][1] = 'tallarines'
compras[0].remove('pan')
print(compras)

#Ejercicio 10
lista_anidada = [15, True, [25.5, 57.9, 30.6], False]
print(lista_anidada)