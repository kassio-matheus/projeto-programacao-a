from tkinter import Canvas, StringVar

from .oval_controller import OvalController
from prodraw.models.shapes import Oval


def oval_bind(canvas: Canvas, figures: dict, bg: StringVar) -> OvalController:
    controller = OvalController(canvas, figures, get_bg=bg.get)
    controller.bind()
    return controller


def oval_sync_data(canvas: Canvas, figures: list, data: list) -> OvalController:
    controller = OvalController(canvas, figures, get_bg=lambda: "#000000")

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


def oval_delete(canvas: Canvas, controller: OvalController):
    controller.unbind()
