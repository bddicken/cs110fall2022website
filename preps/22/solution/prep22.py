
def most_common_vehicle(file_name):
    f = open(file_name)
    toyota = int(f.readline())
    ford   = int(f.readline())
    chevy  = int(f.readline())
    if toyota > ford and toyota > chevy:
        print('Toyota most common')
    elif ford > toyota and ford > chevy:
        print('Ford most common')
    elif chevy > toyota and chevy > ford:
        print('Chevy most common')
    else:
        print('There\'s a tie!')

'''
def main():
    most_common_sickness('t1.txt')
    most_common_sickness('t2.txt')

main()
'''

