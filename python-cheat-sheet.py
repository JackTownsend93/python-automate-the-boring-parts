# PYTHON CHEAT SHEET
# Quick reference file for language basics

# ----------------------------------------         LISTS         ---------------------------------------- #
# Lists are ordered
list = ['1', '2', '3']     # Brackets

firstItem = list[0]     # Index from beginning
lastItem = list[-1]     # Index from end

# Looping through lists
for item in list:
    print(list)

list.append('newItem')  # Appending to lists

# The following methods achieve the same result
# - Method 1
for x in range(1,11):
    list.append(x**2)
# - Method 2
list = [x**2 for x in range(1,11)]

# Slicing lists
listSlice = list[:2]    # Slices first two indices
listCopy = list[:]      # Slices all indices (i.e., copies the whole list)


# ----------------------------------------         TUPLES        ---------------------------------------- #
# Tuples are essentially lists that cannot be edited
tuple = ('1', '2', '3')    # Parentheses


# ----------------------------------------      DICTIONARIES     ---------------------------------------- #
# Each dictionary item is a key-value pair
dictionary = {'key1': 1, 'key2': 2, 'key3': 3}  # Braces

keyValue1 = dictionary['key1']  # Accessing a value with its key
dictionary['key4'] = 4          # Adding a new key-value pair

# Looping through all key-value pairs
for k, v in dictionary.items():
    print('key: ' + str(k) + ' value: ' + str(v))
# Looping through all keys
for k in dictionary.keys():
    print(k)
# Looping through all values
for v in dictionary.values():
    print(v)


# ----------------------------------------     IF STATEMENTS     ---------------------------------------- #
# Lists
item in list
item not in list

# if-else statements
number = 1
if number > 1:
    print('that is big!')
elif item < 1:
    print('thath is small!')
else:
    print('must be 1!')
