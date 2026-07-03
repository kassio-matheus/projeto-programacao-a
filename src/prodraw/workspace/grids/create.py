from dataclasses import *
from tkinter import *

from prodraw.workspace.text_version import use_text_version

class Create:
    """Handles the generation of the background grid and version text on the canvas."""
    
    # Initializes the grid creator with the target canvas and application version
    def __init__ (self, canvas: Canvas, version: str):
        self.canvas = canvas
        self.version = version

    # Clears existing grids and dynamically draws a dotted background grid based on canvas size
    def create_grids(self, event: Event):
        self.canvas.delete("grids")
        self.canvas.delete("version_text")

        width = self.canvas.winfo_width()
        height = self.canvas.winfo_height()

        # Adjust by zoom - Waiting for implement
        GRID_SIZE = 50

        for x in range(0, width, GRID_SIZE):
            for y in range(0, height, GRID_SIZE):
                self.canvas.create_oval(
                    x - 1, y - 1, x + 1, y + 1,
                    fill="#5B5B5B", outline="",
                    tags="grids",
                )

        self.canvas.tag_lower("grids")

        use_text_version(self.canvas, self.version)