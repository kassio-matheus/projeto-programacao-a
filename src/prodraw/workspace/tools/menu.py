from tkinter import *
from tkinter import ttk

from .select import Select


class Menu:
    """Creates and manages the tool selection dropdown menu."""
    
    # Initializes the menu with the canvas, selected state, and available tool options
    def __init__(self, canvas: Canvas, selected_option, options):
        self.canvas = canvas
        self.selected_option = selected_option
        self.options = options
        pass

    # Renders the dropdown menu and binds the selection event to activate the chosen tool
    def create(self, select: Select, selected_color_var: StringVar, figures: list):
        menu_tools = ttk.OptionMenu(self.canvas, self.selected_option,
                                    *self.options, command=lambda option: select.select_option(option, selected_color_var=selected_color_var, figures=figures))

        menu_tools.config(width=20)

        menu_tools.pack(side="bottom", anchor="se",
                        padx=30, pady=10, expand=False)