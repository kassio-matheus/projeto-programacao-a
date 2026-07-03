from tkinter import *

from .button import Button

def use_clear_draw(canvas: Canvas, figures: list):
    Button(canvas, figures).create()