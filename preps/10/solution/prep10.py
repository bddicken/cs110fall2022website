import os

string = input('Enter string:\n')

## May not use the count function

paren_count = 0
i = 0
while i < len(string):
    if string[i] == '(':
        paren_count += 1
    if string[i] == ')':
        paren_count -= 1
    if paren_count < 0:
        print('Parentheses unbalanced')
        os._exit(0)
    i += 1

if paren_count != 0:
    print('Parentheses unbalanced')
else:
    print('Parentheses balanced')
