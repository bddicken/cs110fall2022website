---
layout: default
title: Prep 37
---

# Prep Problem - 37

In this problem, you should write one function named `get_highest_neighbor`.
This function should have three parameters.
The fist will be a 2D list of numeric values, and the second and third will be integers, representing a zero-based row/column position within the 2D list.
This function should look at the 4 "neighbors" of the number at the position specified by the second and third parameters
(the neighbor "above" it, "below" it, to the "left" of it, and to the "right" of it).
The function should return the largest value of these four neighbors.
You can assume that the grid will contain numbers greater than or equal to zero.

For instance, the code:

```
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
```

Should print

```
8
4
9
```

Make sure to include only the one function in your file.
The gradescope tests will call the functions to test them.
Name the program `prep37.py`.
Make sure that gradescope gives you the points for passing the test case.

