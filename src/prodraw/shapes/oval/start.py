from prodraw.shapes import Shape

from .oval import Oval
from tkinter import *

class Start:
    


    @staticmethod
    def start(canvas: Canvas, bg: StringVar, obj):

        
        def start_points(event):
            oval = Oval(canvas, bg, start_x=event.x, start_y=event.y)

            obj['obj'] = oval

        return start_points
    

