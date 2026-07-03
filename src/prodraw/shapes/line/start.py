from prodraw.shapes import Shape

from .line import Line
from tkinter import *

class Start:
    """Manages the initial creation of a line shape upon mouse click."""

    @staticmethod
    # Returns an event handler to instantiate a line shape at the start position
    def start(canvas: Canvas, bg: StringVar, obj):
        
        # Creates a new Line instance at the event coordinates
        def start_points(event):
            line = Line(canvas, bg, start_x=event.x, start_y=event.y)

            obj['obj'] = line

        return start_points