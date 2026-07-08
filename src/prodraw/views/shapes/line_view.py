from dataclasses import dataclass
from tkinter import Canvas

from prodraw.config import SHAPE_COLORS


@dataclass
class LineView:
    """All you know how to do is draw line from pre-existing data."""

    canvas: Canvas

    def draw_preview(self, start_x: float, start_y: float, end_x: float, end_y: float, bg: str):
        """Draw a preview of the rectangle being built (while dragging)."""

        self.canvas.delete("line_preview")
        self.canvas.create_line(
            start_x, start_y, end_x, end_y,
            fill=bg,
            tags=("line_preview", "shape"))

    def draw(self, start_x: float, start_y: float, end_x: float, end_y: float, distance: float, bg: str) -> int:
        """Draws a single line."""
        return self.canvas.create_line(
            start_x, start_y, end_x, end_y,
            fill=bg,
            tags=("line", "shape"))

    def clear_preview(self):
        self.canvas.delete("line_preview")

    def delete(self):
        self.canvas.delete("line")
        self.canvas.delete("line_preview")
