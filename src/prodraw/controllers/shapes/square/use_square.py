from tkinter import Canvas, StringVar

from .square_controller import SquareController
from prodraw.views.shapes import SquareView


def square_bind(canvas: Canvas, figures: dict, bg: StringVar) -> SquareController:
    controller = SquareController(canvas, figures, get_bg=bg.get)
    controller.bind()
    return controller


def square_sync_data(canvas: Canvas, figures: list, data: list) -> SquareController:
    view = SquareView(canvas=canvas)
    controller = SquareController(
        canvas, figures, get_bg=lambda: "#000000", view=view)

    formated_data = {
        "shape_id": data[0],
        "start_x": data[1],
        "start_y": data[2],
        "end_x": data[3],
        "end_y": data[4],
        "distance_x": data[5],
        "bg": data[6]
    }

    controller.view.draw(**formated_data)

    return controller


def square_delete(canvas: Canvas, controller: SquareController):
    controller.unbind()
