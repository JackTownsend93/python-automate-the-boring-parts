# Write a function that takes a list value as an argument and returns a string with all the items separated by a comma and a space, with and inserted before the last item.

def list2str(listOfStrings):
    strOut = ''
    for i in range(len(listOfStrings)):
        if (i == len(listOfStrings) - 1):
            strOut += 'and ' + listOfStrings[i]
            break
        else:
            strOut += listOfStrings[i] + ', '
    return strOut

if __name__ == "__main__":
    spam = ['apples', 'bananas', 'tofu', 'cats']
    print(list2str(spam))
    