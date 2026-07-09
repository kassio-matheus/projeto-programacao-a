from tkinter import Canvas, Event
from typing import Callable

from prodraw.models import Circle
from prodraw.views import CircleView


class CircleController:
    """Bridges raw Tkinter mouse events and the Circle model/view.
    This is the only layer allowed to know about both Tkinter events
    and business rules (model state)."""

    def __init__(self, canvas: Canvas, figures: dict, get_bg: Callable[[], str]):
        self.canvas = canvas
        self.figures = figures
        self.get_bg = get_bg  # callable, e.g. selected_color_var.get
        self.view = CircleView(canvas)
        self.current: Circle = None

    def bind(self):
        """Attach mouse event handlers to the canvas."""
        self.canvas.bind('<ButtonPress-1>', self._on_press)
        self.canvas.bind('<B1-Motion>', self._on_drag)
        self.canvas.bind('<ButtonRelease-1>', self._on_release)

    def unbind(self):
        """Detach mouse event handlers and clear any drawn circles.
        Must be called when switching tools, otherwise stale bindings
        keep reacting to mouse events meant for the next tool."""
        self.canvas.unbind('<ButtonPress-1>')
        self.canvas.unbind('<B1-Motion>')
        self.canvas.unbind('<ButtonRelease-1>')
        self.view.delete()

    def _on_press(self, event: Event):
        """Step 1: mouse down starts a new, uncommitted circle.
        A fresh Circle instance is created per press — no shared
        class-level state between draws."""
        self.current = Circle(bg=self.get_bg())
        self.current.start(event.x, event.y)

    def _on_drag(self, event: Event):
        """Step 2: mouse movement updates the in-progress circle's
        radius and renders a preview only, never touching the
        confirmed figures list."""
        self.current.update(event.x, event.y)
        if self.current.has_min_size():
            self.view.draw_preview(
                self.current.start_x, self.current.start_y,
                self.current.radius, self.current.bg)

    def _on_release(self, event: Event):
        """Step 3: mouse up commits the circle if it meets the minimum
        size. The confirmed circle is appended to the model and drawn
        once via draw — never redrawing the whole canvas here,
        since already-drawn circles are immutable and don't need to
        be redrawn."""
        if self.current is not None and self.current.has_min_size():
            circle_data = self.current.to_tuple()
            self.figures['Circle'].append(circle_data)
            self.view.draw(*circle_data)
        self.view.clear_preview()
        self.current = None