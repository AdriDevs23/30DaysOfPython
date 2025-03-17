# Exercises with for loop with Micrsoft Copilot 

# Suma de elementos en una lista:

even_list = [2, 4, 6, 8, 10]

resultado_even = 0

for i in even_list:
    resultado_even += i
print(f"La suma total de la lista es: {resultado_even}")

# Multiplicación de elementos en una lista:

odd_list = [1, 3, 5, 7, 9]
resultado_odd = 1

for i in odd_list:
    resultado_odd *= i
print(f"La multiplicacion de la lista es {resultado_odd}")

# Imprimir caracteres de una cadena:

palabra = "Programación"
for i in palabra:
    print(i)

# Números pares en una lista:

is_even = [10, 21, 32, 43, 54, 65]

for i in is_even:
    if i % 2 == 0:
        print(f"{i} es numero par")
    else:
        print(f"{i} es impar")

# Calcular factorial de un número dado:

factorial = 7
resultado_factorial = 1

for i in range(1, factorial + 1):
    resultado_factorial *= i
print(resultado_factorial)


# Imprimir números en orden inverso en una lista:

numeros_desordenados = [12, 34, 56, 78, 90]

numeros_desordenados.reverse()
print(numeros_desordenados)


# Tablas de multiplicar de un número dado:

i = 6

for j in range(11):
    print(f"{i} x {j} = {i * j}")


# Contar vocales en una cadena:

