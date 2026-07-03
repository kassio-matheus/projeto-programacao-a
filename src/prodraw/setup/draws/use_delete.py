from tkinter import *

from .delete import Delete

def use_delete_draws(canvas: Canvas, figures: list):
    Delete(canvas, figures).delete_all_draws()
