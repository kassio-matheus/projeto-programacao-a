from tkinter import *
from .rectangle import Rectangle

from src.shapes.colors import SHAPE_COLORS
class Draw:
    
    @staticmethod
    def draw(canvas: Canvas, figures: list):
        canvas.delete("rectangle")

        for retangle in figures:
            if isinstance(retangle, Rectangle):
                canvas.create_rectangle(retangle.start_x, retangle.start_y, retangle.end_x, retangle.end_y,
                                              fill=SHAPE_COLORS.get(retangle.bg), outline=retangle.bg, tags="rectangle")
                



