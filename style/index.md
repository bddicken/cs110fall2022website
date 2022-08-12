---
layout: default
title: Code Requirements
---

# CSc 110: Code Style Requirements

Note: Some of these requirements may apply to concepts not yet covered, depending on what point in the semester you are reading this at.

### File Comments

You are required to have a file comment (comment at the top of your code) which includes at least your name and a description of your code.
The description should _not_ be a tiny one-liner.
Provide a few sentences describing what your program accomplishes.
You can also include other pieces of information in this comment, such as what CS course the program was a PA for.
Below is an outline that you may follow:

```
###
### Author: Your name here
### Course: CSc 110
### Description: Put a description of your program here. you can describe what
###              kinds of inputs your program accepts, what it is supposed to
###              accomplish, and other features.
###
```

### Code Comments

You should place comments above any block of code that completes a non-trivial tasks.
These should begin with a single `#`.
For example, you are not required to place a comment immediately above this code:

```
age = int(input('Enter your age: '))
if age > 18:
    print('You may apply to join the army')
```

After you gain enough programming experience, it should be pretty clear from the variable names and structure of the code what this is doing.
Though, on a block of code like this:

```
grid = fetch_grid_values()
for i in range(len(grid)):
    for j in range(len(i)):
        if j > MIDDLE:
           grid[i][j] += 1
```

You should place one or more comments above it, describing what it is accomplishing.

### Variable Naming

You should name all of your variables according the typical python style guidelines.
Variable names should contain primarily only lower-case letters, number, and underscores.
The words for multi-word variable names should be separated with underscores.
The below code displays some examples of good and not-good variable naming.

```
# Good variable naming
age = 30
yearly_salary = 50000
vehicle_type = 'Nissan Altima'

# Variable naming that is not good (for this course)
aGE = 30
yearlySalary = 50000
vehicle_TYPE = 'Nissan Altima'
a = 'something'
aL = 20
aa84ga7 = 'something'
```

### General/Misc Code Structure

You should do your best to submit code that is well-structured and easy-to-read.
Some guidance for this:

* Chunk your lines of code into groups.
  If there are several lines of code in-a-row that all help achieve the same small task, you should group them together with no spaces in-between.
  Then, you can put an empty space before the next block of code.
* Use 4 spaces for indentation. Note that 4 spaces is different than 1 tab.
* You should keep all of your lines of code less than 100 characters wide.
  If you have a line of code that is wider, consider re-writing it to be in two statements, or use the `\` character to continue a statement onto the next line.
* You may only use material for an prep, PA, or exam if it has been covered in class or the book up to the point of the deadline.
  For example, you may not use a list for PA number 2, since it would not have been covered at that point in time.

## Once functions are covered...

### Function Comments

You should include a function comment for each function that you write, other than main.
The comment should describe the task that the function performs.
It should also describe each of the parameters.
Below is an example:

```
def max(value_1, value_2, value_3):
    '''
    This function returns the maximum value of the three parameter varuables.
    value_1: Can be any integer.
    value_2: Can be any integer.
    value_3: Can be any integer.
    '''
    if value_1 > value_2 and value_1 > value_3:
        return value_1
    elif value_2 > value_1 and value_2 > value_3:
        return value_2
    return value_3

```

### Function Naming

For the purposes of this course, the function naming rules are the same as the variable naming rules.

### Function Structure

When using functions in your program, have each function accomplish a specific task.
Don't try to cram too much functionality into one function.
If you find yourself writing the majority of your code for a PA in a single function, refactor.
If you find yourself writing one function that is more than 30 lines of code, refactor.
The function-level comments (the multi-line string comment) does not count against the 30 line limit.
You should not write a function that has more than 5 parameters or returns more than 5 separate return values.
All other code, spacing, and comments do count.

## Other

You should not be using the `break` statement in your code, unless otherwise specified.
If you want to use it to get out of a loop, think of another way!

