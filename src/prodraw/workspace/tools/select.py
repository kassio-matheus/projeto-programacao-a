from tkinter import *

from .config import DRAW_TOOLS


class Select:
    def __init__(self, canvas: Canvas, selected_option: StringVar):
        self.canvas = canvas
        self.selected_option = selected_option

    def select_option(self, option, selected_color_var: StringVar, figures: list):
        self.selected_option.set(option)

        DRAW_TOOLS[option](
            canvas=self.canvas, bg=selected_color_var, figures=figures)
