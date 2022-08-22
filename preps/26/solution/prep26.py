def longest_word(words):
    words_split = words.split(' ')
    longest = ''
    for word in words_split:
        if len(word) > len(longest):
            longest = word
    return longest

