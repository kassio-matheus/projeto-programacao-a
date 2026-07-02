from tkinter import *

from src.shapes.shape import Shape
from src.shapes.colors import SHAPE_COLORS


class Line(Shape):
    def __init__(self, canvas: Canvas, bg: StringVar, figures: list):
        super().__init__(canvas, bg, figures)

    # Quando o mouse é pressionado

    def start(self, event):
        self.start_x = event.x
        self.start_y = event.y

    # Quando o mouse é movido com o botão pressionado
    def update(self, event):
        self.end_x = event.x
        self.end_y = event.y
        self.draw()
        self.canvas.create_line(self.start_x, self.start_y, self.end_x, self.end_y,
                                fill=self.bg.get(), tags=("line", "shape"))

    # Quando o mouse é solto
    def add(self, event):
        self.figures.append(
            ("line", self.bg.get(), (self.start_x, self.start_y, self.end_x, self.end_y)))

    def draw(self):
        self.canvas.delete("line")
        for line in self.figures:
            if line[0] == 'line':
                self.canvas.create_line(
                    line[2], fill=line[1], tags=("line", "shape"))
                
    def bind (self):
        super().bind()

def create_line (canvas: Canvas, bg: StringVar, figures: list):
    Line(canvas, bg, figures).bind()