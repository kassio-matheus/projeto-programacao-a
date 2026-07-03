"""Stores configuration and mappings for drawing tools."""

from prodraw.shapes import use_rectangle
from prodraw.shapes import use_circle
from prodraw.shapes import use_oval
from prodraw.shapes import use_line
from prodraw.shapes import use_freehand

# Maps UI option strings to their corresponding drawing tool initialization functions
DRAW_TOOLS = {
    'rectangle': use_rectangle,
    'circle': use_circle,
    'oval': use_oval,
    'line': use_line,
    'freedraw': use_freehand
}