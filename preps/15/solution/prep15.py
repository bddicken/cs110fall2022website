
def get_height_category(sex, height_in_inches):
    if sex == 'male':
        if height_in_inches > 70:
            return 'above average'
        else:
            return 'below average'
    elif sex == 'female':
        if height_in_inches > 64:
            return 'above average'
        else:
            return 'below average'
    else:
       return 'unknown average'

'''
def main():
    print(get_height_category('female', 67))
    print(get_height_category('female', 63))
    print(get_height_category('male', 72))
    print(get_height_category('male', 67))
    print(get_height_category('abc', 72))

main()
'''

