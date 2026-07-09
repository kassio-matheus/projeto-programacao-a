from tkinter import Canvas, Frame
from prodraw.models.workspace.toolbar_model import ToolbarModel, TOOLBAR_BG
from prodraw.models.workspace.color_picker_model import SHAPE_COLORS


class ToolbarView:
    """Renders the toolbar frame and all tool icon buttons."""

    def __init__(self, canvas: Canvas, model: ToolbarModel):
        self.canvas = canvas
        self.model = model
        self.frame: Frame = None

    def build(self) -> Frame:
        """Create the toolbar frame at the bottom center of the canvas."""
        self.frame = Frame(self.canvas, bg=self.model.background,
                           width=self.model.width, height=self.model.height)
        self.frame.place(relx=0.5, rely=1.0, anchor="s", y=-30)
        return self.frame

    def create_tool_button(self, tool_cls, selected_color_var, selected_option,
                           selected_key, on_click):
        """Instantiate and render a single tool button.

        Args:
            tool_cls: One of the Button subclasses (Rectangle, Circle, etc.).
            selected_color_var: StringVar for the active color.
            selected_option: StringVar for the active tool key.
            selected_key: The string key this button represents.
            on_click: Callback called when the button is pressed.
        """
        btn = tool_cls(
            self.frame,
            width=self.model.button_size,
            height=self.model.height,
            background=self.model.background,
            shape_colors=SHAPE_COLORS,
            selected_color_var=selected_color_var,
            selected_option=selected_option,
            selected_key=selected_key,
            command=lambda event: on_click(selected_key),
            padding=self.model.button_padding,
        )
        btn.create_button()
        return btn
