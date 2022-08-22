value = int(input('Enter factorial to calculate:\n'))
print()
result = 1
counter = 1
while counter <= value:
    result *= counter 
    counter += 1
print(str(value) + ' factorial = ' + str(result))
