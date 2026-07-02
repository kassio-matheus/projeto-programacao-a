from tkinter import *

from abc import *

from dataclasses import *

from typing import ClassVar


@dataclass
class Shape (ABC):



    canvas: Canvas
    bg: StringVar


    start_x: float = None
    start_y: float = None
    end_x: float = None
    end_y: float = None


    @property
    def bg(self):
        return self._bg
    
    @bg.setter
    def bg(self, bg:StringVar):
        self._bg = bg.get()

    @abstractmethod
    def bind(self, start, update, add):
        self.canvas.bind('<ButtonPress-1>', start)
        self.canvas.bind('<B1-Motion>', update)
        self.canvas.bind('<ButtonRelease-1>', add)