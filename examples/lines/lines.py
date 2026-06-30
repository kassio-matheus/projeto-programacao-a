from tkinter import *


def Lines(canva: Canvas, figures: list):

    # Quando o mouse é pressionado
    def start_line(event):
        global ini_x, ini_y
        ini_x = event.x
        ini_y = event.y

    # Quando o mouse é movido com o botão pressionado
    def update_line(event):
        global fim_x, fim_y
        fim_x = event.x
        fim_y = event.y
        draw()
        canva.create_line(ini_x, ini_y, fim_x, fim_y, fill='white', tags='line')

    # Quando o mouse é solto
    def add_line(event):
        figures.append(("line",(ini_x, ini_y, fim_x, fim_y)))

    def draw():
        canva.delete("line")
        for line in figures:
            if line[0] == "line":
                canva.create_line(line[1])

    ini_x = None
    ini_y = None
    fim_x = None
    fim_y = None
    canva.bind('<ButtonPress-1>', start_line)
    canva.bind('<B1-Motion>', update_line)
    canva.bind('<ButtonRelease-1>', add_line)

