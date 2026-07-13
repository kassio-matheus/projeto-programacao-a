from dataclasses import dataclass
from tkinter import Canvas

from prodraw.config import SHAPE_COLORS


@dataclass
class RectangleView:
    """All you know how to do is draw rectangle from pre-existing data."""

    canvas: Canvas = None

    def draw_preview(self, start_x: float, start_y: float, end_x: float, end_y: float, bg: str):
        """Draw a preview of the rectangle being built (while dragging)."""

        self.canvas.delete("rectangle_preview")
        self.canvas.create_rectangle(
            start_x, start_y, end_x, end_y,
            fill=SHAPE_COLORS.get(bg), outline=bg,
            tags=("rectangle_preview", "shape"))

    def draw(self, shape_id: int, start_x: float, start_y: float, end_x: float, end_y: float, distance_x: float, distance_y: float, bg: str) -> int:
        """Draws a single circle."""

        return self.canvas.create_rectangle(
            start_x, start_y, end_x, end_y,
            fill=SHAPE_COLORS.get(bg), outline=bg,
            tags=("rectangle", "shape", f"id_{shape_id}"))

    def clear_preview(self):
        self.canvas.delete("rectangle_preview")

    def delete(self, shape_id: int):
        self.canvas.delete(shape_id)
        self.canvas.delete("rectangle_preview")
