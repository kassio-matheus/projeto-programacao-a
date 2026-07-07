from tkinter import *

from prodraw.models import Circle
from prodraw.views import CircleView


class CircleController:

    obj = {'obj': None}

    @staticmethod
    def start(bg: StringVar):
        circle = Circle(bg=bg)

        def start_circle(event):
            circle.start(event)

        CircleController.obj['obj'] = circle
        return start_circle

    @staticmethod
    def update(view: CircleView):
        circle = CircleController.obj['obj']

        def update_circle(event):
            circle.update(event)

            if circle.empty():
                view.draw(circle)

        return update_circle

    @staticmethod
    def add(view: CircleView, figures: dict):
        circle = CircleController.obj['obj']

        def add_circle(event):

            circle.add(figures)
            view.draw_all(figures)

        return add_circle

    @staticmethod
    def delete(view: CircleView):
        view.delete()
