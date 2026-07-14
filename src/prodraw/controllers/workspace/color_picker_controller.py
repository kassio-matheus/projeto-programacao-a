from tkinter import Canvas, StringVar

from prodraw.models.workspace.color_picker_model import ColorPickerModel, DEFAULT_COLOR
from prodraw.views.workspace.color_picker_view import ColorPickerView
from prodraw.controllers.workspace.cursor_controller import CursorController
from prodraw.config.colors import SHAPE_COLORS


class ColorPickerController:
    """Connects the color picker model and view; handles color selection."""

    def __init__(self, canvas: Canvas, cursor: CursorController = None):
        self.model = ColorPickerModel()
        self.view = ColorPickerView(canvas, self.model)
        self.cursor = cursor

    def setup(self) -> StringVar:
        """Build the color picker UI and return the active color StringVar."""
        self.view.build(on_color_click=self._on_select)
        self._on_select(DEFAULT_COLOR)
        return self.model.selected_color_var

    def _on_select(self, color: str):
        """Update the model and refresh button highlights on color change."""
        previous = self.model.get_color()

        self.view.unhighlight(previous)
        self.model.set_color(color)
        self.view.highlight(color)

        if (self.cursor):
            self.cursor.change_shape_color(
                bg_color=SHAPE_COLORS.get(color), outline_color=color)
