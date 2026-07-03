from tkinter import *

from .toolbar import Toolbar
from .rectangle import Rectangle
from .circle import Circle
from .oval import Oval
from .line import Line
from .freedraw import FreeDraw

from .select import Select

from prodraw.workspace.color_picker import SHAPE_COLORS


# Constructs the main toolbar, initializes all drawing tool buttons, and sets the default selection
def use_tools(canvas: Canvas, width: int = 250, height: int = 50,
              background: str = "#303035", selected_color_var: StringVar = None, figures: list = None):
    toolsbar: Frame = Toolbar(
        canvas, width=width, height=height, background=background).create_toolbar()

    selected_option = StringVar(value="rectangle")
    select = Select(canvas, selected_option)
    select.select_option(selected_option.get(), selected_color_var, figures)

    rectangle_button = Rectangle(
        toolsbar, width=50, height=height, background=background,
        shape_colors=SHAPE_COLORS, selected_color_var=selected_color_var,
        selected_option=selected_option, selected_key="rectangle",
        command=lambda event: select.select_option(
            "rectangle", selected_color_var, figures),
        padding=12
    )

    rectangle_button.create_button()

    circle_button = Circle(
        toolsbar, width=50, height=height, background=background,
        shape_colors=SHAPE_COLORS, selected_color_var=selected_color_var,
        selected_option=selected_option, selected_key="circle",
        command=lambda event: select.select_option(
            "circle", selected_color_var, figures),
        padding=12
    )

    circle_button.create_button()

    oval_button = Oval(
        toolsbar, width=50, height=height, background=background,
        shape_colors=SHAPE_COLORS, selected_color_var=selected_color_var,
        selected_option=selected_option, selected_key="oval",
        command=lambda event: select.select_option(
            "oval", selected_color_var, figures),
        padding=15
    )

    oval_button.create_button()

    line_button = Line(
        toolsbar, width=50, height=height, background=background,
        shape_colors=SHAPE_COLORS, selected_color_var=selected_color_var,
        selected_option=selected_option, selected_key="line",
        command=lambda event: select.select_option(
            "line", selected_color_var, figures),
        padding=15
    )

    line_button.create_button()

    freedraw_button = FreeDraw(
        toolsbar, width=50, height=height, background=background,
        shape_colors=SHAPE_COLORS, selected_color_var=selected_color_var,
        selected_option=selected_option, selected_key="freedraw",
        command=lambda event: select.select_option(
            "freedraw", selected_color_var, figures),
        padding=15
    )

    freedraw_button.create_button()