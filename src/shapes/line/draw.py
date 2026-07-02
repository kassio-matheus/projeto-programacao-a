from tkinter import *
from .line import Line

from src.shapes.colors import SHAPE_COLORS
class Draw:
    
    @staticmethod
    def draw(canvas: Canvas, figures: list):
        canvas.delete("line")

        for line in figures:
            if isinstance(line, Line):
                canvas.create_line(line.start_x, line.start_y, line.end_x, line.end_y,
                                              fill=line.bg, tags="line")
                



