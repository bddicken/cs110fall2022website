
def sum_nums(data):
    result = 0
    for row in data:
        for element in row:
            if element < 10:
                result += element
    return result

'''
def main():
    data = [[5, 7], [15, 25], [2, 7]]
    numbers = sum_nums(data)
    print(numbers)
    
    data = [[2, 12, 2], [12, 5, 100, 9]]
    numbers = sum_nums(data)
    print(numbers)
    
main()
'''

