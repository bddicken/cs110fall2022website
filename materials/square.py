from graphics import graphics

def main():
    gui = graphics(500, 300, 'Example')
    while True:
        gui.clear()
        gui.rectangle(gui.mouse_x - 50, gui.mouse_y - 50, \
                      100, 100, 'blue')
        gui.update_frame(60)

main()