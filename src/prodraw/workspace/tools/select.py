from tkinter import *

from .config import DRAW_TOOLS


class Select:
    """Handles the selection and activation of drawing tools."""
    
    # Initializes the tool selector with the target canvas
    def __init__(self, canvas: Canvas):
        self.canvas = canvas
        pass

    # Triggers the corresponding drawing tool function based on the selected option
    def select_option(self, option, selected_color_var: StringVar, figures: list):
        DRAW_TOOLS[option](
            canvas=self.canvas, bg=selected_color_var, figures=figures)