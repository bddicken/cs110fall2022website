---
layout: default
title: Prep 23
---

# Prep Problem - 23

In this problem, you should write one function named `get_supply_count`.
This function should have no parameters, and does not need to return anything.
The task of the function is:

* (A) Open a file in read mode named `supplies.txt`
* (B) Loop through the lines, keeping track of the total number of supplies
      You can assume each line has one string representing the name of the supply, followed by thr number of that supply.
      For instance `Television 10` or `tomato 38` or `skittles 147`.
* (C) Open a file in write mode named `total.txt`
* (D) Write the total supply count to the file


For instance, say the function was called and this is what was in `supplies.txt`:

```
tv  0
mouse 100
monitor 0
speakers 12
iphone 5
```

When the function finishes, `total.txt` should look like so:

```
117
```

Make sure to include only the one function in your file.
The gradescope tests will call the functions to test them.
Name the program `prep23.py`.
Make sure that gradescope gives you the points for passing the test case.

