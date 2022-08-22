
def print_words_starting_with(sentence, character):
    i = 0
    while i < len(sentence):
        if sentence[i] == character and sentence[i-1] == ' ':
            while i < len(sentence) and sentence[i] != ' ':
                print(sentence[i], end='')
                i += 1
            print()
        i += 1

'''
def main():

    words = 'One of those old sterio systems was on sale.'
    print_words_starting_with(words, 'o')

    sentence = 'the big brown fox'
    print_words_starting_with(sentence, 'b')

main()
'''

