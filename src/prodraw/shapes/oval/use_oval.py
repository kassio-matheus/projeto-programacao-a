from tkinter import *

from .oval import Oval
from .add import Add
from .update import Update
from .start import Start



def use_oval(canvas: Canvas, bg: StringVar, figures: list):
    obj = {"obj": Oval(canvas, bg)}
    start = Start.start(canvas, bg, obj)
    update = Update.update(obj, figures)
    add = Add.add(obj, figures)

    obj["obj"].bind(start, update, add)


