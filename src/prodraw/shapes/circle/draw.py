from tkinter import *
from .circle import Circle

from prodraw.shapes.colors import SHAPE_COLORS

class Draw:
    """Renders shape figures onto the canvas."""
    
    @staticmethod
    # Clears the canvas and redraws all stored circle figures
    def draw(canvas: Canvas, figures: list):
        canvas.delete("circle")

        for circle in figures:
            if isinstance(circle, Circle):
                canvas.create_oval(circle.start_x-circle.raio, circle.start_y-circle.raio, circle.start_x+circle.raio, circle.start_y+circle.raio,
                                              fill=SHAPE_COLORS.get(circle.bg), outline=circle.bg, tags="circle")