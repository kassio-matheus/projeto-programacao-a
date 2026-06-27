from tkinter import *


def start_line(event):
    # event = <ButtonPress event num=1 x=291 y=184>
    global start_x, start_y
    start_x = event.x
    start_y = event.y


def update_line(event):
    # event = <Motion event state=Button1 x=120 y=102>
    global end_x, end_y

    end_x = event.x
    end_y = event.y

    draw()

    # Preview
    canvas.create_oval(start_x, start_y, end_x, end_y,
                       outline="white", tags=["ovals"])

# Quando o mouse é solto


def add_line(event):
    ovals.append((start_x, start_y, end_x, end_y))
    draw()


def draw():
    canvas.delete("ovals")

    for oval in ovals:
        x0, y0, x1, y1 = oval
        canvas.create_oval(x0, y0, x1, y1, fill="white", tags=["ovals"])


# ******* MAIN *******#
# Todas os círuculos desenhados são armazenados aqui
ovals = []

root = Tk()

canvas = Canvas(root, bg='black', width=600, height=600)
canvas.pack()

start_x = None
start_y = None
end_x = None
end_y = None

canvas.bind('<ButtonPress-1>', start_line)
canvas.bind('<B1-Motion>', update_line)
canvas.bind('<ButtonRelease-1>', add_line)

root.mainloop()
