from tkinter import *

def FreeHand(canva: Canvas):

    init_x = None
    init_y = None

    def startFigure(event):
        global init_x, init_y

        init_x = event.x
        init_y = event.y

    def updateFigure(event):
        global init_x, init_y
        canva.create_line(init_x, init_y, event.x, event.y, fill='white', tags='freehand')

        init_x = event.x
        init_y = event.y
        



    

    canva.bind('<ButtonPress-1>', startFigure)
    canva.bind('<B1-Motion>', updateFigure)
