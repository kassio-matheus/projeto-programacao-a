from tkinter import Canvas, StringVar

from .oval_controller import OvalController


def oval_bind(canvas: Canvas, figures: dict, bg: StringVar) -> OvalController:
    controller = OvalController(canvas, figures, get_bg=bg.get)
    controller.bind()
    return controller


def oval_delete(canvas: Canvas, controller: OvalController):
    controller.unbind()
