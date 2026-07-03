from tkinter import *

class Zoom:
    def __init__(self, canvas: Canvas):
        self.canvas = canvas
        pass

    factor = 1.0
    STEP = 0.1
    MIN = 0.1
    MAX = 2

    def scale(self, event):

        x = self.canvas.canvasx(event.x)
        y = self.canvas.canvasy(event.y)

        if event.delta > 0:
            new_factor = min(round(Zoom.factor + Zoom.STEP, 1), Zoom.MAX)
        else:
            new_factor = max(round(Zoom.factor - Zoom.STEP, 1), Zoom.MIN)

        if new_factor == Zoom.factor:
            return  # já está no limite, não faz nada

        # fator RELATIVO em relação ao estado atual do canvas
        scale_step = new_factor / Zoom.factor
        self.canvas.scale("shape", x, y, scale_step, scale_step)
        # schedule_grid_update()

        Zoom.factor = new_factor
