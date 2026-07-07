from tkinter import *
from dataclasses import *

from prodraw.shapes import Shape

from prodraw.config import SHAPE_COLORS


@dataclass
class Circle(Shape):
    """Represents a circle shape with a specific radius."""

    raio: float = None

    def start(self, event):

        self.start_x = event.x
        self.start_y = event.y

    def update(self, event):

        self.end_x = event.x
        self.end_y = event.y

        self.raio = ((self.start_y - self.end_y)**2 +
                     (self.start_x - self.end_x)**2)**0.5

    def add(self, figures: dict):
        figures['Circle'].append(
            (self.start_x, self.start_y, self.raio, self.bg))

    def empty(self):
        return self.raio > 5
