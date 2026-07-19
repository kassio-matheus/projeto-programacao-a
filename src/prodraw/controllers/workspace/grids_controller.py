from tkinter import Canvas, Event

from prodraw.models.workspace.grids_model import GridsModel
from prodraw.views.workspace.grids_view import GridsView


class GridsController:
    """Handles grid redraws triggered by canvas resize events."""

    def __init__(self, canvas: Canvas,):
        self.canvas = canvas
        
        self.model = GridsModel()
        self.view = GridsView(canvas, self.model)

    def on_resize(self, event: Event):
        """Redraw the grid and restore the version label on canvas resize."""
        self.view.draw(event)
