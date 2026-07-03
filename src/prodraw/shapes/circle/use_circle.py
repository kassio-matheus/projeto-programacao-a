from tkinter import *

from .circle import Circle
from .add import Add
from .update import Update
from .start import Start


# Initializes and binds start, update, and add events to the circle drawing process
def use_circle(canvas: Canvas, bg: StringVar, figures: list):
    obj = {"obj": Circle(canvas, bg)}
    start = Start.start(canvas, bg, obj)
    update = Update.update(obj, figures)
    add = Add.add(obj, figures)

    obj["obj"].bind(start, update, add)