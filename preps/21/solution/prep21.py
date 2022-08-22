
def two_words(words):
    first = 'zzzzzzzzzzzzzz'
    last = 'aaaaaaaaaaaaaa'
    for word in words:
        if word < first:
            first = word
        if word > last:
            last = word
    return first + ' ' + last

'''
def main():
    two_results = two_words(['tree', 'forest', 'antelope', 'zebra'])
    print(two_results)
    two_results = two_words(['zoo', 'champion', 'fetch', 'those', 'lemurs'])
    print(two_results)

main()
'''
