
def differences(set_a, set_b):
    count = 0
    for e in set_a:
        if e not in set_b:
            count += 1
    for e in set_b:
        if e not in set_a:
            count += 1
    return count

'''
def main():
    print(differences({1, 2, 3}, {2, 3, 4, 5}))
    print(differences({'john', 'mark', 'paul'}, {'john', 'mark'}))

main()
'''
