from tkinter import *

from .config import PANEL_BG
from .config import SELECTED_BG


class Select:
    def __init__(self, selected_color_var, canvas_by_color):
        self.selected_color_var: StringVar = selected_color_var
        self.canvas_by_color = canvas_by_color

    def select_color(self, color):
        previous = self.selected_color_var.get()

        if previous in self.canvas_by_color:
            self.canvas_by_color[previous].config(bg=PANEL_BG)

        self.canvas_by_color[color].config(bg=SELECTED_BG)
        self.selected_color_var.set(color)
