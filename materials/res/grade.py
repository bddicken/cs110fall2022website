from os import _exit as exit

numeric_grade = input('What is your numeric grade? ')
if numeric_grade.isnumeric() == False:
    print('Enter a different value next time. Exiting.')
    exit(0)

numeric_grade = int(numeric_grade)

# Write your code here
# Use the numeric_grade variable
    