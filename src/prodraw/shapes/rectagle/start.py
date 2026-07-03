from prodraw.shapes import Shape

from .rectangle import Rectangle
from tkinter import *

class Start:
    


    @staticmethod
    def start(canvas: Canvas, bg: StringVar, obj):

        
        def start_points(event):
            retangulo = Rectangle(canvas, bg, start_x=event.x, start_y=event.y)

            obj['obj'] = retangulo

        return start_points
    

