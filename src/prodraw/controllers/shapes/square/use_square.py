from tkinter import Canvas, StringVar

from .square_controller import SquareController
from prodraw.models.shapes import Square


def square_bind(canvas: Canvas, figures: dict, bg: StringVar) -> SquareController:
    controller = SquareController(canvas, figures, get_bg=bg.get)
    controller.bind()
    return controller


def square_sync_data(canvas: Canvas, figures: list, data: list) -> SquareController:
    controller = SquareController(canvas, figures, get_bg=lambda: "#000000")

    formated_data = {
        "start_x": data[0],
        "start_y": data[1],
        "end_x": data[2],
        "end_y": data[3],
        "distance_x": data[4],
        "bg": data[5]
    }

    controller.view.draw(**formated_data)

    return controller


def square_delete(canvas: Canvas, controller: SquareController):
    controller.unbind()
