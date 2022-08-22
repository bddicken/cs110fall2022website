
def calculate_tree_height(height, years):
    i = 0
    while i < years:
        height = height * 1.2
        i += 1
    height = round(height, 4)
    return height

'''
def main():
    print(calculate_tree_height(1, 10))
    print(calculate_tree_height(2, 7))
    print(calculate_tree_height(3, 11))
    print(calculate_tree_height(5, 10))

main()
'''

