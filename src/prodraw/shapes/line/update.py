from prodraw.shapes import Shape
from .draw import Draw
from prodraw.shapes.colors import SHAPE_COLORS
from .start import Start
from tkinter import *
from .line import Line

class Update:
    
    @staticmethod
    def update(obj, figures: list):
        def update_points(event):
            obj["obj"].end_x = event.x
            obj["obj"].end_y = event.y
            Draw.draw(obj["obj"].canvas,figures)

            obj["obj"].canvas.create_line(obj["obj"].start_x, obj["obj"].start_y, obj["obj"].end_x, obj["obj"].end_y,
                                          fill=obj["obj"].bg, tags="line")
            
        return update_points

