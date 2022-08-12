import random
import time
from graphics import graphics

def get_selection_sort_steps(l):
    steps = []
    begin = 0
    for i in range(0, len(l)):
        small_i = begin
        for j in range(begin, len(l)):
            if l[small_i] > l[j]:
                small_i = j
        l[begin], l[small_i] = l[small_i], l[begin]
        s = l.copy()
        steps.append(s)
        begin += 1
    return steps

def get_bubble_sort_steps(l):
    steps = []
    end = len(l)
    for i in range(0, len(l)):
        for j in range(0, end-1):
            if l[j] > l[j+1]:
                l[j], l[j+1] = l[j+1], l[j]
                s = l.copy()
                steps.append(s)
        end -= 1
    return steps

def get_insertion_sort_steps_old(l):
    steps = []
    for compare_index in range(1, len(l)):
        ci = compare_index
        for j in range(ci-1, -1, -1):
            if ci < 0 or l[ci] >= l[j]:
                break
            else:
                l[ci], l[j] = l[j], l[ci]
                s = l.copy()
                steps.append(s)
                ci -= 1
    return steps

def get_insertion_sort_steps(l):
    steps = []
    for compare_index in range(1, len(l)):
        e = l[compare_index]
        ci = compare_index
        for j in range(compare_index-1, -1, -1):
            if e >= l[j]:
                l[ci] = e
                s = l.copy()
                steps.append(s)
                break
            else:
                l[j+1] = l[j]
                s = l.copy()
                steps.append(s)
                ci -= 1
    return steps

def get_random_list(length):
    l = []
    for i in range(length):
        r = random.randint(0, length)
        l.append(r)
    return l

def get_different_indexes(l1 ,l2):
    indexes = []
    for i in range(len(l1)):
        if l1[i] != l2[i]:
            indexes.append(i)
    return indexes

def get_sort_steps(e):
    sort_type = input('Type of sort? ')
    if sort_type == 'selection':
        return get_selection_sort_steps(e)
    elif sort_type == 'bubble':
        return get_bubble_sort_steps(e)
    else:
        return get_insertion_sort_steps(e)

def main():

    length = input('Number of elements? ')
    e = get_random_list(int(length))

    steps = get_sort_steps(e)

    height = 400
    width = 700
    bar_width = (width // len(e)) - 1
    maximum = max(e)

    gui = graphics(width, height, 'vis')

    for i in range(len(steps)):
        step = steps[i]
        gui.clear()
        x = 0
        for j in range(len(step)):
            bar_height = step[j] * (height / maximum)
            color = 'blue'
            if i < len(steps)-1:
                indexes = get_different_indexes(steps[i], steps[i+1])
                if j in indexes:
                    color = 'red'
            gui.rectangle(x, height - bar_height, bar_width, bar_height, color)
            gui.text(x, height-15, str(step[j]), 'light blue', 12)
            x += bar_width + 1
        gui.update_frame(60)

main()