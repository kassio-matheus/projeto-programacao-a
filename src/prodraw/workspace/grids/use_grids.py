from tkinter import *
from .create import Create

# Initializes the Create handler and triggers the rendering of background grids
def use_grids (event: Event, canvas: Canvas, version: str):
    Create(canvas, version).create_grids(event)