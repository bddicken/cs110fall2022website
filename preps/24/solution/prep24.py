
def count_vowels(data, begin, end):
    substring = data[begin:end+1]
    count = 0
    for c in substring:
        if c in 'aeiou':
            count += 1
    return count

'''
def main():
    print(count_vowels('one fish two fish', 2, 10))
    print(count_vowels('kiwis and oranges are good', 10, 25))
    print(count_vowels('aeiouaeiouaeiou', 5, 12))

main()
'''

