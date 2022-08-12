from graphics import graphics

def get_stock_data():
    f = open('stocks.csv', 'r')
    data = []
    for line in f:
        row = []
        sp = line.split(',')
        row.append(sp[0])
        row.append(sp[1])
        for element in sp[2:]:
            row.append(int(element))
        data.append(row)
    return data

def main():
    stock_data = get_stock_data()
    gui = graphics(600, 300, 'stocks')
    i = 0
    while i < len(stock_data):
        ### What should go here?
        i += 1

main()