from tkinter import Canvas, StringVar

from .freedraw_controller import FreeDrawController
from prodraw.models.shapes import FreeDraw


def freedraw_bind(canvas: Canvas, figures: dict, bg: StringVar) -> FreeDrawController:
    controller = FreeDrawController(canvas, figures, get_bg=bg.get)
    controller.bind()
    return controller


def freedraw_sync_data(canvas: Canvas, figures: list, data: list) -> FreeDrawController:
    controller = FreeDrawController(canvas, figures, get_bg=lambda: "#000000")

    formated_data = {
        "start_x": data[0],
        "start_y": data[1],
        "end_x": data[2],
        "end_y": data[3],
        "bg": data[4]
    }

    controller.view.draw(**formated_data)

    return controller


def freedraw_delete(canvas: Canvas, controller: FreeDrawController):
    controller.unbind()
