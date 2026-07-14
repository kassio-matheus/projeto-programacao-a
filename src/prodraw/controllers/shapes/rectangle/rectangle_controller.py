from tkinter import Event
from dataclasses import dataclass

from prodraw.models import Rectangle

from prodraw.views import RectangleView

from prodraw.controllers.shapes.tools import Tools


@dataclass
class RectangleController(Tools):
    """Bridges raw Tkinter mouse events and the Rectangle model/view.
    This is the only layer allowed to know about both Tkinter events
    and business rules (model state)."""

    current: Rectangle = None

    def _on_press(self, event: Event):
        """Step 1: mouse down starts a new, uncommitted rectangle.
        A fresh Rectangle instance is created per press — no shared
        class-level state between draws."""

        self.current = Rectangle(bg=self.get_bg())
        self.current.start(event.x, event.y)

    def _on_drag(self, event: Event):
        """Step 2: mouse movement updates the in-progress rectangle's
        and renders a preview only, never touching the
        confirmed figures list."""

        self.current.update(event.x, event.y)
        
        if self.current.has_min_size():
            self.view.clear_preview()

            self.view.draw_preview(
                self.current.start_x, self.current.start_y, self.current.end_x, self.current.end_y, self.current.bg)

    def _on_release(self, event: Event):
        """Step 3: mouse up commits the rectangle if it meets the minimum
        size. The confirmed rectangle is appended to the model and drawn
        once via draw — never redrawing the whole canvas here,
        since already-drawn rectangles are immutable and don't need to
        be redrawn."""

        if self.current is not None and self.current.has_min_size():
            rectangle_data = self.current.to_tuple()
            self.figures['Rectangle'].append(rectangle_data)
            self.view.draw(*rectangle_data)

        self.view.clear_preview()
        self.current = None
