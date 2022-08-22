
def get_supply_count():
    f = open('supplies.txt', 'r')
    total = 0
    for line in f:
        total += int(line.split(' ')[1])
    out = open('total.txt', 'w')
    out.write(str(total))
    out.close()

def main():
    get_supply_count()

main()

