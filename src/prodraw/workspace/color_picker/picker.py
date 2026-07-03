from tkinter import Frame

from .config import PANEL_BG
from .config import COLORS

from .button import Button


class Picker:
    """Constructs the color picker UI panel."""
    
    # Initializes the picker panel and state references
    def __init__(self, canvas, canvas_by_color, selected_color_var):
        self.canvas = canvas
        self.canvas_by_color = canvas_by_color
        self.selected_color_var = selected_color_var
        self.panel = Frame(canvas, bg=PANEL_BG, padx=12, pady=12)

    # Generates the grid of color buttons and positions the panel on the canvas
    def create_color_picker(self, select):
        for row, row_colors in enumerate(COLORS):
            for column, color in enumerate(row_colors):
                Button(self.canvas, self.panel, row, column, color, self.canvas_by_color,
                       self.selected_color_var).create_color_button(select)

        # pin to the top-right corner, with a 16px margin
        self.panel.place(relx=1.0, x=-16, y=16, anchor="ne")

    # Placeholder method for future color selection logic
    def select_color(self):
        pass