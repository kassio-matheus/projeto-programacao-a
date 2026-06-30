from tkinter import *


def Circle(canvas: Canvas, bg: str):
    def start_line(event):
        nonlocal start_x, start_y
        start_x = event.x
        start_y = event.y

    def update_line(event):
        nonlocal end_x, end_y, raio
        end_x = event.x
        end_y = event.y
        raio = ((start_x - end_x)**2 + (start_y - end_y)**2) ** 0.5
        draw()
        canvas.create_oval(start_x-raio, start_y-raio, start_x +
                           raio, start_y+raio, outline="black", fill="white", tags="circle")

    def add_line(event):
        circles.append((start_x, start_y, raio))

    def draw():
        canvas.delete("circle")
        for circle in circles:
            x, y, r = circle
            canvas.create_oval(x-r, y-r, x+r, y+r, outline="black", fill="white", tags="circle")

    start_x = None
    start_y = None
    end_x = None
    end_y = None
    canvas.bind('<ButtonPress-1>', start_line)
    canvas.bind('<B1-Motion>', update_line)
    canvas.bind('<ButtonRelease-1>', add_line)

    circles = []
    raio = None