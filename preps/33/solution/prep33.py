
def longest_string(data):
    string = ''
    for dictionary in data:
        for key, value in dictionary.items():
            if len(value) > len(string):
                string = value
    return string

'''
def main():
    data = [{'a':'horse', 'b':'caterpillar'}, {'a':'camp', 'c':'joker'}]
    result = longest_string(data)
    print(result)
    
    data = [{1:'abc', 5:'onetwothree'}, {2:'abcd'}, {7:'one two three'}]
    result = longest_string(data)
    print(result)
    
main()
'''

