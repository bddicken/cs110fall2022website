food = input('Enter food:\n')
price = int(input('Enter price:\n'))

if price > 20:
    print('That', food, 'is expensive.')
if price <= 20:
    print('That', food, 'is affordable.')
