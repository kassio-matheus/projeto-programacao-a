from tkinter import *

from src.shapes.shape import Shape
from src.shapes.colors import SHAPE_COLORS
from dataclasses import *

@dataclass
class Line(Shape):
    
    def bind (self, start, update, add):
        super().bind(start, update, add)

