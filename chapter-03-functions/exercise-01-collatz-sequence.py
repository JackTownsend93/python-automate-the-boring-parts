def collatz(number):
    if number % 2 == 0:
        return number // 2 # even.
    else:
        return 3 * number + 1 # odd.

print('Enter an integer')
try: 
    number = int(input())
    while not (number == 1):
        number = collatz(number)
        print(number)

except:
    print('Error: you must enter an integer.')
