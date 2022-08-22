
def average_numbers(count):
    sum_of_nums = 0
    i = 0
    while i < count:
        sum_of_nums += int(input('Number:\n'))
        i += 1
    average = sum_of_nums / count
    print('Average =', round(average, 2))

'''
def main():
    average_numbers(2)
    print()
    average_numbers(5)

main()
'''

