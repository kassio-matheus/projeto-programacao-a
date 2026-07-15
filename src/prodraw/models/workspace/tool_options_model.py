from tkinter import StringVar

# Styling constants matching the Color Picker panel
PANEL_BG = "#1c1c22"
SELECTED_BG = "#3a3a42"
BUTTON_SIZE = 30  # Slightly larger to comfortably fit the drawn shapes


class ToolOptionsModel:
    """
    Holds the data and state for the tool options panel.
    Manages the currently selected fill, border, and size options.
    """

    def __init__(self):
        # Define available options mapped to unique string identifiers
        self.fills = ["solid_border", "solid_no_border", "no_solid_border"]
        self.borders = ["solid", "dotted"]
        self.sizes = ["S", "M", "L", "XL"]

        # Default selections
        self.selected_fill_var = StringVar(value="solid_border")
        self.selected_border_var = StringVar(value="solid")
        self.selected_size_var = StringVar(value="M")

        # Dictionary to store the canvas references for highlighting by option key
        self.canvas_by_option: dict = {}

    def set_fill(self, fill_type: str) -> None:
        """Sets the selected fill type."""
        self.selected_fill_var.set(fill_type)

    def get_fill(self) -> str:
        """Gets the selected fill type."""
        return self.selected_fill_var.get()

    def set_border(self, border_type: str) -> None:
        """Sets the selected border type."""
        self.selected_border_var.set(border_type)

    def get_border(self) -> str:
        """Gets the selected border type."""
        return self.selected_border_var.get()

    def set_size(self, size: str) -> None:
        """Sets the selected font/line size."""
        self.selected_size_var.set(size)

    def get_size(self) -> str:
        """Gets the selected font/line size."""
        return self.selected_size_var.get()
