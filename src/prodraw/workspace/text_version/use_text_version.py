from tkinter import *
from .create import Create


# Initializes the Create handler and triggers the display of the version text
def use_text_version (canvas: Canvas, version: str):
    Create(canvas, version).create_text_version()