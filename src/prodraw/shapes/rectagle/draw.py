from tkinter import *
from .rectangle import Rectangle

from prodraw.config import SHAPE_COLORS


class Draw:
    """Renders rectangle figures onto the canvas."""

    @staticmethod
    # Clears the canvas and redraws all stored rectangle figures
    def draw(canvas: Canvas, figures: list):
        canvas.delete("rectangle")
        
        for rectangle in figures:
            
            if isinstance(rectangle, Rectangle):
                
                canvas.create_rectangle(rectangle.start_x, rectangle.start_y, rectangle.end_x, rectangle.end_y,
                                        fill=SHAPE_COLORS.get(rectangle.bg), outline=rectangle.bg, tags=("rectangle", "shape"))
