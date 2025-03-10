# Exercise 1 

# Get user input using input(“Enter your age: ”). If user is 18 or older, give feedback: You are old enough to drive. If below 18 give feedback to wait for the missing amount of years. 

user_input = int(input("Enter your age: ").strip())

if user_input >= 18:
    print("You're old enough to drive")
else:
    print(f"You need {18 - user_input} years to learn to drive")


# Compare the values of my_age and your_age using if … else. Who is older (me or you)? Use input(“Enter your age: ”) to get the age as input. You can use a nested condition to print 'year' for 1 year difference in age, 'years' for bigger differences, and a custom text if my_age = your_age.

my_age = 29
your_age = int(input("Enter your age to check our age difference: ").strip())

if my_age > your_age:
    diff = my_age - your_age
    print(f"I'm older than you by {diff} year{"s" if diff > 1 else ""}.")
elif my_age < your_age:
    diff = your_age - my_age
    print(f"You're older than me by {diff} year{"s" if diff > 1 else ""}.")
else:
    print("We have the same age")


# Get two numbers from the user using input prompt. If a is greater than b return a is greater than b, if a is less b return a is smaller than b, else a is equal to b.

a = float(input("Enter the first number: ").strip())
b = float(input("Enter the second number: ").strip())

if a > b:
    print(f"a = {a}  is greater than b = {b}")
elif a < b:
    print(f"a = {a} is smaller than b = {b}")
else:
    print(f"a = {a} is equal to b = {b}")


# Write a code which gives grade to students according to theirs scores:

student_grade = int(input("Enter your grade: ").strip())

if student_grade == 100:
    print(f"You're excelsior!")
elif 80 <= student_grade < 100:
    print(f"Your grade {student_grade} is A")
elif 70 <= student_grade > 80:
    print(f"Your grade {student_grade} is B")
elif 60 <= student_grade > 70:
    print(f"Your grade {student_grade} is C")
elif 50 <= student_grade > 60:
    print(f"Your grade {student_grade} is D")
else:
    print(f"Your grade {student_grade} is F")


# Check if the season is Autumn, Winter, Spring or Summer. If the user input is: September, October or November, the season is Autumn. December, January or February, the season is Winter. March, April or May, the season is Spring June, July or August, the season is Summer

autumn = ["September", "October", "November"]
winter = ["December", "January", "February"]
spring = ["March", "April", "May"]
summer = ["June", "July", "August"]

month = str(input("Enter the month you are: ").strip().capitalize())

if month in autumn:
    print(f"The month of {month} belongs to the autumn season.")
elif month in winter:
    print(f"The month of {month} belongs to the winter season.")
elif month in spring:
        print(f"The month of {month} belongs to the spring season.")
else:
    print(f"The month of {month} belongs to the summer season.")


# The following list contains some fruits:
# If a fruit doesn't exist in the list add the fruit to the list and print the modified list. If the fruit exists print('That fruit already exist in the list')

fruits = ['banana', 'orange', 'mango', 'lemon']

user_fruit = str(input("Enter a fruit: "). strip().lower())

if user_fruit not in fruits:
    fruits.append(user_fruit)
    print("That fruit doesn't exist! I will add it :)")
    print(fruits)
else:
    print("That fruit already exists in the list, try again!")


# Here we have a person dictionary. Feel free to modify it!

person={
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}

# Check if the person dictionary has skills key, if so print out the middle skill in the skills list.

