from tkinter import Canvas
from prodraw.models.workspace.zoom_model import ZoomModel


class ZoomView:
    """Applies the zoom transformation to canvas shapes."""

    def __init__(self, canvas: Canvas, model: ZoomModel):
        self.canvas = canvas
        self.model = model

    def apply_scale(self, x: float, y: float, scale_step: float):
        """Scale all 'shape'-tagged items around the given canvas point."""
        self.canvas.scale("shape", x, y, scale_step, scale_step)
