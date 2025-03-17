# Exercises with for loop with Micrsoft Copilot 

# Crea un bucle while que imprima los valores del 7 al 14

i = 7

while i <= 14:
    print(f"El valor del bucle es: {i}")
    i += 1

# Crea un bucle while que imprima los valores de 0 al -5000 en decrementos de 500

i = 0

while i >= -5000:
    print(f"El valor del bucle es: {i}")
    i -= 500


# Imprimir números del 1 al 10 usando un bucle while.

numero = 1

while numero < 11:
    print(numero)
    numero += 1

# Sumar los números pares del 1 al 20.

numero = 1
suma = 0

while numero <= 20:
    if numero % 2 == 0:
        suma += numero
    numero += 1
print(suma)



# Contar cuántas veces aparece un carácter en una cadena:

cadena = "abracadabra"
caracter_a_contar = 'a'
contador = 0
indice = 0

while indice < len(cadena):
    if cadena[indice] == caracter_a_contar:
        contador += 1
    indice += 1

print(contador)



# Encontrar el valor mínimo en una lista:

numeros = [12, 5, 23, 7, 18, 3, 15]
indice = 0
minimo = numeros[0]

while indice < len(numeros):
    if numeros[indice] < minimo:
        minimo = numeros[indice]
    indice += 1

print(minimo)

# Imprimir elementos de una lista en orden inverso:

# frutas = ['manzana', 'pera', 'naranja', 'plátano']

# Calcular la longitud de una cadena sin usar len():

# cadena = "Python es genial"

# Contar cuántas claves tiene un diccionario:

# datos = {'nombre': 'Alice', 'edad': 30, 'ciudad': 'Madrid'}

# Multiplicar todos los elementos de una lista:

# numeros = [2, 4, 6, 8]

# Encontrar el número de elementos únicos en un conjunto:

# conjunto = {1, 2, 3, 4, 5, 6, 7, 8, 9}

# Eliminar las vocales de una cadena:

# cadena = "el desarrollo es divertido"