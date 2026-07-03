from prodraw.shapes import Shape

from .circle import Circle
from tkinter import *

class Start:
    """Manages the initial creation of a shape upon mouse click."""

    @staticmethod
    # Returns an event handler to instantiate a shape at the start position
    def start(canvas: Canvas, bg: StringVar, obj):
        
        # Creates a new Circle instance at the event coordinates
        def start_points(event):
            circle = Circle(canvas, bg, start_x=event.x, start_y=event.y)

            obj['obj'] = circle

        return start_points