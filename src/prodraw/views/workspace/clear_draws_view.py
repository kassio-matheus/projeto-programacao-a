from tkinter import Canvas

from prodraw.models.workspace.clear_draws_model import ClearDrawsModel
from prodraw.controllers.window import WindowController


class ClearDrawsView:
    """Renders the 'clear all drawings' button on the canvas."""

    def __init__(self, canvas: Canvas, model: ClearDrawsModel, window: WindowController, subItemMenu: str):
        self.canvas = canvas
        self.model = model
        self.window = window
        self.subItemMenu = subItemMenu

    def render(self, on_click):
        """Place the clear button at the bottom-right corner of the canvas."""
        
        self.window.update_menu(isSubItem=True, subItem=self.subItemMenu,
                                label=self.model.label, command=on_click)
