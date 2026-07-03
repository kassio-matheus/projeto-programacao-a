from prodraw.shapes import Shape

from prodraw.shapes.colors import SHAPE_COLORS
from .start import Start
from tkinter import *


class Update:
    
    @staticmethod
    def update(obj):
        def update_points(event):
            obj["obj"].canvas.create_line(obj["obj"].start_x, obj["obj"].start_y, event.x,event.y,
                                          fill=obj["obj"].bg, tags="freehand")
            obj["obj"].start_x = event.x
            obj["obj"].start_y = event.y



            
        return update_points

