from dataclasses import dataclass
from tkinter import Canvas

from prodraw.config import SHAPE_COLORS


@dataclass
class FreeDrawView:
    """All you know how to do is free draw from pre-existing data."""

    canvas: Canvas = None

    def draw_preview(self):
        """Draw a preview of the FreeDraw being built (while dragging)."""
        pass

    def draw(self, start_x: float, start_y: float, end_x: float, end_y: float, bg: str) -> int:
        """Draws the free draw."""

        self.canvas.create_line(
            start_x, start_y, end_x, end_y,
            fill=bg,
            width=2,
            tags=("freedraw", "shape"))

    def clear_preview(self):
        # self.canvas.delete("freedraw_preview")
        pass

    def delete(self):
        self.canvas.delete("freedraw")
        # self.canvas.delete("freedraw_preview")
