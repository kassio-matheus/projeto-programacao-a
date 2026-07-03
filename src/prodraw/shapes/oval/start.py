from prodraw.shapes import Shape

from .oval import Oval
from tkinter import *

class Start:
    """Manages the initial creation of an oval shape upon mouse click."""

    @staticmethod
    # Returns an event handler to instantiate an oval shape at the start position
    def start(canvas: Canvas, bg: StringVar, obj):

        # Creates a new Oval instance at the event coordinates
        def start_points(event):
            oval = Oval(canvas, bg, start_x=event.x, start_y=event.y)

            obj['obj'] = oval

        return start_points