frase = "Inteligencia Artificial"
frase = frase.lower()
contador_vocales = { 'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0 }


for caracter in frase:
    if caracter in "aeiou":
        contador_vocales[caracter] += 1
print(contador_vocales)


# Crear una lista de cuadrados de números del 1 al 10:

cuadrados = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
cuadrados_calculados = []

for i in cuadrados:
    cuadrados_calculados.append(i **2)
print(cuadrados_calculados)

# Filtrar palabras de una lista que tengan menos de 4 letras:

letras = ["sol", "luna", "estrella", "mar", "tierra"]
mas_caracter = []
menos_caracter = []

for caracter in letras:
    if len(caracter) > 4:
        mas_caracter.append(caracter)
    else:
        menos_caracter.append(caracter)

print(f"Las palabras con menos de cuatro letras son {menos_caracter}")
print(f"Las palabras con más de cuatro letras son {mas_caracter}")


# Sumar todos los números en una lista:

numeros = [2, 4, 6, 8, 10]
numeros_sumados = sum(numeros)

print(f"Los numeros suman {numeros_sumados}")


# Encontrar el número máximo en una lista:

numeros_max = [15, 22, 34, 11, 27]
max_numero = max(numeros_max)

print(f"El numero más grande es {max_numero}")

# Contar el número de veces que aparece una vocal en una cadena:

frase = "Inteligencia Artificial"
vocales_contador = {"a": 0, "e": 0, "i": 0, "o": 0, "u": 0}

for caracter in frase.lower():
    if caracter in "aeiou":
        vocales_contador[caracter] += 1
print(vocales_contador)

# Imprimir cada clave y valor en un diccionario:

estudiantes = {'Juan': 18, 'Ana': 20, 'Luis': 19, 'Sofía': 21}

for key, value in estudiantes.items():
    print(f"{key}: {value}")

# Generar una lista de números al cuadrado:

numeros_cuadrado = [1, 2, 3, 4, 5]
cuadrado_calculado = []

for i in numeros_cuadrado:
    cuadrado_calculado.append(i ** 2)
    print(f"El cuadrado de {i} es {i ** 2}")

# Calcular la longitud de cada palabra en una lista:

lista_palabras = ['gato', 'perro', 'elefante', 'tigre']
longitud = []

for i in lista_palabras:
    longitud.append(len(i))
    print(f"La palabra {i} tiene {len(i)} caracteres")

# Encontrar todos los números pares en una lista:

numeros_pares = [1, 3, 4, 7, 8, 10, 13, 14, 17]
lista_pares = []
lista_impares = []

for i in numeros_pares:
    if i % 2 == 0:
        lista_pares.append(i)
    else:
        lista_impares.append(i)

print(f"Los números pares son {lista_pares}")
print(f"Los números impares son {lista_impares}")

# Concatenar todas las palabras en una lista en una sola cadena:

concatenar_palabras = ['Hola', 'mundo', 'esto', 'es', 'Python']
frase_concatenada = " ".join(concatenar_palabras)

print(frase_concatenada)

# Contar el número de elementos únicos en un conjunto (set):

conjunto_numeros = {3, 5, 7, 9, 11, 5, 3, 9}
elementos_unicos = len(conjunto_numeros)

print(f"El número de elementos únicos es {elementos_unicos}")

# Sumar todos los valores en un diccionario:

ventas = {'enero': 1500, 'febrero': 2300, 'marzo': 1850, 'abril': 2000}
suma_total = 0

for values in ventas.values():
    suma_total += values

print(f"La suma de todos los valores de ventas es de {suma_total}€")


# Multiplicar todos los números en una lista y obtener el producto:

numeros = [2, 3, 4, 5]
producto = 1

for i in numeros:
    producto *= i
print(f"El resultado total de la multiplicación es {producto}")

# Convertir cada palabra en una lista a mayúsculas:

palabras = ['python', 'java', 'c++', 'ruby']
palabras_mayusculas = []

for i in palabras:
    palabras_mayusculas.append(i.upper())
print(f"La lista de palabras en mayuscula es {palabras_mayusculas}")

# Contar cuántos números son mayores que 10 en una lista:

numeros = [5, 12, 18, 3, 7, 25, 10]
numeros_mayores = []
numeros_menores = []

for i in numeros:
    if i > 10:
        numeros_mayores.append(i)
    else:
        numeros_menores.append(i)

print(f"Los números mayores que 10 son {sorted(numeros_mayores)}")
print(f"Los números menores que 10 son {sorted(numeros_menores)}")

# Imprimir la posición (índice) y el valor de cada elemento en una lista:

colores = ['rojo', 'verde', 'azul', 'amarillo']

for indice, valor in enumerate(colores):
    print(f"Indice: {indice}, valor: {valor}")


# Agregar una cadena de texto a cada elemento de una lista:
# Cadena de texto para agregar: ' fruta'

frutas = ['manzana', 'pera', 'naranja']
frutas_actualizado = []

for i in frutas:
    frutas_modificada = i + " fruta"
    frutas_actualizado.append(frutas_modificada)
print(frutas_actualizado)

# Revertir los elementos de una lista sin usar métodos de lista incorporados:

numeros = [1, 2, 3, 4, 5]
numeros_reverse = []

for i in range(len(numeros) -1, -1, -1):
    numeros_reverse.append(numeros[i])
print(numeros_reverse)

# Suma acumulativa de los elementos en una lista:

numeros = [10, 20, 30, 40]
suma_acumulativa = 0

for i in numeros:
    suma_acumulativa += i
    print(suma_acumulativa)


# Concatenar los valores de un diccionario en una sola cadena:

datos = {'nombre': 'Alice', 'apellido': 'Smith', 'ciudad': 'Madrid'}
cadena = str()

for value in datos.values():
    cadena += value + " "
print(f"Los valores son {cadena}")

# Calcular la frecuencia de cada carácter en una cadena:

cadena = "abracadabra"
frecuencias = dict()

for caracter in cadena:
    if caracter in frecuencias:
        frecuencias[caracter] += 1
    else:
        frecuencias[caracter] = 1
print(frecuencias)

# Generar una lista de pares (i, j) de todos los elementos en dos listas:

lista1 = [1, 2, 3]
lista2 = ['a', 'b', 'c']
pares = []

for i in lista1:
    for j in lista2:
        pares.append((i, j))

print(pares)

# Crea un bucle for que imprima los valores del 7 al 14

for i in range(7, 15):
    print(f"El valor del bucle es: {i}")

# Crea un bucle for que imprima los valores de 0 al -5000 en decrementos de 500

for i in range (0, -5001, -500):
    print(f"El valor del bucle es: {i}")

# Imprime por pantalla la lista de numeros exceptuando los 10 y debe salir del bucle cuando se encuentre el numero 356
lista_numeros = [10, 45, 356, 10, 10, 10, 46, 67, 45, 10,43, 10, 65, 10, 10]
lista_numeros_ordenada = sorted(lista_numeros)

for i in lista_numeros_ordenada:
    if i == 10:
        continue
    elif i == 356:
        break
    else:
        print(f"El valor del elemento es {i}")