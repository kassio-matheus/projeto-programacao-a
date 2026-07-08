from dataclasses import dataclass
from tkinter import Canvas

from prodraw.config import SHAPE_COLORS


@dataclass
class OvalView:
    """All you know how to do is draw oval from pre-existing data."""

    canvas: Canvas

    def draw_preview(self, start_x: float, start_y: float, end_x: float, end_y: float, bg: str):
        """Draw a preview of the oval being built (while dragging)."""

        self.canvas.delete("oval_preview")
        self.canvas.create_oval(
            start_x, start_y, end_x, end_y,
            fill=SHAPE_COLORS.get(bg), outline=bg,
            tags=("oval_preview", "shape"))

    def draw(self, start_x: float, start_y: float, end_x: float, end_y: float, distance_x: float, distance_y: float, bg: str) -> int:
        """Draws a single oval."""
        return self.canvas.create_oval(
            start_x, start_y, end_x, end_y,
            fill=SHAPE_COLORS.get(bg), outline=bg,
            tags=("oval", "shape"))

    def clear_preview(self):
        self.canvas.delete("oval_preview")

    def delete(self):
        self.canvas.delete("oval")
        self.canvas.delete("oval_preview")
