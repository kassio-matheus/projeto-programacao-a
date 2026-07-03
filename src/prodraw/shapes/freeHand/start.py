from prodraw.shapes import Shape

from .freeHand import FreeHand
from tkinter import *

class Start:
    """Manages the initial creation of a freehand shape upon mouse click."""

    @staticmethod
    # Returns an event handler to instantiate a freehand shape at the start position
    def start(canvas: Canvas, bg: StringVar, obj):

        # Creates a new FreeHand instance at the event coordinates
        def start_points(event):
            freehand = FreeHand(canvas, bg, start_x=event.x, start_y=event.y)

            obj['obj'] = freehand

        return start_points