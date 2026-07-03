from prodraw.shapes import Shape

from .line import Line
from tkinter import *

class Start:
    


    @staticmethod
    def start(canvas: Canvas, bg: StringVar, obj):

        
        def start_points(event):
            line = Line(canvas, bg, start_x=event.x, start_y=event.y)

            obj['obj'] = line

        return start_points
    

