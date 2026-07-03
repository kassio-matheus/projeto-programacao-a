from prodraw.shapes import use_rectangle
from prodraw.shapes import use_circle
from prodraw.shapes import use_oval
from prodraw.shapes import use_line
from prodraw.shapes import use_freehand

DRAW_TOOLS = {
    'Desenhar um:': None,
    'Quadrado': use_rectangle,
    'Círculo': use_circle,
    'Oval': use_oval,
    'Linha': use_line,
    'Mão livre': use_freehand
}
