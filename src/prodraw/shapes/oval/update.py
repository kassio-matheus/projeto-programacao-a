from prodraw.shapes import Shape
from .draw import Draw
from prodraw.shapes.colors import SHAPE_COLORS
from .start import Start
from tkinter import *


class Update:
    
    @staticmethod
    def update(obj, figures: list):
        def update_points(event):
            obj["obj"].end_x = event.x
            obj["obj"].end_y = event.y
            Draw.draw(obj["obj"].canvas,figures)

            obj["obj"].canvas.create_oval(obj["obj"].start_x, obj["obj"].start_y, obj["obj"].end_x, obj["obj"].end_y,
                                          fill=SHAPE_COLORS.get(obj["obj"].bg), outline = obj['obj'].bg, tags="oval")
            
        return update_points

