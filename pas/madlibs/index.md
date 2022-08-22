---
layout: default
title: CSc 110 - Mad Libs
---

# CSc 110 - Mad Libs

In this PA, you will be writing two simple programs that print out text.
Note that this programming assignment (PA) is relatively straightforward.
Not all of the future PAs will be this way.
It is simple because we have not yet covered a wide variety of programming concepts, so there's only so much I can reasonably expect you to be able to program.
The PAs will get more challenging, but also, hopefully, more interesting!

## Part 1: Course Survey

Remember - a part of this PA is filling out the 110 student survey.
Don't forget to fill this out ... it is worth points!

### [Click here to take the 110 PA survey](https://docs.google.com/forms/d/e/1FAIpQLScXXKWvUB2-nHAdpRll4PvXTd4UmpDCrGX_NLkAEarPBjHR3A/viewform?usp=sf_link)

This should not take more than 15 minutes.
Please fill it out thoroughly, accurately, and honestly.

## Part 2: Mad Libs

<img src="./res/madlibs.png" width="200px" />

Mad Libs is a simple game / activity where the host player prompts other participant(s) for words of various types.
For instance, the host might ask the other participants for various words that fall into categories such as nouns, places, names, verbs, etc.
These words are filled in to blanks in a story, and after the host has gotten all of the words filled in, the story is read aloud.
For instance, [here](https://live-madlibs.pantheonsite.io/wp-content/uploads/2016/04/VacationFun_ML_2009_pg15.pdf) is a printable mad lib from [madlibs.com](www.madlibs.com).

In this programming exercise, you'll write two mad lib program, that act as the host of the game.
The program will prompt the participant (the computer user) for various words, and then it will print out a story using these words.

### Move Mad Lib

The first program should be named `move.py`.
The outline of the story is shown below:

```
??? decided to move from her apartment on 5th
to a condo on ???. She called her friend ???
for help. However, they could not fit ??? into
the moving truck, so they had to rent a ??? ???
in order to move it!
```

The locations with `???` indicate that these should be replaced with a word specified by the computer user.
You should prompt the user for 6 inputs, and fill them in to the story.
An example of running the program would look like so:

```
A female name:
Janet
A street name:
Loopdydoo Avenue
A male name:
Richard
An object:
Christmas tree
A vehicle:
Horse-drawn carriage
An adjective:
Off-road
----------
Janet decided to move from her apartment on 5th
to a condo on Loopdydoo Avenue. She called her friend Richard
for help. However, they could not fit Christmas tree into
the moving truck, so they had to rent a Off-road Horse-drawn carriage
in order to move it!
```

### Vacation Mad Lib

The second program should be named `vacation.py`.
The outline of the story is shown below:

```
??? and ??? were best friends.
One day ??? and ??? decided to go on a
vacation to ???. However, they didn't know
what to do with their ??? pet ??? named ???.
??? had been causing problems, due to constant ???.
??? found a sitter for their pet, and ??? went on the trip.
```

Again, locations with `???` indicate that these should be replaced with a word specified by the computer user.
You should prompt the user for 8 inputs.
An example of running the program would look like so:

```
A male name:
Joe
A female name:
Lily
A pet name:
Poncho
A place:
Madagascar
An adjective:
Ridiculous
An animal:
polar bear
A verb ending in ing:
planking
An adverb:
spastically
----------
Joe and Lily were best friends.
One day Joe and Lily decided to go on a
vacation to Madagascar. However, they didn't know
what to do with their Ridiculous pet polar bear named Poncho.
Poncho had been causing problems, due to constant planking.
Joe found a sitter for their pet, and spastically went on the trip.
```

## Comments

Don't forget to include a header/file comment in your code!
Include your name and a description of what the program does.
For instance:

```
### 
### Author: Your Name Here
### Class: CSc 110
### Description: Describe your program with several
###              sentences of text.
###
```

You should also do your best follow the code [Style Guidelines](../style)

## Due Date

This PA is due Tuesday, August 30th by 7pm.
Turn in all programs via Gradescope.
You should try to make sure that all of the test cases pass.
If you don't you will likely lose points.
You can still submit without all of the cases passing, though that is not preferable.

