from dataclasses import *
from tkinter import *
from prodraw.models.shapes import Circle

from prodraw.config import SHAPE_COLORS


@dataclass
class CircleView:
    canvas: Canvas

    def draw(self, circle: Circle):
        self.canvas.delete("circle_creating")
        self.canvas.create_oval(circle.start_x-circle.raio, circle.start_y-circle.raio, circle.start_x+circle.raio, circle.start_y+circle.raio,
                                fill=SHAPE_COLORS.get(circle.bg.get()), outline=circle.bg.get(), tags=("circle_creating", "shape"))

    def draw_all(self, figures: dict):
        self.canvas.delete("circle_creating")
        for circle in figures['Circle']:
            x, y, r, bg = circle
            self.canvas.create_oval(
                x-r, y-r, x+r, y+r, fill=SHAPE_COLORS.get(bg.get()), outline=bg.get(), tags=("circle", "shape"))

    def delete(self):
        self.canvas.delete('circle')
