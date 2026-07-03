from tkinter import *

from .button import Button


# Initializes and displays the clear drawings button on the canvas
def use_clear_draw(canvas: Canvas, figures: list):
    Button(canvas, figures).create()