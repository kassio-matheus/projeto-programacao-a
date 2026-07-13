from tkinter import Event
from dataclasses import dataclass, field
from typing import List, Tuple

from prodraw.models.workspace.cursor_model import CursorModel
from prodraw.views.workspace.cursor_view import CursorView

from prodraw.controllers.shapes.tools import Tools


@dataclass
class CursorController(Tools):
    """Bridges raw Tkinter mouse events and the Cursor model/view.
    This is the only layer allowed to know about both Tkinter events
    and business rules (model state)."""

    current: CursorModel = None
    is_selected: bool = False
    selected_figures: List[Tuple[str, int]] = field(default_factory=list)

    # Keep track of the last mouse position to calculate real-time dx, dy
    last_x: float = 0.0
    last_y: float = 0.0

    def _get_selected_figures(self, sx0: float, sy0: float, sx1: float, sy1: float) -> List[Tuple[str, int]]:
        """Helper method to find all shapes within a specific bounding box."""
        selected = []
        sel_min_x, sel_max_x = min(sx0, sx1), max(sx0, sx1)
        sel_min_y, sel_max_y = min(sy0, sy1), max(sy0, sy1)

        for shape_type, shape_list in self.figures.items():
            for index, shape in enumerate(shape_list):
                # Deslocado em +1 pois shape[0] agora é o shape_id
                if shape_type in ('Rectangle', 'Oval', 'Square', 'Line'):
                    fx0, fy0, fx1, fy1 = shape[1], shape[2], shape[3], shape[4]
                    fig_min_x, fig_max_x = min(fx0, fx1), max(fx0, fx1)
                    fig_min_y, fig_max_y = min(fy0, fy1), max(fy0, fy1)

                elif shape_type == 'Circle':
                    cx, cy, r = shape[1], shape[2], shape[3]
                    fig_min_x, fig_max_x = cx - r, cx + r
                    fig_min_y, fig_max_y = cy - r, cy + r

                elif shape_type == 'FreeDraw':
                    positions = shape['positions']
                    if not positions:
                        continue
                    xs = [p[0] for p in positions]
                    ys = [p[1] for p in positions]
                    fig_min_x, fig_max_x = min(xs), max(xs)
                    fig_min_y, fig_max_y = min(ys), max(ys)
                else:
                    continue

                if (fig_min_x <= sel_max_x and fig_max_x >= sel_min_x and
                        fig_min_y <= sel_max_y and fig_max_y >= sel_min_y):
                    selected.append((shape_type, index))

        return selected

    def move_figure(self, shape_type: str, index: int, dx: float, dy: float):
        """
        Move a shape by (dx, dy).
        Updates the internal model and visually moves it on the Tkinter canvas.
        """
        shape = self.figures[shape_type][index]

        if shape_type in ('Rectangle', 'Oval'):
            shape_id, x0, y0, x1, y1, w, h, color = shape
            self.figures[shape_type][index] = (
                shape_id, x0 + dx, y0 + dy, x1 + dx, y1 + dy, w, h, color)

        elif shape_type == 'Square':
            shape_id, x0, y0, x1, y1, size, color = shape
            self.figures[shape_type][index] = (
                shape_id, x0 + dx, y0 + dy, x1 + dx, y1 + dy, size, color)

        elif shape_type == 'Line':
            shape_id, x0, y0, x1, y1, length, color = shape
            self.figures[shape_type][index] = (
                shape_id, x0 + dx, y0 + dy, x1 + dx, y1 + dy, length, color)

        elif shape_type == 'Circle':
            shape_id, cx, cy, r, color = shape
            self.figures[shape_type][index] = (
                shape_id, cx + dx, cy + dy, r, color)

        elif shape_type == 'FreeDraw':
            new_positions = [(x + dx, y + dy) for x, y in shape['positions']]
            self.figures[shape_type][index]['positions'] = new_positions

        # No final de move_figure:
        if isinstance(shape, dict):
            canvas_id = shape.get('shape_id')
        else:
            canvas_id = shape[0]

        if canvas_id is not None:
            self.canvas.move(f"id_{canvas_id}", dx, dy)

    def _on_press(self, event: Event):
        """Step 1: Check if the user clicked on a shape or empty space."""
        self.last_x = event.x
        self.last_y = event.y

        tolerance = 3
        clicked_figures = self._get_selected_figures(
            event.x - tolerance, event.y - tolerance,
            event.x + tolerance, event.y + tolerance
        )

        if clicked_figures:
            first_clicked = clicked_figures[0]
            if first_clicked not in self.selected_figures:
                self.selected_figures = [first_clicked]

            self.is_selected = True
            self.current = None
        else:
            self.selected_figures = []
            self.is_selected = False
            self.current = CursorModel()
            self.current.start(event.x, event.y)

    def _on_drag(self, event: Event):
        """Step 2: Either move the selected shapes or draw the selection box."""
        if self.is_selected and self.selected_figures:
            dx = event.x - self.last_x
            dy = event.y - self.last_y

            for shape_type, index in self.selected_figures:
                self.move_figure(shape_type, index, dx, dy)

            self.last_x = event.x
            self.last_y = event.y

        elif self.current is not None:
            self.current.update(event.x, event.y)
            self.view.draw(
                self.current.start_x, self.current.start_y,
                self.current.end_x, self.current.end_y,
                outline=self.current.outline_color
            )

    def _on_release(self, event: Event):
        """Step 3: Finish drawing the selection box (if any) and select elements inside it."""
        if not self.is_selected and self.current is not None:
            self.view.clear_view_selection()

            start_x, start_y, end_x, end_y = self.current.to_tuple()

            self.selected_figures = self._get_selected_figures(
                start_x, start_y, end_x, end_y
            )

            if self.selected_figures:
                self.is_selected = True
            self.current = None
