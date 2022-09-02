---
layout: default
title: CSc 110 - Where's the Money
---

# CSc 110 - Where's the Money

<img src="./res/finances.png" width="280px" />

Budgeting and money management is very important both at the individual level, and for corporations and government.
Having a clear understanding of where your money goes, how much you are saving, and how much you invest is important to financial success.
As a famous author once wrote:

_Annual income twenty pounds, annual expenditure nineteen six, result happiness._
<br/>
_Annual income twenty pounds, annual expenditure twenty pound ought and six, result misery._

_--Charles Dickens_

In this PA, you will be writing a program that helps a user visualize and understand how much money they spend of various categories of expenditures.
Perhaps you will even find this program useful for your personal finances!
You should name your program `wheres_the_money.py`.

## The program interface

This program works by accepting a number of various inputs from a user about how much they make, and how much they spend.
The program will accept 5 input values.
After printing out a welcome message, the program will request all 6 of these inputs.
Below is an example of these input requests, with values provided:

```
-----------------------------
----- WHERE'S THE MONEY -----
-----------------------------
What is your annual salary?
50000
How much is your monthly mortgage or rent?
1000
What do you spend on bills monthly?
400
What are your weekly grocery/food expenses?
200
How much do you spend on travel annually?
2500
```

These 5 values will be used to generate a visualization of the financial situation that looks like so:

```
------------------------------------------------------------------
See the financial breakdown below, based on a salary of $50000
------------------------------------------------------------------
| mortgage/rent | $  12,000.00 |  24.0% | ########################
|         bills | $   4,800.00 |   9.6% | #########
|          food | $  10,400.00 |  20.8% | ####################
|        travel | $   2,500.00 |   5.0% | #####
|           tax | $  10,000.00 |  20.0% | ####################
|         extra | $  10,300.00 |  20.6% | ####################
------------------------------------------------------------------
```

As you can see, the result is essentially a 6-row, 4-column grid that neatly shows that amounts and percentages of income go where.

Each row represents an expense (or other category) where money goes to on a yearly basis.
The first columns provides the name of the category.
The second column shows the amount of money that goes to this category in dollars.
The third columns shows the amount of money as a percentage of yearly income.
The last column is a horizontal bard that correlates with the percentage of income.
The number of `#` characters in this column should be the same as the percentage of income (rounded down).

## Calculating the values
 
The output provided above shows the kind of output this program should produce.
Let's talk a bit about how to compute these values.

The basis for all of the percentages is the first input value - the annual income.
All of the percentages are calculated based on this.
The next two inputs, rent and bills, are monthly expense values.
In order to get the total spend on these categories annually, these numbers must be multiplied by the number of months in a year.
Then, you can use this result to calculate the percentage.
The fourth value is a weekly expense, so this must instead be multiplied by the number of weeks in a year.
The fifth value is already input as an annual value, so you don't need to multiple by number of weeks or months.

The tax percentage is dependent upon the amount of money a person make annually.
The tax brackets are as follows:

* [$0, $15k] annually: 10% tax
* ($15k, $75k] annually: 20% tax
* ($75k, $200k] annually: 25% tax
* over $200k annually: 30% tax

You should use one or more if / elif / else statements in the code to determine which tax percentage to use.
You can store the tax percentage as an integer variable, with one of the following values: `10`, `20`, `25`, or `30`.
You can compute the amount of the salary goes to taxes as a particular percentage with this formula:

```
annual_salary * ( tax_percentage / 100.0)
```

After calculating all of these values programmatically, you should generate the output table.

There is also a tax limit of $75,000.
The tax should be capped at this value, and if the limit is reached, a message indicating this should be printed out after the chart.
The message should say:

```
>>> TAX LIMIT REACHED <<<
```

## Overspending

What happens if the expenditures and taxes are more than the annual salary?
This should be represented by _negative_ values in the extra row.
You should also print a warning after the chart.
Below is an example of a financial situation in which the user spends more than they earn, resulting in a deficit in the _extra_ row.

```
-----------------------------
----- WHERE'S THE MONEY -----
-----------------------------
What is your annual salary?
40000
How much is your monthly mortgage or rent?
2000
What do you spend on bills monthly?
300
What are your weekly grocery/food expenses?
150
How much do you spend on travel annually?
4000

------------------------------------------------------------------------------------------------------
See the financial breakdown below, based on a salary of $40000
------------------------------------------------------------------------------------------------------
| mortgage/rent | $  24,000.00 |  60.0% | ############################################################
|         bills | $   3,600.00 |   9.0% | #########
|          food | $   7,800.00 |  19.5% | ###################
|        travel | $   4,000.00 |  10.0% | ##########
|           tax | $   8,000.00 |  20.0% | ####################
|         extra | $  -7,400.00 | -18.5% |
------------------------------------------------------------------------------------------------------
>>> WARNING: DEFICIT <<<
```

## Validation

You are required to validate the inputs that your program accepts.
You should use if-statements for the validation.
For each numeric input, you should use the `isnumeric` function to check if is a positive integer before converting the value to an integer.

If any do not fit these requirements, you should print out the following message, and then exit:
```
Must enter positive integer for ...
```

However, the `...` should say `salary` or `mortgage or rent` or `bills` or `food` or `travel` depending on which input is not a positive integer.

Multiple test cases will be provided that show what the program should print when these issues occur.
Check The differ tool and/or gradescope.

## Formatting a Number

Notice that the numbers are formatted in a particular way in the output table.
You must match this formatting exactly.
In order to do so, you can use the `format()` function.
This function was mentioned in chapter two of the textbook.
I will provide one example of how you can use this function to match the formatting in the spec.

Say we have a floating point number, like below:

```
number = 134567.123
```

Perhaps this is a result you get for one of the dollar values after doing the necessary computations.
When printing, you'll want to adjust the way it is printed in several ways.

* Add a comma
* Set to stop at two decimal points
* Add necessary spacing before the number, so that the table lines up

You could print out this number and add these three things:

```
string_to_print_out = format(number, '15,.1f')
```

The `15` indicates that the resulting string should be 15 characters wide.
Any characters not needed to display the number will be added as padding to the left side.
The `,` indicates that commas should be added to the number.
The `1` indicates that one decimal place should be shown.
Use this function (with different formatting options) to print out the formatted percentages and dollar values that you calculate.

## Commenting and Style

You should also include a comment at the top of the code file.
The comment should include your name and a short description of what the program does.
Below is a template you may use:

```
### 
### Author: Your Name Here
### Course: CSc 110
### Description: Describe your program with one
###              or more sentences of text.
###
```

You should also make sure to follow the style principles shown in the style guidelines.
Also, you may use the `max` function.

## Examples

See gradescope for more example outputs.

## Due Date

This PA is due on Tuesday, September 13th at 7pm.
Turn in the program via Gradescope.
You should make sure that all of the test cases pass before you turn it in.
You can still submit without all of the cases passing, but that is not preferable.

