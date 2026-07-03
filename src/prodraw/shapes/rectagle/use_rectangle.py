from tkinter import *

from .rectangle import Rectangle
from .add import Add
from .update import Update
from .start import Start

from prodraw.shapes.shape import Shape

# Initializes and binds start, update, and add events to the rectangle drawing process
def use_rectangle(canvas: Canvas, bg: StringVar, figures: list):
    obj = {"obj": Rectangle(canvas, bg)}
    start = Start.start(canvas, bg, obj)
    update = Update.update(obj, figures)
    add = Add.add(obj, figures)

    obj["obj"].bind(start, update, add)