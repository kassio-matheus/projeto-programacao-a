from tkinter import *

from src.shapes.shape import Shape
from .rounded import create_round_rectangle
#from src.shapes.colors import SHAPE_COLORS
from dataclasses import *
# function for draw rectangles

@dataclass
class Rectangle(Shape):

    def bind(self, start, update, add):
        super().bind(start, update, add)

