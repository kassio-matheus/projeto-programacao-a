from tkinter import *

from .text_version import use_text_version
from .grids import use_grids
from .color_picker import use_color_picker
from .draws import use_delete_draws
from .buttons import use_clear_draw
from .tools import use_tools

from .color_picker import COLORS


class Setup:
    """Main screen setup - Groups all functions"""

    def __init__(self, root, version):
        self.root = root
        self.canvas: Canvas = Canvas(root, bg='#101010', highlightthickness=0,
                                     relief="flat", borderwidth=0)
        self.figures = list()
        self.version = version

    def start(self):
        self.canvas.pack(fill="both", expand=True)
        use_text_version(self.canvas, version=self.version)

        self.canvas.bind("<Configure>", lambda event: use_grids(
            event, self.canvas, self.version))

        picker_getter = use_color_picker(self.canvas)
        selected_color_var = picker_getter()  # chama get(), retorna o StringVar

        use_clear_draw(self.canvas, self.figures)

        use_tools(self.canvas, selected_color_var, self.figures)
