
# EXERCISES 

# Declare your age as integer variable

age = 29

# Declare your height as a float variable

height = 1.76

# Declare a variable that store a complex number

complex_number = 3j

# Write a script that prompts the user to enter base and height of the triangle and calculate an area of this triangle (area = 0.5 x b x h)

base_triangle = float(input("Enter the base of the triangle: "))
height_triangle = float(input("Enter the height of the triangle: "))

area_triangle = 0.5 * base_triangle * height_triangle

print(f"The area of your triangle is: {round(area_triangle, 2)}")


# Write a script that prompts the user to enter side a, side b, and side c of the triangle. Calculate the perimeter of the triangle (perimeter = a + b + c)

side_a = float(input("Enter the a side: "))
side_b = float(input("Enter the b side: "))
side_c = float(input("Enter the c side: "))

perimeter = side_a + side_b + side_c

print(f"The perimeter of your triangle is {round(perimeter, 2)}")

# Get length and width of a rectangle using prompt. Calculate its area (area = length x width) and perimeter (perimeter = 2 x (length + width))

length_rectangle = float(input("Enter the length of the rectangle: "))
width_rectangle = float(input("Enter the width of the rectangle: "))

area_rectangle = length_rectangle * width_rectangle
print(f"The area of the rectangle you are calculating is: {round(area_rectangle, 2)}")

perimeter_rectangle = 2 * (length_rectangle + width_rectangle)
print(f"The perimeter of the rectangle you are calculating is: {round(perimeter_rectangle, 2)}")


# Get radius of a circle using prompt. Calculate the area (area = pi x r x r) and circumference (c = 2 x pi x r) where pi = 3.14.
import math


radius_circle = float(input("Enter the radius of the circle: "))

area_circle = math.pi * (radius_circle ** 2)
print(f"The area of the circle is: {round(area_circle, 2 )}")

circumference_circle = 2 * math.pi * radius_circle
print(f"The circumference of the circle is: {round(circumference_circle, 2)}")

# Calculate the slope, x-intercept and y-intercept of y = 2x -2 (y = mx + b)

m = 2 
b = -2

    # 1. Calcular la pendiente (ya sabemos que m es 2)

slope = m
print(f"The slope is: {slope}")

    # 2. Calcular el x-intercept (cuando y = 0)
x_intercept = -b / m  # Despejamos x de la ecuación y = mx + b
print(f"The x-intercept is: ({x_intercept}, 0)")

    # 3. Calcular el y-intercept (cuando x = 0)
y_intercept = b  # El valor de y cuando x = 0 es simplemente b
print(f"The y-intercept is: (0, {y_intercept})")


# Slope is (m = (y2 - y1) / (x2 - x1)). Find the slope and Euclidean (d = √(x2 - x1)**2 + (y2 - y1)**2) distance between point (2, 2) and point (6,10)

x1, y1 = 2, 2
x2, y2 = 6, 10

m2 = (y2 - y1) / (x2 - x1)

print(f"The slope between ({x1}, {y1}) and ({x2}, {y2}) is: {m2}")


import math

distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
print(f"The Euclidean distance between ({x1}, {y1}) and ({x2}, {y2}) is: {round(distance, 2)}")


# Compare the slopes in tasks 8 and 9.

print(f"Are slopes task 8 and task 9 equal? {slope == m2}")

# Calculate the value of y (y = x ** 2 + 6x + 9). Try to use different x values and figure out at what x value y is going to be 0

x_values = [-10, -5, -3, 0, 3, 10]

for x in x_values:
    y = x ** 2 + (6 * x) + 9
    print(f"The value of y where x = {x} is: {y}")


# Find the length of 'python' and 'dragon' and make a falsy comparison statement

length_python = len("Python")
length_dragon = len("Dragon")


print(f"Length of 'Python': {length_python}")
print(f"Length of 'Dragon': {length_dragon}")


print(f"Is 'Python' longer than 'Dragon'? {length_python > length_dragon}") 
print(f"Are 'Python' and 'Dragon' different in length? {length_python != length_dragon}")


# Use and operator to check if 'on' is found in both 'python' and 'dragon'

print(f"Is 'on' in both words?: {"on" in "python" and "on" in "dragon"}")


# I hope this course is not full of jargon. Use in operator to check if jargon is in the sentence.

print(f"Is 'Jargon' in the phrase?: {"jargon" in "I hope this course is not full of jargon"}")


# There is no 'on' in both dragon and python

print(f"Is 'on' in Dragon word?: {'on' in "dragon"}")

print(f"Is 'on' in Python word?: {'on' in "python"}")


# Find the length of the text python and convert the value to float and convert it to string

len_python = len("Python")
print(type(len_python))

len_python_float = float(len_python)
print(type(len_python_float))

len_python_str = str(len_python_float)
print(type(len_python_str))


# Even numbers are divisible by 2 and the remainder is zero. How do you check if a number is even or not using python?

dividends = [3, 8, 15, 22, 41]

for number in dividends:
    if number % 2 == 0:
        print(f"The number {number} is divisible by 2")
    else:
        print(f"The number {number} isn't divisible by 2")


# Check if the floor division of 7 by 3 is equal to the int converted value of 2.7

floor_division = 7 // 3

int_converted = int(2.7)

print(floor_division == int_converted)

print((7 // 3) == int(2.7))  # Easy way


# Check if type of '10' is equal to type of 10

print(type("10") == type(10))

# Check if int('9.8') is equal to 10

print(int(9.8) == 10)


# Write a script that prompts the user to enter hours and rate per hour. Calculate pay of the person?

work_hours = int(input("Enter your hours of work: "))

rate_hours = float(input("Enter your rate per hour of work: "))

pay = work_hours * rate_hours

print(f"Your payment of the month is {round(pay, 2)}")


# Write a script that prompts the user to enter number of years. Calculate the number of seconds a person can live. Assume a person can live hundred years


years = int(input("How many years you think you will live?: "))

seconds_in_a_year = 31_622_400

seconds_alive = years * seconds_in_a_year

print(f"You will live {seconds_alive} seconds")


# Write a Python script that displays the following table

print(1, 1, 1, 1, 1)
print(2, 1, 2, 4, 8)
print(3, 1, 3, 9, 27)
print(4, 1, 4, 16, 64)
print(5, 1, 5, 25, 125)