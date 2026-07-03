from tkinter import *

from prodraw.shapes.shape import Shape
from prodraw.shapes.colors import SHAPE_COLORS
from dataclasses import *

@dataclass
class Line(Shape):
    """Represents a straight line shape."""
    
    # Binds start, update, and add events to the shape
    def bind (self, start, update, add):
        super().bind(start, update, add)