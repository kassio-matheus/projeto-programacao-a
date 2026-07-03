from tkinter import *

from .config import DRAW_TOOLS


class Select:
    def __init__(self, canvas: Canvas):
        self.canvas = canvas
        pass

    def select_option(self, option, selected_color_var: StringVar, figures: list):
        DRAW_TOOLS[option](
            canvas=self.canvas, bg=selected_color_var, figures=figures)
