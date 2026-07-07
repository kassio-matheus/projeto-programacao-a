from tkinter import *

from prodraw.views import CircleView
from .circle_controller import CircleController


def circle_bind(canvas: Canvas, figures: dict, bg: StringVar):
    view = CircleView(canvas)

    canvas.bind('<ButtonPress-1>', CircleController.start(bg))
    canvas.bind('<B1-Motion>', CircleController.update(view))
    canvas.bind('<ButtonRelease-1>', CircleController.add(view, figures))


def circle_delete(canvas):
    view = CircleView(canvas)
    view.delete()
