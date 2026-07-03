from tkinter import *
from .create import Create

def use_text_version (canvas: Canvas, version: str):
    Create(canvas, version).create_text_version()