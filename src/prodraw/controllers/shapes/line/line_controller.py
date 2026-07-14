from tkinter import Event
from dataclasses import dataclass

from prodraw.models import Line
from prodraw.views import LineView
from prodraw.controllers.shapes.tools import Tools


@dataclass
class LineController(Tools):
    """Bridges raw Tkinter mouse events and the Line model/view.
    This is the only layer allowed to know about both Tkinter events
    and business rules (model state)."""

    current: Line = None

    def _on_press(self, event: Event):
        """Step 1: mouse down starts a new, uncommitted line.
        A fresh Line instance is created per press — no shared
        class-level state between draws."""
        self.current = Line(bg=self.get_bg())
        self.current.start(event.x, event.y)

    def _on_drag(self, event: Event):
        """Step 2: mouse movement updates the in-progress line's
        and renders a preview only, never touching the
        confirmed figures list."""
        self.current.update(event.x, event.y)
        if self.current is not None and self.current.has_min_size():
            self.view.clear_preview()

            self.view.draw_preview(
                self.current.start_x, self.current.start_y, self.current.end_x, self.current.end_y, self.current.bg)

    def _on_release(self, event: Event):
        """Step 3: mouse up commits the line if it meets the minimum
        size. The confirmed line is appended to the model and drawn
        once via draw — never redrawing the whole canvas here,
        since already-drawn lines are immutable and don't need to
        be redrawn."""
        if self.current is not None and self.current.has_min_size():
            line_data = self.current.to_tuple()
            self.figures['Line'].append(line_data)
            self.view.draw(*line_data)
        self.view.clear_preview()
        self.current = None
