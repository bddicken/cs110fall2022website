---
layout: default
title: Prep 31
---

# Prep Problem - 31

In this problem, you should write one function named `get_elements`.
This function should have two parameters.
You can assume that the first will be a dictionary with strings as keys and ints as values.
The second parameter will be an int.
The function should return a list containing all of the values who fall into at least one of these three categories:

* The corresponding key starts with an upper-case letter
* The corresponding key ends with an upper-case letter
* The value is greater than or equal to the second parameter integer

For instance, the code:



```
data = {'Alpha':10, 'bravo':25, 'charliE':15, 'dELTa':2}
numbers = get_elements(data, 12)
print(numbers)
```

Could print

```
[10, 25, 15]
```

Make sure to include only the one function in your file.
The gradescope tests will call the functions to test them.
Name the program `prep31.py`.
Make sure that gradescope gives you the points for passing the test case.


