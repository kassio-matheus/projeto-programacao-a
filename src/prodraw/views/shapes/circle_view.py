from dataclasses import dataclass
from tkinter import Canvas

from prodraw.config import SHAPE_COLORS


@dataclass
class CircleView:
    """All you know how to do is draw circles from pre-existing data."""

    canvas: Canvas = None

    def draw_preview(self, x: float, y: float, radius: float, bg: str):
        """Draw a preview of the circle being built (while dragging)."""

        self.canvas.delete("circle_preview")
        self.canvas.create_oval(
            x - radius, y - radius, x + radius, y + radius,
            fill=SHAPE_COLORS.get(bg), outline=bg,
            tags=("circle_preview", "shape"))

    def draw(self, x: float, y: float, radius: float, bg: str) -> int:
        """Draws a single circle."""
        return self.canvas.create_oval(
            x - radius, y - radius, x + radius, y + radius,
            fill=SHAPE_COLORS.get(bg), outline=bg,
            tags=("circle", "shape"))

    def clear_preview(self):
        self.canvas.delete("circle_preview")

    def delete(self):
        self.canvas.delete("circle")
        self.canvas.delete("circle_preview")
