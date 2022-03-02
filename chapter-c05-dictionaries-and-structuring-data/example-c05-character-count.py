# Count number of occurances of each character in the string "message".
message = 'It was a bright cold day in April, nad the clocks were striking thirteen.'
count = {} # initialises the count dictionary.

for character in message:
    count.setdefault(character, 0) # Avoids adding 1 to non-existant key, but does not increment the value (default is zero).
    count[character] = count[character] + 1

print(count)