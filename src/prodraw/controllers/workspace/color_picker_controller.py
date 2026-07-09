from tkinter import Canvas, StringVar
from prodraw.models.workspace.color_picker_model import ColorPickerModel, DEFAULT_COLOR
from prodraw.views.workspace.color_picker_view import ColorPickerView


class ColorPickerController:
    """Connects the color picker model and view; handles color selection."""

    def __init__(self, canvas: Canvas):
        self.model = ColorPickerModel()
        self.view = ColorPickerView(canvas, self.model)

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
