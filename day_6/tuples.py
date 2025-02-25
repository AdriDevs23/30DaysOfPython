# Create an empty tuple

empty_tuple = ()
other_empty_tuple = tuple()

# Create a tuple containing names of your sisters and your brothers (imaginary siblings are fine)

brothers_tuple = ("Álvaro", "Garza", "Héctor", "Samuga")
sisters_tuple = ("Ana", "Lucía", "María", "Sofía")

# Join brothers and sisters tuples and assign it to siblings

siblings_tuple = brothers_tuple + sisters_tuple

# How many siblings do you have?

print(f"I have {len(siblings_tuple)} siblings")

# Modify the siblings tuple and add the name of your father and mother and assign it to family_members

family_members = siblings_tuple + ("Pedro", "Ana Isabel")
print(family_members)

# Unpack siblings and parents from family_members

*siblings, father, mother = family_members

print(f"The siblings are {siblings}")
print(f"And parents are {father}, {mother}")

# Create fruits, vegetables and animal products tuples. Join the three tuples and assign it to a variable called food_stuff_tp.

fruits_tuple = ("Apple", "Banana", "Watermelon")
vegetables_tuple = ("Tomato", "Potato", "Ginger")
animal_product_tuple = ("Meat", "Milk", "Blood")
food_stuff_tp = fruits_tuple + vegetables_tuple + animal_product_tuple

# Change the about food_stuff_tp tuple to a food_stuff_lt list

food_stuff_lt = list(food_stuff_tp)

# Slice out the middle item or items from the food_stuff_tp tuple or food_stuff_lt list.

food_stuff_tp_len = len(food_stuff_tp) // 2
print(food_stuff_tp[food_stuff_tp_len - (len(food_stuff_tp) % 2 == 0): food_stuff_tp_len + 1])

# Slice out the first three items and the last three items from food_staff_lt list

food_stuff_lt_sliced = food_stuff_lt[3:-3]

# Delete the food_staff_tp tuple completely

del food_stuff_tp

# Check if an item exists in tuple: nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')

nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')

# Check if 'Estonia' is a nordic country

print('Estonia' in nordic_countries)

# Check if 'Iceland' is a nordic country

print('Iceland' in nordic_countries)