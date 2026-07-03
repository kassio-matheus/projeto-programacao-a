from tkinter import *


class Toolbar:
    """Creates and manages the main toolbar container."""
    
    # Initializes the toolbar frame properties
    def __init__(self, canvas: Canvas, width: int = 250, height: int = 50, background: str = "#303035"):
        self.width = width
        self.height = height
        self.canvas = canvas
        self.background = background

    # Renders and positions the toolbar at the bottom center of the canvas
    def create_toolbar(self):
        toolsbar = Frame(self.canvas, bg=self.background,
                         width=self.width, height=self.height)
        toolsbar.pack(side="bottom", anchor="center")
        #toolsbar.pack_propagate(False)
        toolsbar.place(relx=0.5, rely=1.0, anchor="s", y=-30)

        return toolsbar