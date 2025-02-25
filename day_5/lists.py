# EXERCISE 1

# Declare an empty list

empty_list = []

empty_second_list =list()


# Declare a list with more than 5 items

item_list = ["Adrian", "Carretero", 29, 1.77, "Rayo Vallecano", "Hollow Knight"]

# Find the length of your list 

print(len(item_list))


# Get the first item, the middle item and the last item of the list


print(item_list[0]) # First item

middle_index = len(item_list) // 2
print(item_list[middle_index])  # Middle item

print(item_list[-1]) # Last item


# Declare a list called mixed_data_types, put your(name, age, height, marital status, address)

mixed_data_types = ["Adrian", 29, 1.77, "married", "Madrid"]

# Declare a list variable named it_companies and assign initial values Facebook, Google, Microsoft, Apple, IBM, Oracle and Amazon.

it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]

# Print the list using print()

print(it_companies)

# Print the number of companies in the list

print(len(it_companies))

# Print the first, middle and last company

print(it_companies[0]) #First Company

it_companies_middle = len(it_companies) // 2
print(it_companies[it_companies_middle])  # Middle company

print(it_companies[-1])

# Print the list after modifying one of the companies

it_companies.append("Logitech")
print(it_companies)

# Add an IT company to it_companies

it_companies.insert(3, "Huawei")

print(it_companies)

# Insert an IT company in the middle of the companies list

