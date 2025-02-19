# 'Day 2: 30 Days of python programming'


# EXERCISE 1

# Declare a first name variable and assign a value to it

first_name = "Adrián"

# Declare a last name variable and assign a value to it

last_name = "Carretero"

# Declare a full name variable and assign a value to it

full_name = "Adrián Carretero"

# Declare a country variable and assign a value to it

country = "Spain"

# Declare a city variable and assign a value to it

city = "Madrid"

# Declare an age variable and assign a value to it

age = 29

# Declare a year variable and assign a value to it

year = 1995

# Declare a variable is_married and assign a value to it

is_married = True

# Declare a variable is_true and assign a value to it

is_true = True

# Declare a variable is_light_on and assign a value to it

is_light_on = False

# Declare multiple variable on one line

artist, album_name, album_year, favourite_song = "Love of Lesbian", "Ejercito de salvación", 2024, "Canción de emergencias"

print(f"My favourite artist is {artist} with the disc {album_name} published in {album_year} and my favourite song of the tour is {favourite_song}.")



# EXERCISE 2


# Check the data type of all your variables using type() built-in function

print(type(first_name))
print(type(last_name))
print(type(full_name))
print(type(country))
print(type(city))
print(type(age))
print(type(year))
print(type(is_married))
print(type(is_true))
print(type(is_light_on))

# Using the len() built-in function, find the length of your first name

print(len(first_name))

# Compare the length of your first name and your last name

len_first_name = len(first_name)
len_last_name = len(last_name)
print(len_first_name == len_last_name)

# Declare 5 as num_one and 4 as num_two

num_one = 5
num_two = 4

# Add num_one and num_two and assign the value to a variable total

total = num_one + num_two
print(total)

# Subtract num_two from num_one and assign the value to a variable diff

diff = num_one - num_two
print(diff)

# Multiply num_two and num_one and assign the value to a variable product

product = num_one * num_two
print(product)

# Divide num_one by num_two and assign the value to a variable division

division = num_one / num_two
print(division)

# Use modulus division to find num_two divided by num_one and assign the value to a variable remainder

remainder = num_two % num_one
print(remainder)

# Calculate num_one to the power of num_two and assign the value to a variable exp

exp = num_one ** num_two
print(exp)

# Find floor division of num_one by num_two and assign the value to a variable floor_division

floor_division = num_one // num_two
print(floor_division)

# The radius of a circle is 30 meters.
# Calculate the area of a circle and assign the value to a variable name of area_of_circle

import math

radius = 30
area_of_circle = (math.pi * (radius ** 2))
print(area_of_circle)

# Calculate the circumference of a circle and assign the value to a variable name of circum_of_circle

import math

radius = 30
circum_of_circle = 2 * math.pi * radius
circum_rounded = round(circum_of_circle, 2)  # Round: Redondeo a dos dígitos
print(circum_rounded)

# Take radius as user input and calculate the area.

import math

radius = float(input("What radius do you want?: "))
area = (math.pi * (radius ** 2))
area_rounded = round(area, 2)
print(f"The area of your circle is {area_rounded}")

# Use the built-in input function to get first name, last name, country and age from a user and store the value to their corresponding variable names

first_name_input = str(input("Write your first name please: "))
last_name_input = str(input("Now, tell me your last name: "))
country_input = str(input(f"Where are you from {first_name_input}? "))
age_input = int(input("How old are you? "))

dictionary_input = {"Name:": first_name_input, "Last name: ": last_name_input, "Country: ": country_input, "Age: ": age_input}
print(dictionary_input)

# Run help('keywords') in Python shell or in your file to check for the Python reserved words or keywords

# Cheked on the PowerShell Terminal 