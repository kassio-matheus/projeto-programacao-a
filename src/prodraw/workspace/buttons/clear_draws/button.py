from tkinter import *
from tkinter import ttk

from prodraw.workspace.draws import use_delete_draws


class Button:
    """Creates and manages UI buttons for the canvas."""
    
    # Initializes the button with the target canvas and figure list
    def __init__(self, canvas: Canvas, figures: list):
        self.canvas = canvas
        self.figures = figures

    # Creates and displays a button to clear all drawings from the canvas
    def create(self):
        clear_button = ttk.Button(
            self.canvas, text="Limpar desenhos", command=lambda: use_delete_draws(self.canvas, self.figures))

        clear_button.pack(side="bottom", anchor="se",
                          padx=30, pady=(0, 30), expand=False)