# Exercise 1 

# Iterate 0 to 10 using for loop, do the same using while loop

# for loop

for i in range(11):
    print(i)

# while loop 

i = 0

while i <= 10:
    print(i)
    i += 1


# Iterate 10 to 0 using for loop, do the same using while loop.

# for loop 

for i in range(10, -1, -1):
    print(i)


# while loop 

i = 10

while i >= 0:
    print(i)
    i -= 1

# Write a loop that makes seven calls to print(), so we get on the output the following triangle:

#
##
###
####
#####
######
#######

for i in range(1, 8):
    print('#' * i)

# Use nested loops to create the following:

# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #

tamaño = 8

for i in range(tamaño):
    for j in range(tamaño):
        print("#", end=" ")
    print()


# Print the following pattern:

# 0 x 0 = 0
# 1 x 1 = 1
# 2 x 2 = 4
# 3 x 3 = 9
# 4 x 4 = 16
# 5 x 5 = 25
# 6 x 6 = 36
# 7 x 7 = 49
# 8 x 8 = 64
# 9 x 9 = 81
# 10 x 10 = 100

i = 0
j = 0

while i * j <= 100:
    print(f"{i} x {j} = {i * j}")
    i += 1
    j += 1


# Iterate through the list, ['Python', 'Numpy','Pandas','Django', 'Flask'] using a for loop and print out the items.

librerias = ['Python', 'Numpy','Pandas','Django', 'Flask']

for elements in librerias:
    print(elements)


# Use for loop to iterate from 0 to 100 and print only even numbers

for i in range(0, 101):
    if i % 2 == 0:
        print(i)


# Use for loop to iterate from 0 to 100 and print only odd numbers.

for i in range(0, 101):
    if i % 2 != 0:
        print(i)


# Exercises 2 


# Use for loop to iterate from 0 to 100 and print the sum of all numbers

suma = 0

for i in range(0, 101):
    suma += i
print(f"The sum of all numbers is {suma}")

# Use for loop to iterate from 0 to 100 and print the sum of all evens and the sum of all odds.

even_numbers = 0
odd_numbers = 0

for i in range (0, 101):
    if i % 2 == 0:
        even_numbers += i
    else:
        odd_numbers += i
print(f"The sum of the evens is {even_numbers}, and the sum of all odds is {odd_numbers}")


# Exercises level 3


# Go to the data folder and use the countries.py file. Loop through the countries and extract all the countries containing the word land.

import countries

for countrie in countries.countries_list:
    if "land" in countrie:
        print(countrie)


# This is a fruit list ['banana', 'orange', 'mango', 'lemon'] reverse the order using loop.

fruit_list = ['banana', 'orange', 'mango', 'lemon']

fruit_reverse = list()

for i in range(len(fruit_list) - 1, -1, -1):  # Start en -1 ya que empezamos en el último elemento, stop en -1 ya que queremos acabar en 0 -1 = -1 
    fruit_reverse.append(fruit_list[i])
print(fruit_reverse)

# Go to the data folder and use the countries_data.py file.

# 1. What are the total number of languages in the data?

import countries_data

set_countries_languages = set()

for country in countries_data.countries_data_list: # Primero accedemos a cada pais
    for language in country["languages"]:          # Después accedemos a cada lenguaje
        set_countries_languages.add(language)

print(f"The total number of languages in the data is {len(set_countries_languages)}")


# Find the ten most spoken languages from the data

language_counts = dict()

for country in countries_data.countries_data_list:
    for language in country["languages"]:
        if language in language_counts:
            language_counts[language] += 1
        else:
            language_counts[language] = 1

sorted_languages = sorted(language_counts.items(), key=lambda item: item[1], reverse=True)
ten_max_language = sorted_languages[:10]

print(f"The ten most spoken languages are: {ten_max_language}")


# Find the 10 most populated countries in the world

ten_populated_countries = list()

for country in countries_data.countries_data_list:
    ten_populated_countries.append((country["name"], country["population"]))

sorted_population = sorted(ten_populated_countries, key=lambda x: x[1], reverse=True)
ten_populated_countries = sorted_population[:10]

print(f"The ten most populated countries in the world are: {ten_populated_countries}")

