
def count_characters(data, char_a, char_b):
    count = 0
    i = 0
    while i < len(data):
        if data[i] == char_a or data[i] == char_b:
            count += 1
        i += 1
    print('\'' + char_a +'\' and \'' + char_b + '\' appeared ' + str(count) + ' times in the string \'' + data + '\'')

'''
def main():
    count_characters('one fish two fish', 'f', 'o')
    count_characters('the deep blue sea', 'e', 'b')

main()
'''
