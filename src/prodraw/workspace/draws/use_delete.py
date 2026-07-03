from tkinter import *

from .delete import Delete


# Initializes the Delete handler and triggers the removal of all drawings
def use_delete_draws(canvas: Canvas, figures: list):
    Delete(canvas, figures).delete_all_draws()