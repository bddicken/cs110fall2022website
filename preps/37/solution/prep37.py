
def get_highest_neighbor(number_grid, row, col):
    highest = -1
    if number_grid[row][col+1] > highest:
        highest = number_grid[row][col+1]
    if number_grid[row][col-1] > highest:
        highest = number_grid[row][col-1]
    if number_grid[row+1][col] > highest:
        highest = number_grid[row+1][col]
    if number_grid[row-1][col] > highest:
        highest = number_grid[row-1][col]
    return highest

'''
def main():
    grid = [[5, 4, 3, 2, 1],
            [1, 2, 3, 0, 0],
            [7, 2, 8, 1, 2],
            [1, 2, 1, 9, 0]]
    result = get_highest_neighbor(grid, 1, 2)
    print(result)
    result = get_highest_neighbor(grid, 1, 1)
    print(result)
    result = get_highest_neighbor(grid, 2, 3)
    print(result)
    
main()
'''

