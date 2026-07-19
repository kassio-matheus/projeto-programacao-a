from tkinter import Menu
from prodraw.models.window import MenubarCascade


class MenubarCascadeView:
    """Button in menu, the principal button, A.K.A button of buttons."""
    
    def __init__(self, model: MenubarCascade):
        self.model = model

    def add_cascade(self, target_menu: Menu):
        target_menu.add_cascade(
            label=self.model.label,
            menu=self.model.menu,
            underline=self.model.underline
        )
