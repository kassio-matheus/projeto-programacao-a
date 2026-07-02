from src.shapes import Shape
from .draw import Draw
from src.shapes.colors import SHAPE_COLORS
from .start import Start
from tkinter import *
from .rectangle import Rectangle

class Update:
    
    @staticmethod
    def update(obj, figures: list):
        def update_points(event):
            obj["obj"].end_x = event.x
            obj["obj"].end_y = event.y
            Draw.draw(obj["obj"].canvas,figures)

            obj["obj"].canvas.create_rectangle(obj["obj"].start_x, obj["obj"].start_y, obj["obj"].end_x, obj["obj"].end_y,
                                          fill=SHAPE_COLORS.get(obj["obj"].bg), outline=obj["obj"].bg, tags="rectangle")
            
        return update_points

