"""Stores configuration and mappings for drawing tools."""

from prodraw.shapes import use_rectangle
from prodraw.shapes import use_circle
from prodraw.shapes import use_oval
from prodraw.shapes import use_line
from prodraw.shapes import use_freehand

# Maps UI option strings to their corresponding drawing tool initialization functions
DRAW_TOOLS = {
    'Desenhar um:': None,
    'Quadrado': use_rectangle,
    'Círculo': use_circle,
    'Oval': use_oval,
    'Linha': use_line,
    'Mão livre': use_freehand
}