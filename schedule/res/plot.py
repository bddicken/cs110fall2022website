from graphics import graphics

def get_stock_data(file_name):
    '''
    Implement this.
    It should open up a CSV file and load the information
    Into a 2D list.
    The function should return the 2D list after loaded.
    '''

def main():
    file_name = input('Enter name of file: ')
    stock_data = get_stock_data(file_name)
    gui = graphics(700, 400, 'stocks')
    i = 0
    while i < len(stock_data):
        label = stock_data[i][0]
        color = stock_data[i][1]
        gui.text(5, 5+30*i, label, color, 25)
        # Finish the code
    gui.primary.mainloop()

main()



