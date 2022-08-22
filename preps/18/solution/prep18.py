
def multiply(numbers):
    result = 1
    i = 0
    while i < len(numbers):
        result *= numbers[i]
        i += 1
    return result

'''
def main():
    print(multiply([20, 4, 3, 7]))
    print(multiply([1, 2, 3, 4, 5, 6, 7]))
    print(multiply([4, 5, 4, 5, 2, 5, 0, 1]))

main()
'''

