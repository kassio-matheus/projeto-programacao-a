from tkinter import Canvas, Label
from prodraw.models.workspace.text_version_model import TextVersionModel


class TextVersionView:
    """Renders the version watermark label on the canvas."""

    def __init__(self, canvas: Canvas, model: TextVersionModel):
        self.canvas = canvas
        self.model = model

    def render(self):
        """Place the version label at the bottom-left corner of the canvas."""
        label = Label(
            self.canvas, text=self.model.text,
            fg=self.model.fg, bg=self.model.bg, font=self.model.font
        )
        label.place(relx=0, rely=1, x=30, y=-30, anchor="sw")
