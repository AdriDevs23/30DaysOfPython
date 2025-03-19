# Exercise 1


# Declare a function add_two_numbers. It takes two parameters and it returns a sum.

def add_two_numbers(a, b):
    return a + b

resultado = add_two_numbers(3, 7)
print(f"La suma de a y b da como resultado: {resultado}")

# Area of a circle is calculated as follows: area = π x r x r. Write a function that calculates area_of_circle.

import math

def area_of_circle (pi, radius):
    return pi * radius ** 2

area_circle = area_of_circle(math.pi, 5.7)
print(f"El area del circulo es: {round(area_circle, 2)}")

# Write a function called add_all_nums which takes arbitrary number of arguments and sums all the arguments. Check if all the list items are number types. If not do give a reasonable feedback.

def add_all_nums(lista):
    total_sum = 0
    for i in lista:
        # Validamos si cada elemento es un número
        if not isinstance(i, (int, float)):
            return f"Error: '{i}' no es un número. Todos los elementos de la lista deben ser números."
        total_sum += i  # Sumamos si es un número
    return total_sum


suma_total = add_all_nums([3, 5, 14, 6, 9]) # Llamada con una lista válida
print(f"La suma total de los números de la lista es: {suma_total}")


suma_con_error = add_all_nums([3, 5, 'hola', 6, 9]) # Llamada con una lista que contiene un error
print(suma_con_error)


# Temperature in °C can be converted to °F using this formula: °F = (°C x 9/5) + 32. Write a function which converts °C to °F, convert_celsius_to-fahrenheit.

def convert_celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

celsius = float(input("Introduce los grados Celsius que quieres convertir: "))
fahrenheit = convert_celsius_to_fahrenheit(celsius)
print(f"El resultado de la conversión de Celcius a Fahrenheit es {fahrenheit}ºF")

# Write a function called check-season, it takes a month parameter and returns the season: Autumn, Winter, Spring or Summer.

def check_season(month_to_check):
    valid_months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    autumn = ["September", "October", "November"]
    winter = ["December", "January", "February"]
    spring = ["March", "April", "May"]
    summer = ["June", "July", "August"]
    if month_to_check not in valid_months:
        return f"El mes {month_to_check} no es válido"
    elif month_to_check in autumn:
        return "Autumn"
    elif month_to_check in winter:
        return "Winter"
    elif month_to_check in spring:
        return "Spring"
    else:
        return "Summer"

month_to_check = input("Introduce el mes para verificar a qué estación pertenece: ").strip().title()
month = check_season(month_to_check)

print(f"El mes {month_to_check} pertenece a la estación {month}")  # Llamada con un mes válido


# Write a function called calculate_slope which return the slope of a linear equation

def calculate_slope(A, B):
    if B == 0:
        return f"Argumento no válido, no tiene pendiente definida"
    return -(A/B)

A = float(input("Introduce el valor de A: "))
B = float(input("Introduce el valor de B: "))
resultado_slope = calculate_slope(A, B)
print(f"La pendiente de los números dados es de {round(resultado_slope, 2)}")


# Quadratic equation is calculated as follows: ax² + bx + c = 0. Write a function which calculates solution set of a quadratic equation, solve_quadratic_eqn.

import math

def solve_quadratic_eqn(a, b, c):
    discriminant = b ** 2 - 4 * a * c
    if discriminant < 0:
        print(f"Discriminante negativo, soluciones son complejas (números imaginarios)")
        return 
    solucion1 = (-b + math.sqrt(discriminant)) / (2 * a)
    solucion2 = (-b - math.sqrt(discriminant)) / (2 * a)
    return solucion1, solucion2

a = float(input("Introduce el valor de a: "))
b = float(input("Introduce el valor de b: "))
c = float(input("Introduce el valor de c: "))

resultado_ecuacion = solve_quadratic_eqn(a, b, c)
if resultado_ecuacion:
    print(f"El resultado de la ecuacion es de: {resultado_ecuacion}")


# Declare a function named print_list. It takes a list as a parameter and it prints out each element of the list.

def print_list(mi_lista):
    for i in mi_lista:
        print(i)

mi_lista = [1, 2, 3, 4, 5]
print_list(mi_lista)

# Declare a function named reverse_list. It takes an array as a parameter and it returns the reverse of the array (use loops).

def reverse_list(reverse_list1, reverse_list2):
    reversed_list1 = []
    reversed_list2 = []
    for i in range(len(reverse_list1) - 1, -1, -1):
        reversed_list1.append(reverse_list1[i])
    for i in range(len(reverse_list2) - 1, -1, -1):
        reversed_list2.append(reverse_list2[i])
    print(f"La lista 1 invertida es: {reversed_list1}")
    print(f"La lista 2 invertida es: {reversed_list2}")

reverse_list1 = [1, 2, 3, 4, 5]
reverse_list2 = ["A", "B", "C"]

reverse_list(reverse_list1, reverse_list2)


# Declare a function named capitalize_list_items. It takes a list as a parameter and it returns a capitalized list of items

