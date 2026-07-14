from dataclasses import dataclass
from typing import Callable

from prodraw.config import SHAPE_COLORS


@dataclass
class SquareView:
    """All you know how to do is draw square from pre-existing data."""

    canvas: Callable = None

    def draw_preview(self, start_x: float, start_y: float, end_x: float, end_y: float, bg: str):
        """Draw a preview of the rectangle being built (while dragging)."""

        self.canvas.create_rectangle(
            start_x, start_y, end_x, end_y,
            fill=SHAPE_COLORS.get(bg), outline=bg,
            tags=("square_preview", "shape"))

    def draw(self, shape_id: int, start_x: float, start_y: float, end_x: float, end_y: float, distance_x: float, bg: str) -> int:
        """Draws a single circle."""

        return self.canvas.create_rectangle(
            start_x, start_y, end_x, end_y,
            fill=SHAPE_COLORS.get(bg), outline=bg,
            tags=("square", "shape", f"id_{shape_id}"))

    def clear_preview(self):
        self.canvas.delete("square_preview")

    def delete(self, shape_id: int):
        self.canvas.delete(shape_id)
        self.canvas.delete("square_preview")
