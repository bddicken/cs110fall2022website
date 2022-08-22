---
layout: default
title: Prep 33
---

# Prep Problem - 33

In this problem, you should write one function named `longest_string`.
This function should have one parameter, which you can assume will be a list of dictionaries.
The keys in each dictionary could be of various types, but you may assume that the values will be strings.
The function should return the longest string *value* from all of the dictionaries in the list.
For instance, the code:

```
data = [{'a':'horse', 'b':'caterpillar'}, {'a':'camp', 'c':'joker'}]
result = longest_string(data)
print(result)
```

Should print

```
caterpillar
```

And the code:

```
data = [{1:'abc', 5:'onetwothree'}, {2:'abcd'}, {7:'one two three'}]
result = longest_string(data)
print(result)
```

Should print

```
one two three
```

Make sure to include only the one function in your file.
The gradescope tests will call the functions to test them.
Name the program `prep33.py`.
Make sure that gradescope gives you the points for passing the test case.

