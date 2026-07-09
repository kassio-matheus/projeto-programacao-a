from tkinter import Canvas, Event
from prodraw.models.workspace.zoom_model import ZoomModel
from prodraw.views.workspace.zoom_view import ZoomView


class ZoomController:
    """Handles mouse-wheel events and applies zoom to the canvas."""

    def __init__(self, canvas: Canvas):
        self.canvas = canvas
        self.model = ZoomModel()
        self.view = ZoomView(canvas, self.model)

    def on_scroll(self, event: Event):
        """Compute the new zoom factor and apply it centered on the cursor."""
        x = self.canvas.canvasx(event.x)
        y = self.canvas.canvasy(event.y)

        if event.delta > 0:
            new_factor = min(round(ZoomModel.factor + ZoomModel.STEP, 1), ZoomModel.MAX)
        else:
            new_factor = max(round(ZoomModel.factor - ZoomModel.STEP, 1), ZoomModel.MIN)

        if new_factor == ZoomModel.factor:
            return

        scale_step = new_factor / ZoomModel.factor
        self.view.apply_scale(x, y, scale_step)
        ZoomModel.factor = new_factor
