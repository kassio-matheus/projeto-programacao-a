from tkinter import Canvas
from prodraw.models.workspace.clear_draws_model import ClearDrawsModel
from prodraw.views.workspace.clear_draws_view import ClearDrawsView
from .draws_controller import DrawsController


class ClearDrawsController:
    """Wires the clear button to the draws deletion logic."""

    def __init__(self, canvas: Canvas, figures: dict):
        self.canvas = canvas
        self.figures = figures
        self.model = ClearDrawsModel()
        self.view = ClearDrawsView(canvas, self.model)

    def setup(self):
        self.view.render(on_click=self._on_click)

    def _on_click(self):
        DrawsController(self.canvas, self.figures).delete_all()
