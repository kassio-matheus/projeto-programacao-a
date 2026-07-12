from tkinter import Canvas, StringVar

from .rectangle_controller import RectangleController
from prodraw.models.shapes import Rectangle


def rectangle_bind(canvas: Canvas, figures: dict, bg: StringVar) -> RectangleController:
    controller = RectangleController(canvas, figures, get_bg=bg.get)
    controller.bind()
    return controller


def rectangle_sync_data(canvas: Canvas, figures: list, data: list) -> RectangleController:
    controller = RectangleController(canvas, figures, get_bg=lambda: "#000000")

    formated_data = {
        "start_x": data[0],
        "start_y": data[1],
        "end_x": data[2],
        "end_y": data[3],
        "distance_x": data[4],
        "distance_y": data[5],
        "bg": data[6]
    }

    controller.view.draw(**formated_data)

    return controller


def rectangle_delete(canvas: Canvas, controller: RectangleController):
    controller.unbind()
