from tkinter import *

from .line import Line
from .add import Add
from .update import Update
from .start import Start


# Initializes and binds start, update, and add events to the line drawing process
def use_line(canvas: Canvas, bg: StringVar, figures: list):
    obj = {"obj": Line(canvas, bg)}
    start = Start.start(canvas, bg, obj)
    update = Update.update(obj, figures)
    add = Add.add(obj, figures)

    obj["obj"].bind(start, update, add)