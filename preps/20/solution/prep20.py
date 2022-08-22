
def grade_info(grades):
    average = 0.0
    maximum = 0.0
    minimum = 100.0
    for element in grades:
        average += element
        if maximum < element:
            maximum = element
        if minimum > element:
            minimum = element
    return maximum, minimum, (average / len(grades))

'''
def main():
    ma, mi, a = grade_info([90.0, 70.0, 80.0])
    print(ma, mi, a)
    ma, mi, a = grade_info([70.3, 80.5, 71.5, 95.21])
    print(ma, mi, a)
    ma, mi, a = grade_info([100.0, 50.0, 75.0, 48.7, 70.2])
    print(ma, mi, a)

main()
'''
