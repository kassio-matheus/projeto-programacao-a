from tkinter import *

from .picker import Picker
from .select import Select

from .config import COLORS


def use_color_picker(canvas):
    # global state of the color picker
    canvas_by_color = {}
    selected_color_var = StringVar(value=COLORS[0][0])  # "#FFFFFF"

    picker = Picker(canvas, canvas_by_color, selected_color_var)
    select = Select(selected_color_var, canvas_by_color)

    picker.create_color_picker(select)
    select.select_color("#FFFFFF")

    def get():
        return selected_color_var
    
    return get