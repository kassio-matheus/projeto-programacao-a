from tkinter import *

from .freeHand import FreeHand
from .update import Update
from .start import Start

from prodraw.shapes import Shape

def use_freehand(canvas: Canvas, bg: StringVar, figures: list):
    obj = {"obj": FreeHand(canvas, bg)}
    start = Start.start(canvas, bg, obj)
    update = Update.update(obj)


    obj["obj"].bind(start, update)


