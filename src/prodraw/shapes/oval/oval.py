from tkinter import *

from prodraw.shapes.shape import Shape
from prodraw.shapes.colors import SHAPE_COLORS
from dataclasses import *

@dataclass
class Oval(Shape):
    
    def bind (self, start, update, add):
        super().bind(start, update, add)

