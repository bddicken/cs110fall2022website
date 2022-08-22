
def count_calories(food):
    count = 0
    for k, v in food.items():
        count += v
    return count

'''
def main():
    print(count_calories({'chocolate':200, 'milk':120, 'steak':250}))
    print(count_calories({'carrot':5, 'apple':50}))

main()
'''

