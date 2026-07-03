from tkinter import *
from abc import ABC, abstractmethod


class Button(ABC):
    def __init__(self, toolsbar: Frame, width: int = 50, height: int = 50,
                 command=None, watch_vars: tuple = ()):
        self.toolsbar = toolsbar
        self.width = width
        self.height = height
        self.command = command

        self.canvas = Canvas(self.toolsbar, width=self.width,
                              height=self.height, bg="#303035", highlightthickness=0)
        self.canvas.bind("<Button-1>", self.command)

        self.icon_id = None

        for var in watch_vars:
            if var is not None:
                var.trace_add("write", lambda *_: self.draw())

    @abstractmethod
    def draw(self):
        """Subclasse desenha o ícone em self.canvas e define self.icon_id."""
        pass

    def create_button(self):
        self.draw()
        self.canvas.pack(side=LEFT)
        return self.canvas