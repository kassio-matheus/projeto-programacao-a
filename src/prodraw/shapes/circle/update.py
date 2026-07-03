from prodraw.shapes import Shape
from .draw import Draw
from prodraw.shapes.colors import SHAPE_COLORS
from .start import Start
from tkinter import *


class Update:
    
    @staticmethod
    def update(obj, figures: list):
        def update_points(event):
            obj["obj"].end_x = event.x
            obj["obj"].end_y = event.y
            obj['obj'].raio = ((obj['obj'].start_x - obj['obj'].end_x)**2 + (obj['obj'].start_y - obj['obj'].end_y)**2) ** 0.5
            Draw.draw(obj["obj"].canvas,figures)

            obj["obj"].canvas.create_oval(obj["obj"].start_x-obj['obj'].raio, obj["obj"].start_y-obj['obj'].raio, obj["obj"].start_x+obj['obj'].raio, 
                                          obj["obj"].start_y+obj['obj'].raio,fill=SHAPE_COLORS.get(obj["obj"].bg), outline = obj['obj'].bg, tags="circle")
            
        return update_points

