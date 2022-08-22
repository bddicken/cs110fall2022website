---
layout: default
title: Prep 10
---

# Prep Problem - 10

When you write mathematical expressions, as well as lines of code in python, it is important to keep your parentheses balanced.
For every open parenthesis, `(`, there must be a matching closed parenthesis, `)`.
For instance, these math expressions have unbalanced parentheses:

* `5 * (7 * (2 + 4)`
* `((7 / 2) + 5) - 3)`
* `) 1 + ) 2 + 1((`

However, these have balanced parentheses:

* `(1 + 1) + (5 + 7 * 2)`
* `5 + (4 * (3 + (5 + 5)))`

You should write a program that takes a string as input, and determines if the parentheses are balanced or not.
You can use a while-loop to determine this.
While looping through the characters, keep track of how many closed and open parentheses you see.
If either of the below conditions is met, that indicates unbalanced parentheses:

* If on any iteration of the while-loop there are more closed parentheses than open parentheses.
* If after the loop, the number of open parentheses is not the same as the number of closed parentheses.

Some examples:

```
Enter string:
5 + (4 * (3 + (5 + 5)))
Parentheses balanced
```

```
Enter string:
(()))((((())))
Parentheses unbalanced
```

Name the program `prep10.py`.
Make sure that gradescope gives you the points for passing the test case.

