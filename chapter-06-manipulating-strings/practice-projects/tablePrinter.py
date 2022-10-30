# tablePrinter.py - Takes a list of lists of strings and prints them as an organized table.

# Major assumption: all sublists are of equal length.

def printTable(tableData):
    # Determine longest string in each column to allow for correct column width
    colWidths = [0] * len(tableData)
    for cols in range(len(tableData)):
        for rows in range(len(tableData[0])):
            if len(tableData[cols][rows]) > colWidths[cols]:
                colWidths[cols] = len(tableData[cols][rows])

    # Print table
    for rows in range(len(tableData[0])):
        rowString = ''
        for cols in range(len(tableData)):
            rowString = ' '.join([rowString, tableData[cols][rows].rjust(colWidths[cols])])
        print(rowString)

if __name__ == "__main__":
    exampleText = [['apples', 'oranges', 'cherries', 'banana'],
                 ['Alice', 'Bob', 'Carol', 'David'],
                 ['dogs', 'cats', 'moose', 'goose']]

    printTable(exampleText)