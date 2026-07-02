from tkinter import *

from src.shapes.shape import Shape
from src.shapes.colors import SHAPE_COLORS


class FreeHand(Shape):
    def __init__(self, canvas: Canvas, bg: StringVar, figures: list):
        super().__init__(canvas, bg, figures)

    # start the free hand when button is pressed
    def start(self, event):
        self.start_x = event.x
        self.start_y = event.y

    # draw the freehand when the mouse is moved with the button pressed
    def update(self, event):
        self.canvas.create_line(self.start_x, self.start_y, event.x,
                                event.y, fill=self.bg.get(), tags=("freehand", "shape"))

        self.start_x = event.x
        self.start_y = event.y

    def add():
        pass

    def draw():
        pass

    def bind(self):
        super().bind(isFreeHand=True)


def create_freehand(canvas: Canvas, bg: StringVar, figures: list):
    FreeHand(canvas, bg, figures).bind()
