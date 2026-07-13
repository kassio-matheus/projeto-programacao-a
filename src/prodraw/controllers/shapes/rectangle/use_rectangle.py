from tkinter import Canvas, StringVar

from .rectangle_controller import RectangleController
from prodraw.views.shapes import RectangleView


def rectangle_bind(canvas: Canvas, figures: dict, bg: StringVar) -> RectangleController:
    controller = RectangleController(canvas, figures, get_bg=bg.get)
    controller.bind()
    return controller


def rectangle_sync_data(canvas: Canvas, figures: list, data: list) -> RectangleController:
    view = RectangleView(canvas=canvas)
    controller = RectangleController(
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



def rectangle_delete(canvas: Canvas, controller: RectangleController):
    controller.unbind()
