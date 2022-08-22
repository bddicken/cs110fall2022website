---
layout: default
title: Prep 20
---

# Prep Problem - 20


In this problem, you should write one function named `grade_info`.
This function should accept one parameter, which you can assume will be a list with one or more floating-point numbers, representing student grades.
You can assume the smallest possible grade is 0.0 and the largest is 100.0.
Using a for-loop, the function should determine/calculate the maximum, minimum, and average grades from those in the list.
Use if-statements within the loop to determine min and max.
To determine the average, sum up all of the grades and then divide by the number of grades.

The function should return THREE values: First the maximum, then the minimum, then the average.

* The function call `grade_info([90.0, 70.0, 80.0 ])` should return the values `90.0`, `70.0`, and `80.0`, in that order.
* The function call `grade_info([100.0, 50.0, 75.0, 48.7, 70.2])` should return the values `100.0`, `48.7`, and `68.78`, in that order.
* The function call `grade_info([70.3, 80.5, 71.5, 95.21])` should return the values `95.21`, `70.3`, and `79.3775`, in that order.

Make sure to include only the one function in your file.
The gradescope tests will call the functions to test them.
Name the program `prep20.py`.
Make sure that gradescope gives you the points for passing the test case.

