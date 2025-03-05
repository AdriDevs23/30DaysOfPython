# Create an empty dictionary called dog

dog = {}
other_dog = dict()

# Add name, color, breed, legs, age to the dog dictionary

dog.update(
    {"Name": "Felipe", 
    "Color": "Brown and white", 
    "Breed": "Yes", 
    "Legs": 4, 
    "Age": 3}
)

# Create a student dictionary and add first_name, last_name, gender, age, marital status, skills, country, city and address as keys for the dictionary
student = {
    "first_name": "Adrián",
    "last_name": "Carretero",
    "gender": "M",
    "age": 29,
    "marital_status": "married",
    "skills": ["HTML", "CSS", "starting with Python"],
    "country": "Spain",
    "city": "Madrid",
    "adress": "False street 123"
}

# Get the length of the student dictionary

print(len(student))

# Get the value of skills and check the data type, it should be a list

skills_values = student["skills"]
print(skills_values)

print(type(student["skills"]))


# Modify the skills values by adding one or two skills

student["skills"].extend(["JavaScript", "SQL"])

# Get the dictionary keys as a list

print(student.keys())

# Get the dictionary values as a list

print(student.values())

# Change the dictionary to a list of tuples using items() method

print(student.items())

# Delete one of the items in the dictionary

student.pop("adress")

# Other way
student.popitem()

# And other way
del student["gender"]

# Delete one of the dictionaries

del dog