def capitalize_list_items(lista_frutas):
    frutas_capitalize = []
    for fruta in lista_frutas:
        frutas_capitalize.append(fruta.capitalize())
    return frutas_capitalize

lista_frutas = ['manzana', 'manana', 'cereza']
resultado_capitalize = capitalize_list_items(lista_frutas)

print(f"La lista impresa en capitalize es: {resultado_capitalize}")

# Declare a function named add_item. It takes a list and an item parameters. It returns a list with the item added at the end.

# Método append() únicamente:
def add_items(food_staff, item_food):
    food_staff.append(item_food)
    return food_staff

food_staff = ['Potato', 'Tomato', 'Mango', 'Milk']
item_food = "meat"

resultado_food = add_items(food_staff, item_food)
print(f"La lista completa es: {resultado_food}")

# Con bucle for:
def add_number(numbers_original, number):
    numbers = []
    for i in numbers_original:
        numbers.append(i)
    numbers.append(number)
    return numbers

numbers_original = [2, 3, 7, 9]
number = 3

resultado_numbers = add_number(numbers_original, number)
print(f"La lista completa es: {resultado_numbers}")

# Declare a function named remove_item. It takes a list and an item parameters. It returns a list with the item removed from it.

# Método remove() únicamente:
def remove_item(food_staff):
    food_staff.remove(food_to_remove)
    return food_staff

food_staff = ['Potato', 'Tomato', 'Mango', 'Milk']
food_to_remove = "Mango"

resultado_remove_food = remove_item(food_staff)
print(f"La lista sin el item {food_to_remove} es: {food_staff}")

# Con bucle for:

def remove_item(food_staff):
    food_staff_final = []
    for i in food_staff:
        if i == food_to_remove:
            continue
        else:
            food_staff_final.append(i)
    return food_staff_final

food_staff = ['Potato', 'Tomato', 'Mango', 'Milk']
food_to_remove = "Mango"

resultado_remove_food2 = remove_item(food_staff)
print(f"La lista sin el item {food_to_remove} es: {resultado_remove_food2}")


# Declare a function named sum_of_numbers. It takes a number parameter and it adds all the numbers in that range.

def sum_of_numbers(n):
    sum_numbers = 0
    if n < 1:
        print(f"El número introducido es menor que 1, operación no posible")
        return
    for i in range(1, n + 1):
        sum_numbers += i
    return sum_numbers

n = int(input("Introduce un número entero: "))

sum_total = sum_of_numbers(n)
if sum_total:
    print(f"La suma total es de: {sum_total}")


# Declare a function named sum_of_odds. It takes a number parameter and it adds all the odd numbers in that range.

def sum_of_odds(n):
    suma_of_odds = 0
    if n < 1:
        print(f"El número introducido es menor que 1, operación no posible")
        return
    for i in range(1, n + 1):
        if i % 2 == 1:
            suma_of_odds += i
    return suma_of_odds

n = int(input("Introduce un número entero: "))

list_odds = sum_of_odds(n)
print(f"La suma de los números impares es: {list_odds}")

# Declare a function named sum_of_even. It takes a number parameter and it adds all the even numbers in that range.

def sum_of_even(n):
    suma_of_even = 0
    if n < 1:
        print(f"El número introducido es menor que 1, operación no posible")
        return
    for i in range(1, n + 1):
        if i % 2 == 0:
            suma_of_even += i
    return suma_of_even

n = int(input("Introduce un número entero: "))

list_even = sum_of_even(n)
print(f"La suma de los números pares es: {list_even}")


# Exercise level 2


# Declare a function named evens_and_odds . It takes a positive integer as parameter and it counts number of evens and odds in the number.

def evens_and_odds(n):
    contador_evens_numbers = 0
    contador_odds_numbers = 0
    if n < 1:
        print(f"El número introducido es menor que 1, operación no posible")
        return
    for i in range(1, n + 1):
        if i % 2 == 0:
            contador_evens_numbers += 1
        else:
            contador_odds_numbers += 1
    return contador_evens_numbers,contador_odds_numbers

n = int(input("Introduce un número entero: "))

contador_evens_numbers, contador_odds_numbers  = evens_and_odds(n)

print(f"El número de pares siendo n = {n} es de {contador_evens_numbers}")
print(f"El número de impares siendo n = {n} es de {contador_odds_numbers}")


# Call your function factorial, it takes a whole number as a parameter and it return a factorial of the number

def factorial(n):
    calculo_factorial = 1
    if n == 0:
        return 1
    elif n < 1:
        print(f"El número introducido es menor que 1, operación no posible")
        return
    for i in range(1, n +1):
        calculo_factorial *= i
    return calculo_factorial

n = int(input("Introduce un número entero: "))

factorial_de = factorial(n)
print(f"El factorial de {n} es {factorial_de}")


# Call your function is_empty, it takes a parameter and it checks if it is empty or not

def is_empty(param):
    # Verifica si el parámetro está vacío
    if not param:
        return True  # El parámetro está vacío
    else:
        return False  # El parámetro no está vacío

