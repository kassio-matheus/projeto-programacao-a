from tkinter import *

from .zoom import Zoom


def use_zoom(event: Event, canvas: Canvas):
    Zoom(canvas).scale(event)
