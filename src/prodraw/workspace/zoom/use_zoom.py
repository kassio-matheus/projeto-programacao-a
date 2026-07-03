from tkinter import *

from .zoom import Zoom


# Initializes the Zoom handler and triggers the scaling effect on the canvas
def use_zoom(event: Event, canvas: Canvas):
    Zoom(canvas).scale(event)