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