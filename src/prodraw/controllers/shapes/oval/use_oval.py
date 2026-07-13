from tkinter import Canvas, StringVar

from .oval_controller import OvalController
from prodraw.views.shapes import OvalView


def oval_bind(canvas: Canvas, figures: dict, bg: StringVar) -> OvalController:
    controller = OvalController(canvas, figures, get_bg=bg.get)
    controller.bind()
    return controller


def oval_sync_data(canvas: Canvas, figures: list, data: list) -> OvalController:
    view = OvalView(canvas=canvas)
    controller = OvalController(
        canvas, figures, get_bg=lambda: "#000000", view=view)

    formated_data = {
        "shape_id": data[0],
        "start_x": data[1],
        "start_y": data[2],
        "end_x": data[3],
        "end_y": data[4],
        "distance_x": data[5],
        "distance_y": data[6],
        "bg": data[7]
    }

    controller.view.draw(**formated_data)

    return controller


def oval_delete(canvas: Canvas, controller: OvalController):
    controller.unbind()
