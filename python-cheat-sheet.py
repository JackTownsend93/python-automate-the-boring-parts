# PYTHON CHEAT SHEET
# Quick reference file for language basics

# ----------------------------------------        STRINGS        ---------------------------------------- #
# Strings are denoteed by either ' ' or " "
string = 'Hello, world!'

# Useful string functions
string.find()
string.index()
string.isalnum()
string.isalpha()
string.isdecimal()
string.islower()
string.isupper()
string.startswith()
string.endswith()
string.join()
string.split()
string.ljust(20,' ')
string.center(20)
string.strip()

# ----------------------------------------         LISTS         ---------------------------------------- #
# Lists are ordered
list = ['1', '2', '3']  # Brackets

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

# ----------------------------------------        REGEXPS        ---------------------------------------- #
# For identifying and manipulation regular expressions
import re

# Compile converts the argument string into a Regex object
phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')

# Note: always pass RAW STRINGS to regexp functions to avoid having to contantly use escape characters, i.e.:
re.compile('\\d\\d\\d-\\d\\d\\d-\\d\\d\\d\\d') # Standard string with escape characters: messy and verbose

# Search returns a Match object if the pattern is found
mo = re.search('My number is 415-555-1234')
# Match objects have a group() method that can return the matched string
print('Phone number is: ' + mo.group())

# Groups are defined by parentheses
phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
mo = re.search('My number is 415-555-1234')
print('Phone number is: ' + mo.group(1) + mo.group(2)) # These groups can be accessed individually
mo.groups() # Plural groups returns all groups

# Pipes allow for multiple groups 
batRegex = re.compile(r'Bat(man|mobile|copter)') # Would find any of these words starting with bat

# Question marks allow optional matching
batRegex = re.compile(r'Bat(wo)?man') # Would find Batman or Batwoman

# Asterisk allow for matching zero or more (good for repeat patterns)
batRegex = re.compile(r'Bat(wo)*man') # Would find Batwowowowowoman and Batman

# Plus allows for matching one or more
batRegex = re.compile(r'Bat(wo)+man') # Would only find Batwoman or with any repeating amount of "wo"s

# Braces allow for specific repeat patterns
haRegex = re.compile(r'(Ha){3}') # Would find HaHaHa
haRegex = re.compile(r'(Ha){3,5}') # Would find HaHaHa (3), HaHaHaHa (4), and HaHaHaHaHa (5)

# Carets and dollar signs indicate the match must occur at the start and end respectively.
beginsWithHello = re.compile(r'^Hello')
endsWithNumber = re.compile(r'\d$')
# When used in combination you can check if the whole string matches.
beginsAndEndsWithNumber = re.compile(r'^\d+$')

# Dots are wildcards.
atRegex = re.compile(r'.at') # Will match any character + 'at'

# Dot asterisk matches everything.
nameRegex = re.compile(r'First Name: (.*) Last Name: (.*)') # Note: can be made non-greedy with (.*?)

# Greedy matching (default) will match the longest string possible.
# Non-greedy matching {}?  will match the shortest string possible.

# findall() returns every matched expression, whereas search() returns the first one
# If there are groups in the regular expression then finall() will return a list of tuples

# Character classes
'\d'    # Any numeric (d)igit from 0-9
'\D'    # Any character that is NOT the above
'\w'    # Any "(w)ord" character: letters, numeric digits, and underscores
'\W'    # Any character that is NOT the above
'\s'    # Any white(s)pace character: spaces, tabs, and newlines
'\S'    # Any character that is NOT the above

# Useful example:
xmasRegex = re.compile(r'\d+\s\w+')
xmasRegex.findall('5 rings, 4 birds, 3 hens, 2 doves, 1 partridge') # -> ['5 rings', '4 birds', ... etc]

# Custom character classes
vowelRegex = re.compile(r'[aeiouAEIOU]') # All vowels

# Use a caret to apply negative character class.
vowelRegex = re.compile(r'[^aeiouAEIOU]') # Not vowels