from tkinter import Canvas, Event
from prodraw.models.workspace.grids_model import GridsModel


class GridsView:
    """Renders the dot-grid background on the canvas."""

    def __init__(self, canvas: Canvas, model: GridsModel):
        self.canvas = canvas
        self.model = model

    def draw(self, event: Event):
        """Clear and redraw the full dot grid to match the current canvas size."""
        self.canvas.delete("grids")

        width = self.canvas.winfo_width()
        height = self.canvas.winfo_height()

        for x in range(0, width, self.model.grid_size):
            for y in range(0, height, self.model.grid_size):
                self.canvas.create_oval(
                    x - 1, y - 1, x + 1, y + 1,
                    fill=self.model.dot_color, outline="", tags="grids"
                )

        self.canvas.tag_lower("grids")
