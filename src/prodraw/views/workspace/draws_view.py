from tkinter import Canvas
from prodraw.models.workspace.draws_model import DrawsModel


class DrawsView:
    """Handles visual clearing of all drawings from the canvas."""

    def __init__(self, canvas: Canvas, model: DrawsModel):
        self.canvas = canvas
        self.model = model

    def clear_canvas(self):
        """Delete every shape-related tag from the canvas."""
        for tag in self.model.SHAPE_TAGS:
            self.canvas.delete(tag)
