from tkinter import *


root = Tk()

canvas = Canvas(root, bg='white', width=600, height=600)
canvas.pack()


rectangles = []
# When the mouse is pressed


def start_rectangle(event):
    global ini_x, ini_y
    ini_x = event.x
    ini_y = event.y

# When the mouse is moved with the button pressed


def update_rectangle(event):
    global fim_x, fim_y
    fim_x = event.x
    fim_y = event.y
    draw()
    canvas.create_rectangle(ini_x, ini_y, fim_x, fim_y)

# When the mouse is released


def include_rectangle(event):
    rectangles.append((ini_x, ini_y, fim_x, fim_y))


def draw():
    canvas.delete("all")
    for rectagle in rectangles:
        canvas.create_rectangle(
            rectagle[0], rectagle[1], rectagle[2], rectagle[3])


ini_x = None
ini_y = None
fim_x = None
fim_y = None
canvas.bind('<ButtonPress-1>', start_rectangle)
canvas.bind('<B1-Motion>', update_rectangle)
canvas.bind('<ButtonRelease-1>', include_rectangle)

root.mainloop()
