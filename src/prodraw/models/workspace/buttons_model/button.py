from tkinter import *
from abc import ABC, abstractmethod


class Button(ABC):
    """Abstract base class for creating toolbar tool buttons."""
    
    # Initializes button dimensions, event bindings, and state observers
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
    # Subclass draws the icon on self.canvas and sets self.icon_id
    def draw(self):
        pass

    # Renders the button and packs it into the toolbar
    def create_button(self):
        self.draw()
        self.canvas.pack(side=LEFT)
        return self.canvas