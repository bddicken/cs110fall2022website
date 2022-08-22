
def get_highest_sum(number_grid):
    highest = -1
    for i in range(len(number_grid)):
        for j in range(len(number_grid[i])-1):
            val = number_grid[i][j] +  number_grid[i][j+1]
            if val > highest:
                highest = val
    return highest

'''
def main():
    grid = [[5, 4, 3, 2, 1],
            [7, 2, 9, 1, 2, 0, 9, 9],
            [1, 2, 1, 2, 0]]
    result = get_highest_sum(grid)
    print(result)
    
    grid = [[1, 2, 3, 4, 5], [7, 8, 1, 4, 2]]
    result = get_highest_sum(grid)
    print(result)
    
main()
'''

