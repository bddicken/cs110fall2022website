import prep34

grid = [[5, 4, 3, 2, 1, 7],
        [1, 2, 3, 0, 0, 7],
        [7, 2, 8, 1, 2, 7],
        [7, 2, 8, 1, 2, 3],
        [1, 2, 1, 9, 0, 7]]
result = prep34.get_highest_neighbor(grid, 3, 4)
print(result)

