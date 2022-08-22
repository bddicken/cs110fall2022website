---
layout: default
title: Prep 35
---

# Prep Problem - 35

In this problem, you should write one function named `get_common_movies`.
This function should have one parameter, which you can assume will be a list of sets.
Each set in the list will contain movie titles (strings) representing someones collection of movies that he or she owns.
The function should return a set of all of the movies that all of the collections have in common.
I recommend that you use one (or more) of the functions from the video on set operations.
For instance, the code:

```
collections = [{'terminator', 'matrix', 'avengers'}, {'terminator', 'john wick'}, {'indiana jones', 'terminator'}]
result = get_common_movies(collections)
print(result)
```

Should print

```
{'terminator'}
```

And the code:

```
collections = [{'Sherlock', 'Mighty Ducks', 'T2', 'John Wick'},
               {'John Wick', 'Mighty Ducks', 'T3'},
               {'John Wick', 'Mighty Ducks'},
               {'Alita', 'John Wick', 'T2', 'Mighty Ducks'}]
result = get_common_movies(collections)
print(result)    
```

Should print

```
{'John Wick', 'Mighty Ducks'}
```

Make sure to include only the one function in your file.
The gradescope tests will call the functions to test them.
Name the program `prep35.py`.
Make sure that gradescope gives you the points for passing the test case.

