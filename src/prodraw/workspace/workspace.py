from tkinter import *

from .text_version import use_text_version
from .grids import use_grids
from .color_picker import use_color_picker
from .buttons import use_clear_draw
from .tools import use_tools
from .zoom import use_zoom


class Workspace:
    """Main screen setup - Groups all functions"""

    def __init__(self, root, version):
        self.root = root
        self.canvas: Canvas = Canvas(root, bg='#101010', highlightthickness=0,
                                     relief="flat", borderwidth=0)
        self.figures = {'Circle': [], 'Rectangle': [], 'Oval': []}
        self.version = version

    def start(self):
        self.canvas.pack(fill="both", expand=True)
        use_text_version(self.canvas, version=self.version)

        self.canvas.bind("<Configure>", lambda event: use_grids(
            event, self.canvas, self.version))

        picker_getter = use_color_picker(self.canvas)
        selected_color_var = picker_getter()

        use_clear_draw(self.canvas, self.figures)

        use_tools(self.canvas, width=300, height=50, selected_color_var=selected_color_var,
                  figures=self.figures)  # call use_tools with width and height to create the tools bar

        self.canvas.bind(
            "<MouseWheel>", lambda event: use_zoom(event, self.canvas))

        # Restore the last version of figures - A.K.A CTRL + Z
        # self.root.bind("<Control-z>", lambda event: self.figures.set(self.figures.get().pop()))
        # self.root.bind("<Command-z>", lambda event: self.figures.set(self.figures.get().pop()))
