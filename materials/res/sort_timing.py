import random
import time

def insertion_sort(items):
    for compare_index in range(1, len(items)):
        ci = compare_index
        for j in range(ci-1, -1, -1):
            if ci < 0 or items[ci] >= items[j]:
                break
            else:
                items[ci], items[j] = items[j], items[ci]
                ci -= 1

def bubble_sort(items):
    end = len(items)
    for i in range(len(items)-1):
        for j in range(0, end-1):
            if items[j] > items[j+1]:
                items[j], items[j+1] = items[j+1], items[j]
        end -= 1

def selection_sort(items):
    begin = 0
    for i in range(len(items)-1):
        small_i = begin
        for j in range(begin, len(items)):
            if items[small_i] > items[j]:
                small_i = j
        items[begin], items[small_i] = items[small_i], items[begin]
        begin += 1

def get_random_list(length):
    l = []
    for i in range(length):
        r = random.randint(0, length)
        l.append(r)
    return l

def time_list_test(length):

    l1 = get_random_list(length)
    l2 = l1.copy()
    l3 = l1.copy()

    start = time.time()
    selection_sort(l1)
    end = time.time()

    print('Selection Sort')
    print('  Number of elements in list:', length)
    print('  Time:', round(float((end - start)), 3), 'seconds')

    start = time.time()
    bubble_sort(l2)
    end = time.time()

    print('Bubble Sort')
    print('  Number of elements in list:', length)
    print('  Time:', round(float((end - start)), 3), 'seconds')

    start = time.time()
    insertion_sort(l3)
    end = time.time()

    print('Insertion Sort')
    print('  Number of elements in list:', length)
    print('  Time:', round(float((end - start)), 3), 'seconds')

def main():
    list_length = int(input('List length:\n'))
    time_list_test(list_length)

main()
