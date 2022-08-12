from os import _exit as exit

first = input('Enter first name: ')
if not first.isalpha() or len(first) > 30 or not first[0].isupper():
    print('Invalid first name.')
    exit(0)
    
middle = input('Enter middle initial: ')
if not middle.isalpha() or len(middle) > 1 or not middle[0].isupper():
    print('Invalid middle initial.')
    exit(0)

last = input('Enter last name: ')
if not last.isalpha() or len(last) > 30 or not last[0].isupper():
    print('Invalid last name.')
    exit(0)