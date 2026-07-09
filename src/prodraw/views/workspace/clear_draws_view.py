from tkinter import Canvas
from tkinter import ttk
from prodraw.models.workspace.clear_draws_model import ClearDrawsModel


class ClearDrawsView:
    """Renders the 'clear all drawings' button on the canvas."""

    def __init__(self, canvas: Canvas, model: ClearDrawsModel):
        self.canvas = canvas
        self.model = model

    def render(self, on_click):
        """Place the clear button at the bottom-right corner of the canvas."""
        btn = ttk.Button(self.canvas, text=self.model.label, command=on_click)
        btn.pack(side="bottom", anchor="se", padx=30, pady=(0, 30), expand=False)