print(is_empty([]))  # True, una lista vacía
print(is_empty({}))  # True, un diccionario vacío
print(is_empty(""))  # True, una cadena vacía
print(is_empty([1, 2, 3]))  # False, una lista con elementos

# Write different functions which take lists. They should calculate_mean, calculate_median, calculate_mode, calculate_range, calculate_variance, calculate_std (standard deviation).


# Calcular la media:
def calcular_media(lista_media):
    lista_media_sumada = 0
    for i in lista_media:
        lista_media_sumada += i
    media_calculada = lista_media_sumada / len(lista_media)
    return media_calculada

lista_media = [2, 3, 3, 5, 7, 10]
media = calcular_media(lista_media)

print(f"La media de los números de la lista es {media}")

# Calcular mediana:
def calcular_mediana(lista_mediana_ordenada):
    if len(lista_mediana_ordenada) % 2 == 0:
        elemento1_par = lista_mediana_ordenada[len(lista_mediana_ordenada) // 2 - 1]  # Accedemos al valor del índice
        elemento2_par = lista_mediana_ordenada[len(lista_mediana_ordenada) // 2]
        elemento_final_par = (elemento1_par + elemento2_par) / 2
        return elemento_final_par
    else:
        elemento_final_impar= lista_mediana_ordenada[len(lista_mediana_ordenada) // 2]
    return elemento_final_impar

lista_mediana = [2, 3, 3, 5, 7, 10]
lista_mediana_ordenada = sorted(lista_mediana)
mediana = calcular_mediana(lista_mediana)

print(f"La mediana de la lista es {mediana}")


# Calcular moda:
def calcular_moda(lista_moda, frecuencia_moda):
    for number in lista_moda:
        frecuencia_moda[number] += 1
    moda = max(frecuencia_moda, key=frecuencia_moda.get)  # Busca la clave con el valor máximo. key=frecuencia_moda.get sirve para los valores asociados a las claves
    return moda

lista_moda = [2, 3, 3, 5, 7, 7, 7, 10]
frecuencia_moda = {2: 0, 3: 0, 5: 0, 7: 0, 10: 0 }

moda = calcular_moda(lista_moda, frecuencia_moda)
print(f"La moda en esta lista es {moda}")


# Calcular rango:
def calcular_rango(lista_rango):
    max_num = max(lista_rango)
    min_num = min(lista_rango)
    rango = max_num - min_num
    return rango

lista_rango = [2, 3, 7, 10, 1]

rango = calcular_rango(lista_rango)
print(f"El rango de la lista es {rango}")

# Exercises level 3 

# Write a function called is_prime, which checks if a number is prime.

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

n = int(input("Introduce el valor de n: "))

prime_check = is_prime(n)
if prime_check:
    print(f"El número {n} es primo")
else:
    print(f"El número {n} no es primo")


# Write a functions which checks if all items are unique in the list.

def unique_items(sorted_input_list_items):
    unique_items = []
    repeated_items = []
    for i in sorted_input_list_items:
        if i not in unique_items:
            unique_items.append(i)
        else:
            repeated_items.append(i)
    return unique_items, repeated_items

input_list_items = [27, 14, 89, 35, 14, 62, 76, 89, 48, 33]
sorted_input_list_items = sorted(input_list_items)

uniques_items, repeated_items = unique_items(sorted_input_list_items)
print(f"La lista con los numeros únicos es {uniques_items}")
print(f"La lista con los números repetidos es {repeated_items}")


# Write a function which checks if all the items of the list are of the same data type.

def tipos_de_dato(lista1):
    # Si la lista está vacía, consideramos que los elementos "son del mismo tipo" (no hay elementos a comparar)
    if not lista1:
        return True

    # Tipo de referencia: el tipo del primer elemento
    tipo_referencia = type(lista1[0])

    # Comprobamos si todos los elementos tienen el mismo tipo
    for i in lista1:
        if type(i) != tipo_referencia:
            return False
    return True

# Ejemplo de listas a evaluar
lista1 = [1, 2, 3]         # Todos los elementos son del mismo tipo (int)
lista2 = [1, "2", 3]       # Tipos mezclados (int y str)
lista3 = []                # Lista vacía
lista4 = [1]               # Solo un elemento

# Pruebas
print(tipos_de_dato(lista1))  # True
print(tipos_de_dato(lista2))  # False
print(tipos_de_dato(lista3))  # True
print(tipos_de_dato(lista4))  # True

# From this point on, functions are requested from Microsoft Copilot.

# 1. Función para sumar dos números

def suma(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        return f"Valor introducido diferente a entero o decimal"
    return a + b

a = float(input("Introduce el valor de a: "))
b = float(input("Introduce el valor de b: "))

resultado_suma = suma(a, b)
print(f"El resultado de la suma siendo a = {a} y b = {b} es: {round(resultado_suma, 2)}")

# 2. Determinar si un numero es par o impar

def verificar_par_o_impar(n):
    if n < 0:
        print(f"Número no valido, introduce otro")
    elif n % 2 == 0:
        print(f"El número {n} es par")
    else:
        print(f"El número {n} es impar")

n = int(input("Introduce el valor de n: "))

verificar_par_o_impar(n)
