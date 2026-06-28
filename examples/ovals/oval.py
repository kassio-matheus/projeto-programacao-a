from tkinter import *


def Oval(canvas: Canvas):
    def start_line(event):
        # event = <ButtonPress event num=1 x=291 y=184>
        nonlocal start_x, start_y
        start_x = event.x
        start_y = event.y

    def update_line(event):
        # event = <Motion event state=Button1 x=120 y=102>
        nonlocal end_x, end_y

        end_x = event.x
        end_y = event.y

        draw()

        # Preview
        canvas.create_oval(start_x, start_y, end_x, end_y,
                           fill="white", outline="black", tags="oval")

    def add_line(event):

        ovals.append((start_x, start_y, end_x, end_y))
        draw()

    def draw():
        canvas.delete("oval")

        for oval in ovals:
            x0, y0, x1, y1 = oval
            canvas.create_oval(x0, y0, x1, y1, fill="white",
                               outline="black", tags="oval")

    ovals = []

    start_x = None
    start_y = None
    end_x = None
    end_y = None

    canvas.bind('<ButtonPress-1>', start_line)
    canvas.bind('<B1-Motion>', update_line)
    canvas.bind('<ButtonRelease-1>', add_line)
