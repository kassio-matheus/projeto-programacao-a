from tkinter import *
from .create import Create

def use_grids (event: Event, canvas: Canvas, version: str):
    Create(canvas, version).create_grids(event)