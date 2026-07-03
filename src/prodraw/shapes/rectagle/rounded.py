from tkinter import *


#Cria o retangulo com bordas (depois fazer isso)
def create_round_rectangle(canvas: Canvas, x1, y1, x2, y2, radius, **kwargs):    
    points = [x1+radius, y1,
              x1+radius, y1,
              x2-radius, y1,
              x2-radius, y1,
              x2, y1,
              x2, y1+radius,
              x2, y1+radius,
              x2, y2-radius,
              x2, y2-radius,
              x2, y2,
              x2-radius, y2,
              x2-radius, y2,
              x1+radius, y2,
              x1+radius, y2,
              x1, y2,
              x1, y2-radius,
              x1, y2-radius,
              x1, y1+radius,
              x1, y1+radius,
              x1, y1]
    
    return canvas.create_polygon(points, **kwargs, smooth=True)
    #rectangle = round_rectangle(50, 50, 150, 100, radius=20, fill="blue")