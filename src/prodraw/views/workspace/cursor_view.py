from tkinter import Canvas
from dataclasses import dataclass
from prodraw.models.workspace.cursor_model import CursorModel


@dataclass
class CursorView:
    """Renders rectangle selector on drag pressed mouse."""
    canvas: Canvas = None

    def draw(self, start_x: float, start_y: float, end_x: float, end_y: float, outline: str):
        return self.canvas.create_rectangle(
            start_x, start_y, end_x, end_y,
            outline=outline,
            dash=(4, 4),
            tags=("cursor"))

    def clear_view_selection(self):
        self.canvas.delete("cursor")
