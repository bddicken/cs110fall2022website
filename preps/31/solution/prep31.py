
def get_elements(data, minimum):
    result = []
    for key, value in data.items():
        if key[0].isupper() or key[-1].isupper() or value >= minimum:
            result.append(value)
    return result

'''
def main():
    data = {'Alpha':10, 'bravo':25, 'charliE':15, 'dELTa':2}
    numbers = get_elements(data, 12)
    print(numbers)
    
    data = {'echo':100, 'foxtroT':1000, 'golf':15, 'hotel':2}
    numbers = get_elements(data, 500)
    print(numbers)
    
main()
'''

