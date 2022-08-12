import time
import random

def binary_search(items, item_to_search_for):	
    first = 0
    last = len(items) - 1
    while first <= last:
        check = (first + last) // 2
        if items[check] == item_to_search_for:
            return check
        elif items[check] < item_to_search_for:
            first = check+1
        else:
            last = check-1
    return -1


def sequential_search(items, item_to_search_for):	
    for i in range(len(items)):
        if items[i] == item_to_search_for:
            return i
    return -1

def test():
    x = [1, 3, 7, 10, 20, 35, 50, 70, 80, 90, 101]
    print(binary_search(x, 101) == 10)
    print(binary_search(x, 50) == 6)
    print(binary_search(x, 3) == 1)
    print(sequential_search(x, 101) == 10)
    print(sequential_search(x, 50) == 6)
    print(sequential_search(x, 3) == 1)

test()

def get_sorted_list(length):
    l = []
    for i in range(length):
        l.append(i)
    return l

def time_list_test(length, search_count):
    l = get_sorted_list(length)

    start = time.time()
    for i in range(search_count):
        r = random.randint(0, length*2)
        sequential_search(l, r)
    end = time.time()

    print('Sequential Search')
    print('  Number of elements in list:', length)
    print('  Number of searches timed:', search_count)
    print('  Time:', round(float((end - start)), 4), 'seconds')

    start = time.time()
    for i in range(search_count):
        r = random.randint(0, length*2)
        binary_search(l, r)
    end = time.time()

    print('Binary Search')
    print('  Number of elements in list:', length)
    print('  Number of searches timed:', search_count)
    print('  Time:', round(float((end - start)), 4), 'seconds')

def main():
    list_length = int(input('List length:\n'))
    search_count = int(input('number of searches:\n'))
    time_list_test(list_length, search_count)

main()
