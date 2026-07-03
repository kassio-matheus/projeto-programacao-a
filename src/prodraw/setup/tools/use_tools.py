from tkinter import *

from .config import DRAW_TOOLS

from .select import Select
from .menu import Menu


def use_tools(canvas: Canvas, selected_color_var: StringVar, figures: list):
    menu_selected_option = StringVar()
    menu_selected_option.set(next(iter(DRAW_TOOLS)))

    select = Select(canvas)

    Menu(canvas, selected_option=menu_selected_option,
         options=DRAW_TOOLS).create(select, selected_color_var, figures)
