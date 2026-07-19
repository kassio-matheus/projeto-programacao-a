from tkinter import Menu
from prodraw.models.window import MenubarCommand


class MenubarCommandView:
    """Button in menu, inside on cascade."""

    def __init__(self, model: MenubarCommand):
        self.model = model

    def add_command(self, target_menu: Menu):
        target_menu.add_command(
            label=self.model.label,
            command=self.model.command,
        )
