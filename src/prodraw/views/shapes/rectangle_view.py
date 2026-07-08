from dataclasses import dataclass
from tkinter import Canvas

from prodraw.config import SHAPE_COLORS


@dataclass
class RectangleView:
    """All you know how to do is draw rectahgoe from pre-existing data."""

    canvas: Canvas

    def draw_preview(self, start_x: float, start_y: float, end_x: float, end_y: float, bg: str):
        """Draw a preview of the rectangle being built (while dragging)."""

        self.canvas.delete("rectangle_preview")
        self.canvas.create_rectangle(
            start_x, start_y, end_x, end_y,
            fill=SHAPE_COLORS.get(bg), outline=bg,
            tags=("rectangle_preview", "shape"))

    def draw(self, start_x: float, start_y: float, end_x: float, end_y: float, distance: float, bg: str) -> int:
        """Draws a single circle and returns its canvas item id (useful for undo)."""
        return self.canvas.create_rectangle(
            start_x, start_y, end_x, end_y,
            fill=SHAPE_COLORS.get(bg), outline=bg,
            tags=("rectangle", "shape"))

    def clear_preview(self):
        self.canvas.delete("rectangle_preview")

    def delete(self):
        self.canvas.delete("rectangle")
        self.canvas.delete("rectangle_preview")
