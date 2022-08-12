###
### Author: Put your name here
### Course: CSc 110
### Description: Add a description here
###

from graphics import graphics

def draw_sky_and_land(gui):
    '''
    Draws the sky and the land.
    gui should be a graphics object.
    '''
    gui.rectangle(0, 0, 500, 500, 'black')
    gui.ellipse( 10, 210, 7, 7, 'white')
    gui.ellipse(110, 220, 7, 7, 'white')
    gui.ellipse(210,  50, 7, 7, 'white')
    gui.ellipse(430, 119, 7, 7, 'white')
    gui.ellipse(490, 190, 7, 7, 'white')
    gui.ellipse(370, 220, 7, 7, 'white')
    gui.ellipse(170, 175, 7, 7, 'white')
    gui.ellipse(50, 150, 7, 7, 'white')
    gui.ellipse(78, 80, 7, 7, 'white')
    gui.ellipse(330, 70, 7, 7, 'white')
    gui.rectangle(0, 250, 500, 500, 'dark green')

def draw_hut(gui):
    '''
    This function SHOULD draw a hut.
    gui should be a graphics object.
    '''
    pass

def main():
    gui = graphics(500, 500, 'hut')
    while True:
        gui.clear()
        draw_sky_and_land(gui)
        draw_hut(gui)
        gui.update_frame(60)

main()