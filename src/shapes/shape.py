from tkinter import *

from abc import *

class Shape (ABC):
    def __init__ (self, canvas: Canvas, bg: StringVar, figures: list):
        self.canvas = canvas
        self.bg = bg
        self.figures = figures

        self.start_x = None
        self.start_y = None
        self.end_x = None
        self.end_y = None

    @abstractmethod
    def start():
        pass

    @abstractmethod
    def update():
        pass

    @abstractmethod
    def add():
        pass

    @abstractmethod
    def draw():
        pass

    @abstractmethod
    def bind(self, isFreeHand=False):
        self.canvas.bind('<ButtonPress-1>', self.start)
        self.canvas.bind('<B1-Motion>', self.update)
        
        if(isFreeHand != True):
           self.canvas.bind('<ButtonRelease-1>', self.add)