from dataclasses import *
from tkinter import *

class Create:
    def __init__ (self, canvas: Canvas, version: str):
        self.canvas = canvas
        self.version = version

    def create_text_version(self):
        version_label = Label(
            self.canvas,
            text=f"ProDraw @{self.version}",
            fg="#3F3F3F",
            bg="#101010",
            font=("Helvetica", 12, "bold")
        )

        version_label.place(relx=0, rely=1, x=30, y=-30, anchor="sw")
