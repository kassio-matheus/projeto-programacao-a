from tkinter import Canvas, StringVar

from .circle_controller import CircleController
from prodraw.models.shapes import Circle


def circle_bind(canvas: Canvas, figures: dict, bg: StringVar) -> CircleController:
    controller = CircleController(canvas, figures, get_bg=bg.get)
    controller.bind()
    return controller


def circle_sync_data(canvas: Canvas, figures: list, data: list) -> CircleController:
    controller = CircleController(canvas, figures, get_bg=lambda: "#000000")

    formated_data = {
        "x": data[0],
        "y": data[1],
        "radius": data[2],
        "bg": data[3]
    }

    controller.view.draw(**formated_data)

    return controller


def circle_delete(canvas: Canvas, controller: CircleController):
    controller.unbind()
