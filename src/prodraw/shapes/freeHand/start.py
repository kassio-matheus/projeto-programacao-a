from prodraw.shapes import Shape

from .freeHand import FreeHand
from tkinter import *

class Start:
    


    @staticmethod
    def start(canvas: Canvas, bg: StringVar, obj):

        
        def start_points(event):
            freehand = FreeHand(canvas, bg, start_x=event.x, start_y=event.y)

            obj['obj'] = freehand

        return start_points
    

