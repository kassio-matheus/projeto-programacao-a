from tkinter import *

from src.shapes.shape import Shape
from .rounded import create_round_rectangle

from src.shapes.colors import SHAPE_COLORS

# function for draw rectangles

class Rectangle(Shape):
    def __init__ (self, canvas: Canvas, bg: StringVar, figures: list):
        super().__init__(canvas, bg, figures)
        pass

    # When the mouse is pressed

    def start(self, event):
        self.start_x = event.x
        self.start_y = event.y

    # When the mouse is moved with the button pressed

    def update(self, event):
        self.end_x = event.x
        self.end_y = event.y
        self.draw()
        self.canvas.create_rectangle(
            self.start_x, self.start_y, self.end_x, self.end_y, fill=SHAPE_COLORS.get(self.bg.get()), outline=self.bg.get(), tags=("rectangle", "shape"))
        # create_round_rectangle(canvas,
        #                        start_x, start_y, end_x, end_y, radius=40, fill="white", outline="black", tags="rectangle")

    # When the mouse is released

    def add(self, event):
        if self.end_x is not None and self.end_y is not None:
            if self.start_x != self.end_x or self.start_y != self.end_y:
                self.figures.append(("rectangle", self.bg.get(), (self.start_x, self.start_y, self.end_x, self.end_y)))

    # draw all figures
    def draw(self):
        self.canvas.delete("rectangle")
        for rectagle in self.figures:
            if rectagle[0] == "rectangle":
                self.canvas.create_rectangle(
                    *rectagle[2], fill=SHAPE_COLORS.get(rectagle[1]), outline=rectagle[1], tags=("rectangle", "shape"))

        # for rectagle in rectangles:
        #     create_round_rectangle(
        #         canvas, rectagle[0], rectagle[1], rectagle[2], rectagle[3], radius=40, fill="white", outline="black", tags="rectangle")

    def bind (self):
        super().bind()

def create_rectangle (canvas: Canvas, bg: StringVar, figures: list):
    Rectangle(canvas, bg, figures).bind()