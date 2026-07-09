from tkinter import Canvas
from prodraw.models.workspace.text_version_model import TextVersionModel
from prodraw.views.workspace.text_version_view import TextVersionView


class TextVersionController:
    """Sets up and displays the version watermark."""

    def __init__(self, canvas: Canvas, version: str):
        self.model = TextVersionModel(version)
        self.view = TextVersionView(canvas, self.model)

    def setup(self):
        self.view.render()
