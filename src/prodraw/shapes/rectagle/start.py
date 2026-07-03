from prodraw.shapes import Shape

from .rectangle import Rectangle
from tkinter import *

class Start:
    """Manages the initial creation of a rectangle shape upon mouse click."""

    @staticmethod
    # Returns an event handler to instantiate a rectangle shape at the start position
    def start(canvas: Canvas, bg: StringVar, obj):
        
        # Creates a new Rectangle instance at the event coordinates
        def start_points(event):
            retangulo = Rectangle(canvas, bg, start_x=event.x, start_y=event.y)

            obj['obj'] = retangulo

        return start_points