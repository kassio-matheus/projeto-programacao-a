from tkinter import *

from .button import Button


class FreeDraw(Button):
    """Represents a freehand drawing tool button in the toolbar."""
    
    # Initializes the freehand button properties and state watchers
    def __init__(self, toolsbar: Frame, width: int = 50, height: int = 50,
                 command=None, padding: int = 8, background: str = "#303035",
                 shape_colors: dict = None, selected_color_var: StringVar = None,
                 selected_option: StringVar = None, selected_key: str = "freedraw"):
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
    # Returns True if the freehand tool is currently active
    def is_selected(self) -> bool:
        return self.selected_option is not None and self.selected_option.get() == self.selected_key

    # Draws the freehand squiggle icon and updates colors based on selection state
    def draw(self):
        if self.icon_id is not None:
            self.canvas.delete(self.icon_id)

        line_color = self.selected_color_var.get(
        ) if self.selected_color_var and self.is_selected else "#FFFFFF"

        bg_color = self.shape_colors.get(
            line_color, self.background) if self.is_selected else self.background

        # Signals selection by changing the canvas background, since a line has no internal fill
        self.canvas.configure(bg=bg_color)

        w, h = self.width, self.height
        p = self.padding

        # Points proportional to button size, forming a squiggle to represent freehand drawing
        points = [
            p,           h * 0.55,
            w * 0.28,    h * 0.20,
            w * 0.42,    h * 0.70,
            w * 0.58,    h * 0.25,
            w * 0.72,    h * 0.65,
            w - p,       h * 0.35,
        ]

        self.icon_id = self.canvas.create_line(
            *points,
            fill=line_color,
            width=2,
            smooth=True,
            splinesteps=24,
            capstyle=ROUND,
            joinstyle=ROUND,
        )