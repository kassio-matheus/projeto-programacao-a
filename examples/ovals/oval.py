from tkinter import *
from src.shapes.colors import SHAPE_COLORS


def Oval(canvas: Canvas, bg: StringVar):
    def start_line(event):
        nonlocal start_x, start_y
        start_x = event.x
        start_y = event.y

    def update_line(event):
        nonlocal end_x, end_y

        end_x = event.x
        end_y = event.y

        draw()

        # Preview
        canvas.create_oval(start_x, start_y, end_x, end_y,
                           fill=SHAPE_COLORS.get(bg.get()), outline=bg.get(), tags="oval")

    def add_line(event):
        ovals.append((start_x, start_y, end_x, end_y))
        draw()

    def draw():
        canvas.delete("oval")

        for oval in ovals:
            x0, y0, x1, y1 = oval
            canvas.create_oval(x0, y0, x1, y1, fill=SHAPE_COLORS.get(bg.get()),
                               outline=bg.get(), tags="oval")

    ovals = []

    start_x = None
    start_y = None
    end_x = None
    end_y = None

    canvas.bind('<ButtonPress-1>', start_line)
    canvas.bind('<B1-Motion>', update_line)
    canvas.bind('<ButtonRelease-1>', add_line)