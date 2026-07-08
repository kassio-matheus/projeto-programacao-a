from tkinter import Canvas, StringVar

from .circle_controller import CircleController


def circle_bind(canvas: Canvas, figures: dict, bg: StringVar) -> CircleController:
    controller = CircleController(canvas, figures, get_bg=bg.get)
    controller.bind()
    return controller


def circle_delete(canvas: Canvas, controller: CircleController):
    controller.unbind()
