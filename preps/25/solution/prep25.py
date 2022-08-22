
def every_other(tokens):
    token_list = tokens.split(' ')
    result = token_list[0]
    for i in range(2, len(token_list), 2):
         result += ' '+ token_list[i]
    return result

'''
def main():
    print(every_other('one fish two fish red fish blue fish'))
    print(every_other('these are words'))

main()
'''

