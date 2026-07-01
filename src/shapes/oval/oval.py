from tkinter import *

from src.shapes.shape import Shape
from src.shapes.colors import SHAPE_COLORS

class Oval(Shape):
    def __init__ (self, canvas: Canvas, bg: StringVar, figures: list):
        super().__init__(canvas, bg, figures)

    # start oval whe the button is pressed
    def start(self, event):
        self.start_x = event.x
        self.start_y = event.y

    # When the mouse is moved with the button pressed, draw the preview
    def update(self, event):
        self.end_x = event.x
        self.end_y = event.y

        self.draw()

        # Preview
        self.canvas.create_oval(self.start_x, self.start_y, self.end_x, self.end_y,
                           fill=SHAPE_COLORS.get(self.bg.get()), outline=self.bg.get(), tags=("oval", "shape"))

    # add oval in figures list when de mouse is released
    def add(self, event):
        if self.end_x is not None and self.end_y is not None:
            self.figures.append(("oval", self.bg.get(),(self.start_x, self.start_y, self.end_x, self.end_y)))
    
    # draw all ovals
    def draw(self):
        self.canvas.delete("oval")

        for oval in self.figures:
            if oval[0] == 'oval':
                self.canvas.create_oval(oval[2], fill=SHAPE_COLORS.get(oval[1]),
                                outline=oval[1], tags=("oval", "shape"))

    def bind (self):
        super().bind()

def create_oval (canvas: Canvas, bg: StringVar, figures: list):
    Oval(canvas, bg, figures).bind()