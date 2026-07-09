from tkinter import Canvas
from prodraw.models.workspace.draws_model import DrawsModel
from prodraw.views.workspace.draws_view import DrawsView


class DrawsController:
    """Coordinates clearing all drawings from the canvas and memory."""

    def __init__(self, canvas: Canvas, figures: dict):
        self.model = DrawsModel(figures)
        self.view = DrawsView(canvas, self.model)

    def delete_all(self):
        """Remove all shapes from the canvas and reset the figures dict."""
        self.view.clear_canvas()
        for key in self.model.figures:
            self.model.figures[key].clear()
