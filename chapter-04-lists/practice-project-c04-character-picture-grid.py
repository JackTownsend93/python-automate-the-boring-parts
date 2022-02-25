grid = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]


# Write function to flip x and y to rotate image 90deg.
def plot(grid):
    n_cols = len(grid[0])
    n_rows = len(grid)
    for y in range(n_cols):
        for x in range(n_rows):
            print(grid[x][y], end='')
        print()

if __name__ == '__main__':
    plot(grid)