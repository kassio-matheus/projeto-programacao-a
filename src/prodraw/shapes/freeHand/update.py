from prodraw.shapes import Shape

from prodraw.shapes.colors import SHAPE_COLORS
from .start import Start
from tkinter import *


class Update:
    """Handles drawing continuous lines dynamically during mouse drag."""
    
    @staticmethod
    # Returns an event handler that draws a line segment and updates the coordinates
    def update(obj):
        
        # Draws a line from the previous position to the current position and updates the start point
        def update_points(event):
            obj["obj"].canvas.create_line(obj["obj"].start_x, obj["obj"].start_y, event.x,event.y,
                                          fill=obj["obj"].bg, tags="freehand")
            obj["obj"].start_x = event.x
            obj["obj"].start_y = event.y

        return update_points