drink_size = input('Drink Size:\n') 
drink_type = input('Drink type:\n')

print()

if drink_type == 'water':
    print('0 calories')
elif drink_size == 'large' and drink_type == 'regular':
    print('300 calories')
elif drink_size == 'small' and drink_type == 'regular':
    print('150 calories')
elif drink_size == 'large' and drink_type == 'diet':
    print('100 calories')
elif drink_size == 'small' and drink_type == 'diet':
    print('50 calories')

