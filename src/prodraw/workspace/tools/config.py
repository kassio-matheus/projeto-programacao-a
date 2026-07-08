"""Stores configuration and mappings for drawing tools."""

from prodraw.shapes import use_oval
from prodraw.shapes import use_line
from prodraw.shapes import use_freehand

from prodraw.controllers.shapes import circle_bind
from prodraw.controllers.shapes import rectangle_bind

# Maps UI option strings to their corresponding drawing tool initialization functions
DRAW_TOOLS = {
    'rectangle': rectangle_bind,
    'circle': circle_bind,
    'oval': use_oval,
    'line': use_line,
    'freedraw': use_freehand
}