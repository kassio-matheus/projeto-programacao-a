from tkinter import Canvas, StringVar

from .freedraw_controller import FreeDrawController
from prodraw.views.shapes import FreeDrawView


def freedraw_bind(canvas: Canvas, figures: dict, bg: StringVar) -> FreeDrawController:
    controller = FreeDrawController(canvas, figures, get_bg=bg.get)
    controller.bind()
    return controller


def freedraw_sync_data(canvas: Canvas, figures: list, data: dict) -> FreeDrawController:
    view = FreeDrawView(canvas)
    controller = FreeDrawController(
        canvas, figures, get_bg=lambda: "#000000", view=view)

    shape_id = data.get("shape_id", [])
    positions = data.get("positions", [])
    bg_color = data.get("bg", "#000000")

    controller.view.draw_path(shape_id, positions, bg=bg_color)

    return controller


def freedraw_delete(canvas: Canvas, controller: FreeDrawController):
    controller.unbind()
