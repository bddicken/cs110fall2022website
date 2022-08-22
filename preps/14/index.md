---
layout: default
title: Prep 14
---

# Prep Problem - 14

In this problem, you should write one function named `calculate_tree_height`.
The purpose of the function is to calculate how tall a tree will be in some number of years.
This function should accept two parameter variables, and return one floating-point number.
The first parameter should be the current height of the tree, in feet.
The second should be the number of years into the future to calculate the heightof the tree at.
Each year, the height of the tree should grow to 1.2 times the height it was the previous year.
Thus, if a tree is 10 feet tall, in three years it should be: `10 * 1.2 * 1.2 * 1.2 = 17.2799`.
The function should calculate the height based on the current height and number of years, and return the calculated height as a float, rounded to four decimals places.

* For the two parameters `5` and `10`, the function should return `30.9587`:
* For the two parameters `2` and `7`, the function should return `7.1664`:
* For the two parameters `1` and `10`, the function should return `6.1917`:

You may call the functions in your code in order to test.
However, you should remove all calls to the function before you submit to gradescope.
The gradescope tests will call the functions to test them.

Name the program `prep14.py`.
Make sure that gradescope gives you the points for passing the test case.

