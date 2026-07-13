from tkinter import Canvas, StringVar

from .line_controller import LineController
from prodraw.views.shapes import LineView


def line_bind(canvas: Canvas, figures: dict, bg: StringVar) -> LineController:
    controller = LineController(canvas, figures, get_bg=bg.get)
    controller.bind()
    return controller


def line_sync_data(canvas: Canvas, figures: list, data: list) -> LineController:
    view = LineView(canvas=canvas)
    controller = LineController(
        canvas, figures, get_bg=lambda: "#000000", view=view)

    formated_data = {
        "shape_id": data[0],
        "start_x": data[1],
        "start_y": data[2],
        "end_x": data[3],
        "end_y": data[4],
        "distance": data[5],
        "bg": data[6]
    }

    controller.view.draw(**formated_data)

    return controller


def line_delete(canvas: Canvas, controller: LineController):
    controller.unbind()
