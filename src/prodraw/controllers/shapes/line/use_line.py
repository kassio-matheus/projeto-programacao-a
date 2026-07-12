from tkinter import Canvas, StringVar

from .line_controller import LineController
from prodraw.models.shapes import Line


def line_bind(canvas: Canvas, figures: dict, bg: StringVar) -> LineController:
    controller = LineController(canvas, figures, get_bg=bg.get)
    controller.bind()
    return controller


def line_sync_data(canvas: Canvas, figures: list, data: list) -> LineController:
    controller = LineController(canvas, figures, get_bg=lambda: "#000000")

    formated_data = {
        "start_x": data[0],
        "start_y": data[1],
        "end_x": data[2],
        "end_y": data[3],
        "distance": data[4],
        "bg": data[5]
    }

    controller.view.draw(**formated_data)

    return controller


def line_delete(canvas: Canvas, controller: LineController):
    controller.unbind()
