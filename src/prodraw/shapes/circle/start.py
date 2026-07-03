from prodraw.shapes import Shape

from .circle import Circle
from tkinter import *

class Start:
    


    @staticmethod
    def start(canvas: Canvas, bg: StringVar, obj):

        
        def start_points(event):
            circle = Circle(canvas, bg, start_x=event.x, start_y=event.y)

            obj['obj'] = circle

        return start_points
    

