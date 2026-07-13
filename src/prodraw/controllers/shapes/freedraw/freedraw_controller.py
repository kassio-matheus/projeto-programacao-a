from tkinter import Event
from dataclasses import dataclass, field

from prodraw.models import FreeDraw
from prodraw.views import FreeDrawView
from prodraw.controllers.shapes.tools import *


@dataclass
class FreeDrawController(Tools):
    """Bridges raw Tkinter mouse events and the FreeDraw model/view.
    This is the only layer allowed to know about both Tkinter events
    and business rules (model state)."""

    current: FreeDraw = None
    positions: list = field(default_factory=list)
    positions_preview: list = field(default_factory=list)

    def _on_press(self, event: Event):
        """Step 1: mouse down starts a new, uncommitted freedraw.
        A fresh FreeDraw instance is created per press — no shared
        class-level state between draws."""
        self.current = FreeDraw(bg=self.get_bg())
        self.current.start(event.x, event.y)

        freedraw_data = (event.x, event.y)
        self.positions.append(freedraw_data)
        self.positions_preview.append(freedraw_data)

    def _on_drag(self, event: Event):
        """Step 2: mouse movement updates the in-progress freedraw's
        and renders a preview only, never touching the
        confirmed figures list."""
        self.current.update(event.x, event.y)

        if self.current.has_min_size():
            self.view.draw(
                self.current.shape_id, self.current.start_x, self.current.start_y, self.current.end_x, self.current.end_y, self.current.bg)
            self.current.start_x = self.current.end_x
            self.current.start_y = self.current.end_y

        freedraw_data = (event.x, event.y)
        self.positions.append(freedraw_data)
        self.positions_preview.append(freedraw_data)

    def _on_release(self, event: Event):
        if len(self.positions_preview) == 1:
            p = self.positions_preview[0]
            self.positions_preview.append(p)
            self.positions.append(p)

        self.figures['FreeDraw'].append(
            {"bg": self.get_bg(), "positions": self.positions, "shape_id": self.current.shape_id})

        self.view.clear_preview()

        if len(self.positions_preview) >= 2:
            self.view.draw_path(self.current.shape_id,
                                self.positions_preview, bg=self.get_bg())

        self.positions = []
        self.positions_preview = []
        self.current = None
