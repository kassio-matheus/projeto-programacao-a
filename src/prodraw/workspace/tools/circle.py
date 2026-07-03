from tkinter import *

from .button import Button


class Circle(Button):
    """Represents a circle tool button in the toolbar."""
    
    # Initializes the circle button properties and state watchers
    def __init__(self, toolsbar: Frame, width: int = 50, height: int = 50,
                 command=None, padding: int = 8, background: str = "#303035",
                 shape_colors: dict = None, selected_color_var: StringVar = None,
                 selected_option: StringVar = None, selected_key: str = "circle"):
        super().__init__(
            toolsbar=toolsbar, width=width, height=height, command=command,
            watch_vars=(selected_option, selected_color_var)
        )
        self.padding = padding
        self.background = background
        self.shape_colors = shape_colors or {}
        self.selected_color_var = selected_color_var
        self.selected_option = selected_option
        self.selected_key = selected_key

    @property
    # Returns True if the circle tool is currently active
    def is_selected(self) -> bool:
        return self.selected_option is not None and self.selected_option.get() == self.selected_key

    # Draws the circle icon and updates colors based on selection state
    def draw(self):
        if self.icon_id is not None:
            self.canvas.delete(self.icon_id)

        border_color = self.selected_color_var.get(
        ) if self.selected_color_var and self.is_selected else "#FFFFFF"
        fill_color = self.shape_colors.get(
            border_color, "white") if self.is_selected else self.background

        self.canvas.configure(bg=fill_color)

        self.icon_id = self.canvas.create_oval(
            self.padding, self.padding,
            self.width - self.padding, self.height - self.padding,
            outline=border_color,
            fill=fill_color,
        )