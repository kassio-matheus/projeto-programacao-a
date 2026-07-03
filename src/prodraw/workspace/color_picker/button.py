from tkinter import *

from .config import BUTTON_SIZE
from .config import PANEL_BG
from .config import SELECTED_BG

from .select import Select


class Button:
    def __init__(self, canvas: Canvas, panel, row, column, color, canvas_by_color, selected_color_var):
        self.canvas = canvas
        self.panel = panel
        self.row = row
        self.column = column
        self.color = color
        self.canvas_by_color = canvas_by_color
        self.selected_color_var = selected_color_var

    def create_color_button(self, select: Select):
        cv = Canvas(
            self.panel, width=BUTTON_SIZE, height=BUTTON_SIZE,
            bg=PANEL_BG, highlightthickness=0, cursor="hand2"
        )
        cv.grid(row=self.row, column=self.column, padx=4, pady=4)

        cv.create_oval(6, 6, BUTTON_SIZE - 6, BUTTON_SIZE -
                       6, fill=self.color, outline="")
        cv.bind("<Button-1>", lambda e, c=self.color: select.select_color(c))

        self.canvas_by_color[self.color] = cv

        if self.color == self.selected_color_var.get():
            cv.config(bg=SELECTED_BG)
