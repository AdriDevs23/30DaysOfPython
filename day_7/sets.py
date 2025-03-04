# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

# EXERCISES 1

# Find the length of the set it_companies

print(len(it_companies))

# Add 'Twitter' to it_companies

it_companies.add("Twitter")
print(it_companies)

# Insert multiple IT companies at once to the set it_companies

it_companies.update(["Deloitte", "LG", "Logitech", "ASUS"])


# Remove one of the companies from the set it_companies

it_companies.remove("IBM")
print(it_companies)

# EXERCISES 2:


# Join A and B

C = A.union(B)


# Find A intersection B

C = A.intersection(B)
print(C)

# Is A subset of B

A.issubset(B)

# Are A and B disjoint sets

A.isdisjoint(B) 

# Join A with B and B with A

join = A.union(B)
other_join = B.union(A)

# What is the symmetric difference between A and B

symmetric_difference = A.symmetric_difference(B)
print(f"The symmetric difference between {A} and {B} is {symmetric_difference}")

# Delete the sets completely

del A, B, it_companies, age