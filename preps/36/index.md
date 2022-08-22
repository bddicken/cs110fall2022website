---
layout: default
title: Prep 36
---

# Prep Problem - 36

Most airlines have restrictions on what a customer is allowed to put in their carry-on luggage when going on a flight.
For many plane tickets, customers are restricted to one carry-on bag (such as a small rolling suitcase) and one personal item (such as a backpack or purse).
There are also restrictions on the kind of things you can carry in these bags (for instance, no knives longer than some length).

In this problem, you should write one function named `get_ok_items`, which will be responsible for determining the allowed items in a persons carryon and personal bags.
The function should have three parameters, all of which will be sets of items (strings).
The first set represents the carryon bag contents, the seconds represents the personal bag items, and the third represents the restricted items.
The function should return the set of allowed elements.
For instance, the code:

```
restricted = {'knife', 'water', 'razor'}
carryon = {'laptop', 'water', 'clothes'}
personal = {'mints', 'knife', 'keys'}
result = get_ok_items(carryon, personal, restricted)
print(result)
```

Should print

```
{'mints', 'keys', 'clothes', 'laptop'}
```

Make sure to include only the one function in your file.
The gradescope tests will call the functions to test them.
Name the program `prep36.py`.
Make sure that gradescope gives you the points for passing the test case.

