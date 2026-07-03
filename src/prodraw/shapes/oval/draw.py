from tkinter import *
from .oval import Oval

from prodraw.shapes.colors import SHAPE_COLORS
class Draw:
    
    @staticmethod
    def draw(canvas: Canvas, figures: list):
        canvas.delete("oval")

        for oval in figures:
            if isinstance(oval, Oval):
                canvas.create_oval(oval.start_x, oval.start_y, oval.end_x, oval.end_y,
                                              fill=SHAPE_COLORS.get(oval.bg), outline=oval.bg, tags="oval")
                



