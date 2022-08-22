---
layout: default
title: Prep 15
---

# Prep Problem - 15

In this problem, you should write one function named `get_height_category`.
The purpose of the function is to determine of someone is above or below average height.
According to [this website](http://worldpopulationreview.com/states/average-height-by-state/), average female height is 5'4" (64 inches) and average male height is 5'10" (70 inches).
The function should accept two parameters.
The first should be a string, specifying `'female'` or `'male'`, and the second should be the subjects height in inches.
The function should return `'above average'` if the person is taller than 5'4" or 5'10" for female/male respectively.
It should return `'below average'` if the heights are less than or equal to those heights for female/male respectively.
If male or female is not specified, the program can return `'unknown average'`.

* For the two parameters `'female'` and `67`, the function should return `'above average'`:
* For the two parameters `'male'` and `63`, the function should return `'below average'`:
* For the two parameters `'abc123'` and `60`, the function should return `'unknown average'`:

You may call the functions in your code in order to test.
However, you should remove all calls to the function before you submit to gradescope.
The gradescope tests will call the functions to test them.

Name the program `prep15.py`.
Make sure that gradescope gives you the points for passing the test case.

