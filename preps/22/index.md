---
layout: default
title: Prep 22
---

# Prep Problem - 22

In this problem, you should write one function named `most_common_vehicle`.
This function should accept one parameter, which you can assume will be a name of a file with vehicle ownership info in it.
The file will have exactly three lines, with one number per-line.
The first line represents the number of Toyota vechicles, the second line the number of Ford vehicles, and the third the number of Chevy vehicles.
The program should read in these three lines, and determine which is most common, or if there is a tie.
The function does not need to return anything, just print out a string.

For instance, if the function was passed in the file name `vehicles.txt`, and it's contents were:

```
300
2100
500
```

Then the function should print out.

```
Ford most common
```

The function should always print out one of four possible strings.
Either `Toyota most common`, `Ford most common`, `Chevy most common`, or `There's a tie!`.

Make sure to include only the one function in your file.
The gradescope tests will call the functions to test them.
Name the program `prep22.py`.
Make sure that gradescope gives you the points for passing the test case.