if "skills" in person:
    middle_skill = person["skills"][len(person["skills"]) // 2]
    print(f"The middle skill is {middle_skill}")


# Check if the person dictionary has skills key, if so check if the person has 'Python' skill and print out the result.

if "skills" in person:
    if "Python" in person["skills"]:
        print("Python is in skills key")
    else:
        print("Python is not in skills key")


# If a person skills has only JavaScript and React, print('He is a front end developer'), if the person skills has Node, Python, MongoDB, print('He is a backend developer'), if the person skills has React, Node and MongoDB, Print('He is a fullstack developer'), else print('unknown title') - for more accurate results more conditions can be nested!

skills = set(person["skills"])  # Convertimos la lista a un set para comparaciones eficientes

if skills == {"JavaScript", "React"}:
    print("He's a Front End developer")
elif {"Node", "Python", "MongoDB"}.issubset(skills):  
    print("He's a Backend developer")
elif {"React", "Node", "MongoDB"}.issubset(skills):
    print("He's a Full Stack developer")
else:
    print("Unknown title")


# If the person is married and if he lives in Finland, print the information in the following format:  Asabeneh Yetayeh lives in Finland. He is married.

if person["is_marred"] == True and person["country"] == "Finland":
    print(f"{person['first_name']} {person['last_name']} lives in {person['country']}. He is married.")


# Here is more conditionals exercise to increase my conditional knowledge, thanks to ChatGPT


# Escribe un programa que pida al usuario ingresar un número y realice las siguientes verificaciones:

# Si el número es mayor que 0, imprime "El número es positivo".
# Si el número es igual a 0, imprime "El número es cero".
# Si el número es menor que 0, imprime "El número es negativo".
# Si el número es mayor que 100, imprime "El número es grande".
# Si el número es menor que -100, imprime "El número es muy negativo".
# Si el número está entre 0 y 100 (sin incluir 0), imprime "El número es pequeño".


user_number = float(input("Enter a number: "))

if user_number > 100:
    print("El número es grande")
elif 1 < user_number <= 100:
    print("El número es pequeño")
elif user_number > 0:
    print("El número es positivo")
elif user_number == 0:
    print("El número es igual a 0")
elif user_number < -100:
    print("El número es muy negativo")
else:
    print("El número es negativo")


# 🔹 Ejercicio: Número par o impar
# Pide al usuario que ingrese un número y determina si es par o impar.

numero_par = int(input("Enter your number: "))

if numero_par < 0:
    print("Numero negativo, prueba otra vez")
elif numero_par % 2 == 0:
    print("El numero es par")
else:
    print("El numero es impar")



# 🔹 Ejercicio 2: Mayor de edad
# Pide la edad del usuario e imprime si es mayor de edad (18 años o más) o menor de edad.

edad = int(input("Introduce tu edad: "))

if edad >= 18:
    print("Eres mayor de edad")
else:
    print("Eres menor de edad")


# 🔹 Ejercicio 3: Número positivo, negativo o cero
# Pide al usuario que ingrese un número y determina si es positivo, negativo o cero.

numero_positivo = float(input("Introduce un numero: "))

if numero_positivo > 0:
    print("El numero es positivo")
elif numero_positivo < 0:
    print("El numero es negativo")
else:
    print("El numero es 0")


# 🔹 Ejercicio 4: Calificación
# Pide al usuario su calificación en un examen y evalúa su nota:

# 90-100: Excelente
# 70-89: Aprobado
# 0-69: Suspenso

nota_user = float(input("Enter your calification: "))

if 100 >= nota_user >= 90:
    print("Excelente")
elif 89 >= nota_user >= 70:
    print("Aprobado")
else:
    print("Suspenso")

# 🔹 Ejercicio 5: Mayor de tres números
# Pide al usuario que ingrese tres números y determina cuál es el mayor.


numeros = input("Enter three numbers separated by commas: ").split(",")
numeros = [float(num.strip()) for num in numeros]
mayor_numero = max(numeros)

print(f"The largest number is: {mayor_numero}")

# Pide al usuario que ingrese tres longitudes de lados y determina si forman un triángulo equilátero, isósceles o escaleno.

lado_a = float(input("Introduce el lado a: "))
lado_b = float(input("Introduce el lado b: "))
lado_c = float(input("Intoduce el lado c: "))


if lado_a == lado_b == lado_c:
    print("Todos los lados son iguales, es un triangulo equilátero")
elif lado_a == lado_b or lado_a == lado_c or lado_b == lado_c:
    print("Dos lados son iguales, triangulo isósceles")
else:
    print("Ninguno de los lados son iguales, es un triangulo escaleno")


# Ejercicio: Calculadora simple
# Escribe un programa que le pida al usuario ingresar dos números y luego le pida que elija una operación (suma, resta, multiplicación o división). El programa debe realizar la operación elegida 
# y mostrar el resultado.

# Requisitos:

# El usuario debe ingresar dos números.
# El usuario debe elegir una operación de entre las siguientes:
# Sumar
# Restar
# Multiplicar
# Dividir

num1 = float(input("Introduce el primer numero: "))
num2 = float(input("Introduce el segundo numero: "))

operacion = input("Introduce la operación que quieres realizar (suma, + , resta, - , multiplicación, *,  o division, / ): ").lower()

if operacion == "suma" or operacion == "+":
    resultado = num1 + num2
    print(f"El resultado de la suma es {resultado}")
elif operacion == "resta" or operacion == "-":
    resultado = num1 - num2
    print(f"El resultado de la resta es {resultado}")
elif operacion == "multiplicacion" or operacion == "*":
    resultado = num1 * num2
    print(f"El resultado de la multiplicacion es {resultado}")
elif operacion == "division" or operacion == "/":
    if num2 == 0:
        print("Error, no se puede dividir entre 0")
    else:
        resultado = num1 / num2
        print(f"El resultado de la division es {resultado}")
else:
    print("No se contempla esa operación")


# Ejercicio: Calcular el área de una figura
# Pide al usuario que ingrese el tipo de figura (cuadrado, rectángulo, triángulo, círculo) y, dependiendo de la figura, pide las dimensiones necesarias para calcular el área. 
# Luego, calcula y muestra el área correspondiente.

# Instrucciones:

# Si el usuario elige cuadrado, pide el lado del cuadrado y calcula el área (lado * lado).
# Si el usuario elige rectángulo, pide la base y la altura y calcula el área (base * altura).
# Si el usuario elige triángulo, pide la base y la altura y calcula el área (base * altura / 2).
# Si el usuario elige círculo, pide el radio y calcula el área (π * radio²).
# Recuerda que el valor de π puede ser aproximado como 3.1416.

import math

figura = input("Elige la figura (cuadrado, rectángulo, triángulo, círculo): ").lower()

if figura == "cuadrado":
    lado_cuadrado = float(input("Introduce el valor del lado: "))
    area_cuadrado = lado_cuadrado * lado_cuadrado
    print(f"El área del cuadrado es {area_cuadrado}")
elif figura == "rectangulo":
    base_rectangulo = float(input("Introduce la base del rectangulo: "))
    altura_rectangulo = float(input("introduce la altura del rectangulo: "))
    area_rectangulo = base_rectangulo * altura_rectangulo
    print(f"El area del rectangulo es {area_rectangulo}")
elif figura == "triangulo":
    base_triangulo = float(input("Introduce la base del triangulo: "))
    altura_triangulo = float(input("Introduce la altura del triangulo: "))
    area_triangulo = base_triangulo * (altura_triangulo / 2)
    print(f"El area del triangulo es {area_triangulo}")
elif figura == "circulo":
    radio_circulo = float(input("Introduce el radio del circulo: "))
    area_circulo = math.pi * (radio_circulo ** 2)
    print(f"El area del circulo es {area_circulo}")
else:
    print("Error, operación no contemplada")


# Ejercicio: Sistema de clasificación de edad
# Pide al usuario que ingrese su edad y clasifica en las siguientes categorías:

#     Niño (0 - 12 años):

# Mensaje: "Eres un niño."

# Adolescente (13 - 17 años):

# Mensaje: "Eres un adolescente."

# Adulto (18 - 64 años):

# Mensaje: "Eres un adulto."

# Anciano (65 años o más):

# Mensaje: "Eres un anciano."

user_age = int(input("Introduce tu edad: "))

if 100 >= user_age >= 65:
    print("Eres un anciano")
elif 64 >= user_age >= 18:
    print("Eres un adulto")
elif 17 >= user_age >= 13:
    print("Eres un adolescente")
elif 12 >= user_age >= 0:
    print("Eres un niño")
else:
    print("Edad no válida o fuera de rango")


# Ejercicio: Clasificar un número según su signo

# Escribe un programa que pida al usuario que ingrese un número y clasifique ese número como:

# Positivo: Si el número es mayor que 0.
# Negativo: Si el número es menor que 0.
# Cero: Si el número es exactamente 0.

signal_number = float(input("Introduce un número: "))

if signal_number > 0:
    print("El número introducido es un numero positivo")
elif signal_number < 0:
    print("El número introducido es un número negativo")
else:
    print("El número es 0")


# Ejercicio: Pide al usuario que ingrese una calificación numérica (de 0 a 10) y evalúa si la calificación es suficiente para aprobar.

# Condiciones:

# Si la calificación es mayor o igual a 5, es aprobado.
# Si la calificación es menor que 5, es reprobado.
# Si la calificación está fuera del rango 0-10, muestra un mensaje de error.


calificacion = float(input("Introduce tu nota: "))

if 10 >= calificacion >= 5:
    print("Estás aprobado")
elif 5 > calificacion >= 0:
    print("Estás suspenso")
else:
    print("Introduce una nota entre 0 y 10")


# Ejercicio:
# Pide al usuario un año y determina si es un año bisiesto o no.

# Un año es bisiesto si:

# Es divisible por 4.
# No es divisible por 100, a menos que también sea divisible por 400.


año_bisiesto = int(input("Introduce un año: "))

if año_bisiesto % 4 == 0 and año_bisiesto % 100 != 0 or (año_bisiesto % 400 == 0):
    print(f"El año {año_bisiesto} es bisiesto")
else:
    print(f"El año {año_bisiesto} no es bisiesto")


# Ejercicio:
# Número mayor y menor: Pide al usuario que ingrese tres números y determina cuál es el mayor y cuál es el menor.

# Instrucciones:

# El programa debe pedir al usuario ingresar tres números.
# Luego, debe determinar cuál de esos tres números es el mayor y cuál es el menor.
# Imprimir ambos resultados (el mayor y el menor).

num_a = float(input("Introduce el primer numero: "))
num_b = float(input("Introduce el segundo numero: "))
num_c = float(input("Introduce el tercer numero: "))

max_num = max(num_a, num_b, num_c)
min_num = min(num_a, num_b, num_c)

print(f"El numero mayor es {max_num} y el menor es {min_num}")


# Ejercicio: Calculadora de IMC (Índice de Masa Corporal)
# Instrucciones:
# Pide al usuario que ingrese su peso en kilogramos.

# Pide al usuario que ingrese su altura en metros.

# Calcula el IMC usando la fórmula: IMC = peso / (altura ** 2).

# Usa condicionales para clasificar el IMC en las siguientes categorías:

# Menos de 18.5: Bajo peso

# Entre 18.5 y 24.9: Peso normal

# Entre 25 y 29.9: Sobrepeso

# 30 o más: Obesidad

# Muestra el IMC y la categoría correspondiente.


peso_usuario = float(input("Introduce tu peso en kilogramos: "))

altura_usuario = float(input("Ahora introduce tu altura en metros: "))

imc = peso_usuario / (altura_usuario ** 2)

if imc >= 30:
    print(f"Tú IMC es {round(imc, 2)}, Perteneces a la categoría: Obesidad")
elif 29.9 >= imc >= 25:
    print(f"Tú IMC es {round(imc, 2)}, Perteneces a la categoría: Sobrepeso")
elif 24.9 >= imc >= 18.5: 
    print(f"Tú IMC es {round(imc, 2)}, Perteneces a la categoría: Peso normal")
elif imc < 18.5:
    print(f"Tú IMC es {round(imc, 2)}, Perteneces a la categoría: Peso bajo")
else:
    print("Cálculos no posibles")


# Clasificación de calificaciones
# Instrucciones:
# Pide al usuario que ingrese una calificación numérica entre 0 y 100.

# Usa condicionales if-elif-else para clasificar la calificación en las siguientes categorías:

# Entre 90 y 100: A

# Entre 80 y 89: B

# Entre 70 y 79: C

# Entre 60 y 69: D

# Menos de 60: F

calificacion_usuario = float(input("Introduce tu nota entre 0 y 100: "))

if 100 >= calificacion_usuario >= 90:
    print("Calificación A")
elif 89 >= calificacion_usuario >= 80:
    print("Calificación B")
elif 79 >= calificacion_usuario >= 70:
    print("Calificación C")
elif 69 >= calificacion_usuario >= 60:
    print("Calificación D")
else:
    print("Calificación F")


# Ejercicio: Conversor avanzado de temperatura
# Instrucciones:
# Pide al usuario que ingrese una temperatura.

# Pide al usuario que indique la unidad de la temperatura ingresada (C para Celsius, F para Fahrenheit, o K para Kelvin).

# Usa condicionales if-elif-else para convertir la temperatura a las dos unidades restantes.

# Muestra la temperatura en las tres unidades: Celsius, Fahrenheit y Kelvin.

# Clasifica la temperatura en Celsius en las siguientes categorías:

# Menos de 0 grados Celsius: Temperatura bajo cero

# Entre 0 y 30 grados Celsius: Temperatura normal

# Más de 30 grados Celsius: Temperatura alta


temperatura = float(input("Introduce la temperatura: "))
unidad_temperatura = input("Indica la unidad de la temperatura (F = Farenheit, C = Celsius, K = Kelvin): ").lower()

if "c" in unidad_temperatura:
    celsius_farenheit = temperatura * 9/5 + 32
    celsius_kelvin = temperatura + 273.15
    print(f"La temperatura {temperatura}ºC equivale a {round(celsius_farenheit, 2)}ºF y {round(celsius_kelvin, 2)}ºK")
elif "k" in unidad_temperatura:
    kelvin_celsius = temperatura - 273.15
    kelvin_farenheit = (temperatura - 273.15) * 9/5 + 32
    print(f"La temperatura {temperatura}ºK equivale a {round(kelvin_celsius, 2)}ºC y {round(kelvin_farenheit, 2)}ºF")
elif "f" in unidad_temperatura:
    farenheit_celsius = (temperatura - 32) * 5/9
    farenheit_kelvin = (temperatura - 32) * 5/9 + 273.15
    print(f"La temperatura {temperatura}ºF equivale a {round(farenheit_celsius, 2)}ºC y {round(farenheit_kelvin, 2)}ºK")
else:
    print("Unidad no contemplada")


# Identificación del triángulo
# Instrucciones:
# Pide al usuario que ingrese las longitudes de los tres lados de un triángulo.

# Usa condicionales if-elif-else para determinar el tipo de triángulo en función de las longitudes de sus lados:

# Equilátero: todos los lados son iguales.

# Isósceles: dos lados son iguales.

# Escaleno: todos los lados son diferentes.

# Muestra el tipo de triángulo correspondiente.


triangulo_lado_a = float(input("Introduce el primer lado: "))
triangulo_lado_b = float(input("Introduce el segundo lado: "))
triangulo_lado_c = float(input("Introduce el tercer lado: "))

if triangulo_lado_a == triangulo_lado_b == triangulo_lado_c:
    print("Todos los lados son iguales, el triángulo es Equilátero")
elif triangulo_lado_a == triangulo_lado_b or triangulo_lado_a == triangulo_lado_c or triangulo_lado_b == triangulo_lado_c:
    if triangulo_lado_a == triangulo_lado_b:
        print(f"Los lados {triangulo_lado_a} y {triangulo_lado_b} son iguales, es un triangulo isósceles")
    elif triangulo_lado_a == triangulo_lado_c:
        print(f"Los lados {triangulo_lado_a} y {triangulo_lado_c} son iguales, es un triangulo isósceles")
    elif triangulo_lado_b == triangulo_lado_c:
        print(f"Los lados {triangulo_lado_b} y {triangulo_lado_c} son iguales, es un triangulo isósceles")
else:
    print("Todos los lados son diferentes, el triangulo es Escaleno")


# Ejercicio: Calculadora de descuento
# Instrucciones:
# Pide al usuario que ingrese el precio original de un producto.

# Pide al usuario que ingrese el porcentaje de descuento.

# Usa condicionales if-elif-else para calcular el precio final después de aplicar el descuento, considerando las siguientes reglas:

# Si el descuento es menor o igual al 10%, el precio final es simplemente el precio original menos el descuento.

# Si el descuento es mayor al 10% y menor o igual al 20%, aplica un descuento adicional del 5% sobre el precio reducido.

# Si el descuento es mayor al 20%, aplica un descuento adicional del 10% sobre el precio reducido.

# Muestra el precio original, el porcentaje de descuento aplicado y el precio final después del descuento.

precio_original = float(input("Introduce el precio de la compra: "))

porcentaje_descuento = int(input("Introduce el descuento: "))

if porcentaje_descuento <= 10:
    precio_descontado = precio_original * porcentaje_descuento / 100
    precio_total = precio_original - precio_descontado
    print(f"El precio original de la compra era de {precio_original} €, el descuento aplicado es del {porcentaje_descuento}% y el precio final con el descuento es de {precio_total} €")
elif 20 >= porcentaje_descuento >= 10:
    precio_descontado = precio_original * porcentaje_descuento / 100
    precio_descontado_adicional = precio_original * 5 / 100
    precio_total_descontado = precio_original - precio_descontado - precio_descontado_adicional
    print(f"El precio original de la compra era de {precio_original} €, el descuento aplicado es del {porcentaje_descuento}% y el precio final con el descuento añadido del 5% es de {precio_total_descontado} €")
elif porcentaje_descuento > 20:
    precio_descontado = precio_original * porcentaje_descuento / 100
    precio_descontado_adicional = precio_original * 10 / 100
    precio_total_descontado = precio_original - precio_descontado - precio_descontado_adicional
    print(f"El precio original de la compra era de {precio_original} €, el descuento aplicado es del {porcentaje_descuento}% y el precio final con el descuento añadido del 5% es de {precio_total_descontado} €")
else:
    print(f"El precio original se mantiene, siendo de {precio_original} €")
