from tkinter import Canvas, StringVar

from .line_controller import LineController


def line_bind(canvas: Canvas, figures: dict, bg: StringVar) -> LineController:
    controller = LineController(canvas, figures, get_bg=bg.get)
    controller.bind()
    return controller


def line_delete(canvas: Canvas, controller: LineController):
    controller.unbind()
