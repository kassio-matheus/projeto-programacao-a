from tkinter import *

from prodraw.shapes.shape import Shape
from .rounded import create_round_rectangle
#from src.shapes.colors import SHAPE_COLORS
from dataclasses import *

@dataclass
class Rectangle(Shape):
    """Represents a rectangle shape."""

    # Binds start, update, and add events to the shape
    def bind(self, start, update, add):
        super().bind(start, update, add)