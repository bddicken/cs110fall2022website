---
layout: default
title: Prep 27
---

# Prep Problem - 27

As of Spring 2020, in otder to get into the CS major, you must have a 3.0 GPA or better in cs120, cs210, and cs245.
In this problem, you should write one function named `get_gpa`, which will calculate this GPA.
This function should have one parameter, which will be a dictionary of grades in computer science courses.
You can assume that the dictionary will always have the keys `'cs120'`, `'cs210'`, and `'cs245'`, but it also might contain some names of other courses too.
The values associated with each key will be a float representeing the GPA-style grade for that class.
For instance, the parameter dictionary might look like: `{'cs120':4.0 'cs245':3.0, 'cs210':2.0}`.
Some examples:

* `get_gpa({'cs110': 4.0, 'cs245':3.0, 'cs335':4.0, 'cs120':3.0, 'cs210':3.0})` should return 3.0.
* `get_gpa({'cs110': 4.0, 'cs120':3.0, 'cs245':2.0, 'cs210':1.0})` should return 2.0.
* `get_gpa({'cs245':4.0, 'cs120':3.0, 'cs210':2.0})` should return 3.0.

Make sure to include only the one function in your file.
The gradescope tests will call the functions to test them.
Name the program `prep27.py`.
Make sure that gradescope gives you the points for passing the test case.

