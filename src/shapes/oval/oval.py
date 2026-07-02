from tkinter import *

from src.shapes.shape import Shape
from src.shapes.colors import SHAPE_COLORS

class Oval(Shape):
    
    def bind (self, start, update, add):
        super().bind(start, update, add)

