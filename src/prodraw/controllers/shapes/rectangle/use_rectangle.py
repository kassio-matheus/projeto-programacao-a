from tkinter import Canvas, StringVar

from .rectangle_controller import RectangleController


def rectangle_bind(canvas: Canvas, figures: dict, bg: StringVar) -> RectangleController:
    controller = RectangleController(canvas, figures, get_bg=bg.get)
    controller.bind()
    return controller


def rectangle_delete(canvas: Canvas, controller: RectangleController):
    controller.unbind()
