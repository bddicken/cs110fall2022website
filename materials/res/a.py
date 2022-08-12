def binary_search(l, x):
    first = 0
    last = len(l)
    while first < last:
        check = (first + last - 1) // 2
        if l[check] == x:
            return True
        elif l[check] < x:
            first = check+1
        else:
            last = check-1
    return False

