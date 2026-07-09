from tkinter import Canvas, Frame
from prodraw.models.workspace.color_picker_model import ColorPickerModel, PANEL_BG, SELECTED_BG, BUTTON_SIZE


class ColorPickerView:
    """Renders the color picker panel and its circular color buttons."""

    def __init__(self, canvas: Canvas, model: ColorPickerModel):
        self.canvas = canvas
        self.model = model
        self.panel = Frame(canvas, bg=PANEL_BG, padx=12, pady=12)

    def build(self, on_color_click):
        """Build the full color grid and pin the panel to the top-right corner."""
        for row, row_colors in enumerate(self.model.colors):
            for col, color in enumerate(row_colors):
                self._create_button(row, col, color, on_color_click)
        self.panel.place(relx=1.0, x=-16, y=16, anchor="ne")

    def _create_button(self, row, col, color, on_color_click):
        """Create a single circular color swatch button."""
        from tkinter import Canvas as TkCanvas
        cv = TkCanvas(self.panel, width=BUTTON_SIZE, height=BUTTON_SIZE,
                      bg=PANEL_BG, highlightthickness=0, cursor="hand2")
        cv.grid(row=row, column=col, padx=4, pady=4)
        cv.create_oval(6, 6, BUTTON_SIZE - 6, BUTTON_SIZE - 6, fill=color, outline="")
        cv.bind("<Button-1>", lambda e, c=color: on_color_click(c))
        self.model.canvas_by_color[color] = cv

    def highlight(self, color: str):
        """Highlight the button for the given color."""
        self.model.canvas_by_color[color].config(bg=SELECTED_BG)

    def unhighlight(self, color: str):
        """Remove highlight from the given color button."""
        if color in self.model.canvas_by_color:
            self.model.canvas_by_color[color].config(bg=PANEL_BG)
