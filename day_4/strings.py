# Concatenate the string 'Thirty', 'Days', 'Of', 'Python' to a single string, 'Thirty Days Of Python'.

print("Thirty " + "Days " + "Of " + "Python")

# Concatenate the string 'Coding', 'For' , 'All' to a single string, 'Coding For All'.

print("Coding " + "For " + "All")


# Declare a variable named company and assign it to an initial value "Coding For All".


company = "Coding For All"

# Print the variable company using print().

print(company)


# Print the length of the company string using len() method and print().


print(len(company))


# Change all the characters to uppercase letters using upper() method


print(company.upper())

# Change all the characters to lowercase letters using lower() method


print(company.lower())


# Use capitalize(), title(), swapcase() methods to format the value of the string Coding For All.

print(company.capitalize())
print(company.title())
print(company.swapcase())


# Cut(slice) out the first word of Coding For All string.

print(company[0])


# Check if Coding For All string contains a word Coding using the method index, find or other methods.

print("Coding" in company)


# Replace the word coding in the string 'Coding For All' to Python.

company_updated = company.replace("Coding", "Python")

print(company_updated)


# Change Python for Everyone to Python for All using the replace method or other methods

company = "Python for Everyone"

company_updated = company.replace("Everyone", "All")

print(company_updated)

# Split the string 'Coding For All' using space as the separator (split()) .

company_splited = company.split()

print(company_splited)


# "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" split the string at the comma.


companys = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"

companys_splited = companys.split(", ")

print(companys_splited)


# What is the character at index 0 in the string Coding For All.

company = "Coding For All"
print(company[0])


# What is the last index of the string Coding For All.

company = "Coding For All"
print(company[-1])


# What character is at index 10 in "Coding For All" string.


company = "Coding For All"
print(company[10])


# Create an acronym or an abbreviation for the name 'Python For Everyone'.


phrase = "Python For Everyone"

acronym = "".join([word[0] for word in phrase.split()]) # Tomar la primera letra de cada palabra y unirlas

print(acronym)


# Create an acronym or an abbreviation for the name 'Coding For All'.

phrase = "Coding For All"

acronym = "".join([word[0] for word in phrase.split()]) # Tomar la primera letra de cada palabra y unirlas

print(acronym)


# Use index to determine the position of the first occurrence of C in Coding For All.

phrase = "Coding For All" 

print(phrase.index("C"))


# Use index to determine the position of the first occurrence of F in Coding For All.

phrase = "Coding For All" 

print(phrase.index("F"))


# Use rfind to determine the position of the last occurrence of l in Coding For All People.

phrase = "Coding For All People" 

print(phrase.rfind("l"))

# Use index or find to find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'


phrase = "You cannot end a sentence with because because because is a conjunction"


print(phrase.index("because"))


# Use rindex to find the position of the last occurrence of the word because in the following sentence: 'You cannot end a sentence with because because because is a conjunction'


phrase = "You cannot end a sentence with because because because is a conjunction"


print(phrase.rindex("because"))


# Slice out the phrase 'because because because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'


phrase = "You cannot end a sentence with because because because is a conjunction"


print(phrase.find("because"))


print(phrase.find("is"))

print(phrase[31:54])


# Find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'

phrase = "You cannot end a sentence with because because because is a conjunction"

print(phrase.index("because"))


# Slice out the phrase 'because because because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'


phrase = "You cannot end a sentence with because because because is a conjunction"


print(phrase.index("because"))

print(phrase.rindex("because "))


print(phrase[31:54])


# Does ''Coding For All' start with a substring Coding?


phrase = "Coding For All"

print(phrase.startswith("Coding"))


# Does 'Coding For All' end with a substring coding?


phrase = "Coding For All"

print(phrase.endswith("coding"))


# '   Coding For All      '  , remove the left and right trailing spaces in the given string.


phrase = "   Coding For All      "

print(phrase.strip())


# Which one of the following variables return True when we use the method isidentifier():
# 30DaysOfPython
# thirty_days_of_python


daysOf = "30DaysOfPython"
days_of = "thirty_days_of_python"


print(daysOf.isidentifier())
print(days_of.isidentifier())


# The following list contains the names of some of python libraries: ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']. Join the list with a hash with space string.


libraries = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']


libraries_joined = " # ".join(libraries)

print(libraries_joined)


# Use the new line escape sequence to separate the following sentences

print("I am enjoying this challenge. \n I just wonder what is next." )



# Use a tab escape sequence to write the following lines.


print("Name \t Age \t Country \t City")
print("Asabeneh \t 250 \t Finland \t Helsinki")


# Use the string formatting method to display the following: radius = 10 / area = 3.14 * radius ** 2 / The area of a circle with radius 10 is 314 meters square.


radius = 10
area = 3.14 * radius ** 2

# The three ways of print a string
print(f"The area of a circle with radius {radius} is {area} meters square.")

print("The area of a circle with radius %d is %d meters square" %(radius, area))

print("The area of a circle with radius {} is {} meters square." .format(radius, area))


# Make the following using string formatting methods:

a = 8
b = 6

# 8 + 6 = 14
print(f"{a} + {b} = {a + b}")

# 8 - 6 = 2
print(f"{a} - {b} = {a - b}")

# 8 * 6 = 48
print(f"{a} * {b} = {a * b}")

# 8 / 6 = 1.33
print(f"{a} / {b} = {round(a / b, 2)}")

# 8 % 6 = 2
print(f"{a} % {b} = {a % b}")

# 8 // 6 = 1
print(f"{a} // {b} = {a // b}")

# 8 ** 6 = 262144
print(f"{a} ** {b} = {a ** b}")