from tkinter import *

from src.shapes.shape import Shape

from src.shapes.colors import SHAPE_COLORS


class Circle(Shape):
    def __init__(self, canvas: Canvas, bg: StringVar, figures: list):
        super().__init__(canvas, bg, figures)
        pass

    # start the circle when button is pressed
    def start(self, event):
        self.start_x = event.x
        self.start_y = event.y

    # draw the circle when the mouse is moved with the button pressed
    def update(self, event):
        global raio

        self.end_x = event.x
        self.end_y = event.y
        raio = ((self.start_x - self.end_x)**2 + (self.start_y - self.end_y)**2) ** 0.5
        self.draw()
        self.canvas.create_oval(self.start_x-raio, self.start_y-raio, self.start_x +
                           raio, self.start_y+raio, outline=self.bg.get(), fill=SHAPE_COLORS.get(self.bg.get()), tags=("circle", "shape"))

    # add the circle in the figures

    def add(self, event):
        if isinstance(raio, float):
            self.figures.append(("circle", self.bg.get(), (self.start_x, self.start_y, raio)))

    # draw all circles

    def draw(self):
        self.canvas.delete("circle")
        for circle in self.figures:
            if circle[0] == 'circle':
                x, y, r = circle[2]
                self.canvas.create_oval(x-r, y-r, x+r, y+r,
                                   outline=circle[1], fill=SHAPE_COLORS.get(circle[1]), tags=("circle", "shape"))
                
    def bind (self):
        super().bind()

    raio = None

def create_circle (canvas: Canvas, bg: StringVar, figures: list):
    Circle(canvas, bg, figures).bind()