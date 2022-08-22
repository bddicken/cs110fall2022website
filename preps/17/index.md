---
layout: default
title: Prep 17
---

# Prep Problem - 17

In this problem you should write a function named `print_words_starting_with`.
This function should have two parameters.
You can expect that the first will be a string representing a sentence (a sequence of words, separated by spaces).
The second will be a one-letter string.

The function should print out every word from the sentence (the first parameter) that begins with the letter specified (the second parameter).
For example, say that this code was run:

```python
sentence = 'the big brown fox'
print_words_starting_with(sentence, 'b')
```

It should print:

```
big
brown
```

Or if this was run:

```python
words = 'One of those old sterio systems was on sale.'
print_words_starting_with(words, 'o')
```

It should print:

``
of
old
on
```

Make sure to include only the one function in your file.
The gradescope tests will call the functions to test them.
Name the program `prep17.py`.
Make sure that gradescope gives you the points for passing the test cases.