it_companies.insert(len(it_companies) // 2, "Panasonic")
print(it_companies)

# Change one of the it_companies names to uppercase (IBM excluded!)

it_companies[0] = it_companies[0].upper()

print(it_companies)


# Join the it_companies with a string '#;  '

it_companies_joined = "#; ".join(it_companies)

print(it_companies_joined)

# Check if a certain company exists in the it_companies list.

company = "LG"
print(company in it_companies)

company = "Google"
print(company in it_companies)

# Sort the list using sort() method

it_companies_sorted = sorted(it_companies)
print(it_companies_sorted)

# Reverse the list in descending order using reverse() method

it_companies_sorted.reverse() 
print(it_companies_sorted)


# Slice out the first 3 companies from the list

it_companies_first_slice = it_companies[0:3]
print(it_companies_first_slice)

# Slice out the last 3 companies from the list

it_companies_last_slice = it_companies[-3:]
print(it_companies_last_slice)

# Slice out the middle IT company or companies from the list

it_companies_middle = len(it_companies) // 2
print(it_companies[it_companies_middle])

# Remove the first IT company from the list

it_companies.pop(0)
print(it_companies)


# Remove the middle IT company or companies from the list

it_companies_middle = len(it_companies) // 2
it_companies.pop(it_companies_middle)
print(it_companies)

# Remove the last IT company from the list

it_companies.pop(-1)
print(it_companies)

# Remove all IT companies from the list

it_companies.clear()
print(it_companies)

# Destroy the IT companies list

del it_companies
# print(it_companies) -> Output: NameError: name 'it_companies' is not defined


# Join the following lists:

front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']

# After joining the lists in question 26. Copy the joined list and assign it to a variable full_stack, then insert Python and SQL after Redux.

full_stack = front_end + back_end
full_stack.insert(full_stack.index('Redux') + 1, 'Python')
full_stack.insert(full_stack.index('Python') + 1, 'SQL')
print(full_stack)

# EXERCISE 2 

# The following is a list of 10 students ages:

ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

# Sort the list and find the min and max age

ages.sort()
print(ages)

min_age = min(ages)
max_age = max(ages)

print(f"The min age is {min_age}")
print(f"The max age is {max_age}")

# Add the min age and the max age again to the list

ages.insert(6, min_age)
ages.insert(1, max_age)
print(ages)

# Find the median age (one middle item or two middle items divided by two)

ages.sort()
n = len(ages)
median_age = (ages[(n-1)//2] + ages[n//2]) / 2
print("The median age is:", median_age)

# Find the average age (sum of all items divided by their number)

ages_len = len(ages)
ages_sum = sum(ages)
print(f"The average age is: {ages_sum / ages_len}")

# Find the range of the ages (max minus min)

min_age = min(ages)
max_age = max(ages)
print(f"The range of the ages is: {max_age - min_age}")

# Compare the value of (min - average) and (max - average), use abs() method

min_age = min(ages)
max_age = max(ages)
ages_len = len(ages)
ages_sum = sum(ages)
average_age = ages_sum / ages_len
absolute_value_min = abs(min_age - average_age)  # abs() convert to positive the result
absolute_value_max = abs(max_age - average_age)
print(f"The absolute value of the min age is: {absolute_value_min}")
print(f"The absolute value of the max age is: {absolute_value_max}")
print(absolute_value_min == absolute_value_max)

# Find the middle country(ies) in the contries list
countries = [
  'Afghanistan',
  'Albania',
  'Algeria',
  'Andorra',
  'Angola',
  'Antigua and Barbuda',
  'Argentina',
  'Armenia',
  'Australia',
  'Austria',
  'Azerbaijan',
  'Bahamas',
  'Bahrain',
  'Bangladesh',
  'Barbados',
  'Belarus',
  'Belgium',
  'Belize',
  'Benin',
  'Bhutan',
  'Bolivia',
  'Bosnia and Herzegovina',
  'Botswana',
  'Brazil',
  'Brunei',
  'Bulgaria',
  'Burkina Faso',
  'Burundi',
  'Cambodia',
  'Cameroon',
  'Canada',
  'Cape Verde',
  'Central African Republic',
  'Chad',
  'Chile',
  'China',
  'Colombi',
  'Comoros',
  'Congo (Brazzaville)',
  'Congo',
  'Costa Rica',
  "Cote d'Ivoire",
  'Croatia',
  'Cuba',
  'Cyprus',
  'Czech Republic',
  'Denmark',
  'Djibouti',
  'Dominica',
  'Dominican Republic',
  'East Timor (Timor Timur)',
  'Ecuador',
  'Egypt',
  'El Salvador',
  'Equatorial Guinea',
  'Eritrea',
  'Estonia',
  'Ethiopia',
  'Fiji',
  'Finland',
  'France',
  'Gabon',
  'Gambia, The',
  'Georgia',
  'Germany',
  'Ghana',
  'Greece',
  'Grenada',
  'Guatemala',
  'Guinea',
  'Guinea-Bissau',
  'Guyana',
  'Haiti',
  'Honduras',
  'Hungary',
  'Iceland',
  'India',
  'Indonesia',
  'Iran',
  'Iraq',
  'Ireland',
  'Israel',
  'Italy',
  'Jamaica',
  'Japan',
  'Jordan',
  'Kazakhstan',
  'Kenya',
  'Kiribati',
  'Korea, North',
  'Korea, South',
  'Kuwait',
  'Kyrgyzstan',
  'Laos',
  'Latvia',
  'Lebanon',
  'Lesotho',
  'Liberia',
  'Libya',
  'Liechtenstein',
  'Lithuania',
  'Luxembourg',
  'Macedonia',
  'Madagascar',
  'Malawi',
  'Malaysia',
  'Maldives',
  'Mali',
  'Malta',
  'Marshall Islands',
  'Mauritania',
  'Mauritius',
  'Mexico',
  'Micronesia',
  'Moldova',
  'Monaco',
  'Mongolia',
  'Morocco',
  'Mozambique',
  'Myanmar',
  'Namibia',
  'Nauru',
  'Nepal',
  'Netherlands',
  'New Zealand',
  'Nicaragua',
  'Niger',
  'Nigeria',
  'Norway',
  'Oman',
  'Pakistan',
  'Palau',
  'Panama',
  'Papua New Guinea',
  'Paraguay',
  'Peru',
  'Philippines',
  'Poland',
  'Portugal',
  'Qatar',
  'Romania',
  'Russia',
  'Rwanda',
  'Saint Kitts and Nevis',
  'Saint Lucia',
  'Saint Vincent',
  'Samoa',
  'San Marino',
  'Sao Tome and Principe',
  'Saudi Arabia',
  'Senegal',
  'Serbia and Montenegro',
  'Seychelles',
  'Sierra Leone',
  'Singapore',
  'Slovakia',
  'Slovenia',
  'Solomon Islands',
  'Somalia',
  'South Africa',
  'Spain',
  'Sri Lanka',
  'Sudan',
  'Suriname',
  'Swaziland',
  'Sweden',
  'Switzerland',
  'Syria',
  'Taiwan',
  'Tajikistan',
  'Tanzania',
  'Thailand',
  'Togo',
  'Tonga',
  'Trinidad and Tobago',
  'Tunisia',
  'Turkey',
  'Turkmenistan',
  'Tuvalu',
  'Uganda',
  'Ukraine',
  'United Arab Emirates',
  'United Kingdom',
  'United States',
  'Uruguay',
  'Uzbekistan',
  'Vanuatu',
  'Vatican City',
  'Venezuela',
  'Vietnam',
  'Yemen',
  'Zambia',
  'Zimbabwe',
]

countries_len = len(countries) // 2
print(countries[countries_len - (len(countries) % 2 == 0): countries_len + 1])

# Divide the countries list into two equal lists if it is even if not one more country for the first half.

mid = (len(countries) + 1) // 2
first_half, second_half = countries[:mid], countries[mid:]
print(first_half)
print(second_half)

# ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']. Unpack the first three countries and the rest as scandic countries.

countries = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
first, second, third, *scandic = countries

print(f"The non-Scandic countries are: {first}, {second}, {third}")
print(f"The Scandic countries are: {scandic}")
