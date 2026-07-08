"""Stores configuration and mappings for drawing tools."""

from prodraw.shapes import use_freehand

from prodraw.controllers.shapes import circle_bind
from prodraw.controllers.shapes import rectangle_bind
from prodraw.controllers.shapes import oval_bind
from prodraw.controllers.shapes import line_bind

# Maps UI option strings to their corresponding drawing tool initialization functions
DRAW_TOOLS = {
    'rectangle': rectangle_bind,
    'circle': circle_bind,
    'oval': oval_bind,
    'line': line_bind,
    'freedraw': use_freehand
}