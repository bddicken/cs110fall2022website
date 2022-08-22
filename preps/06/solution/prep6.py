temperature = int(input('Temperature in fahrenheit:\n'))

if temperature <= 32:
    print('Ice')
if temperature > 32 and temperature < 212:
    print('Water')
if temperature >= 212:
    print('Steam')

