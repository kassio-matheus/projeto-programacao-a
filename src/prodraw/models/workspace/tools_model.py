from tkinter import StringVar

from prodraw.controllers.shapes import (
    circle_bind, rectangle_bind, oval_bind, line_bind, freedraw_bind, square_bind
)

from prodraw.controllers.shapes.rectangle.rectangle_controller import *
from prodraw.controllers.shapes.oval.oval_controller import *
from prodraw.controllers.shapes.line.line_controller import *

# Maps tool key strings to their shape controller bind functions
DRAW_TOOLS = {
    'rectangle': (RectangleController(), RectangleView()),
    'square': square_bind,
    'circle':    circle_bind,
    'oval':      (OvalController(), OvalView()),
    'line':      (LineController(), LineView()),
    'freedraw':  freedraw_bind,
}

DEFAULT_TOOL = 'rectangle'


class ToolsModel:
    """Holds the available drawing tools and the currently active one."""

    def __init__(self):
        self.tools = DRAW_TOOLS
        self.selected_option = StringVar(value=DEFAULT_TOOL)
        # Holds the active shape controller so it can be unbound on tool switch
        self.active_controller = None
