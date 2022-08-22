---
layout: default
title: Prep 34
---

# Prep Problem - 34

In this problem, you should write one function named `swap`.
This function should have two parameter.
You can assume that the first parameter will be a dictionary, and the second a set.
The function should swap the key and value for all of the keys that exist in the dictionary that also exist in the set.
The function does not need to return a value.
For instance, the code:

```
dict_data = {'a':'b', 'c':'d', 'e':'f'}
set_data = {'c', 'e'}
swap(dict_data, set_data)
print(dict_data)
    
```

Should print

```
{'a': 'b', 'd': 'c', 'f': 'e'}
```

And the code:

```
dict_data = {23:24, 110:120, 50:45, 70:50, 57:1}
set_data = {23, 110, 57}
swap(dict_data, set_data)
print(dict_data)
```

Should print

```
{50: 45, 70: 50, 24: 23, 120: 110, 1: 57}
```

Make sure to include only the one function in your file.
The gradescope tests will call the functions to test them.
Name the program `prep34.py`.
Make sure that gradescope gives you the points for passing the test case.

