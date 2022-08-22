
def calculate_distance(x1, y1, x2, y2):
    distance = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
    return round(distance, 4)

'''
def main():
    print(calculate_distance(0, 0, 5, 5))
    print(calculate_distance(20, 4, 3, 7))
    print(calculate_distance(100, 52, 30, 75))

main()
'''

